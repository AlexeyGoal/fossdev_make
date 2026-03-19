
import ast
import sys
from pathlib import Path

def get_imports_from_file(filepath):
    """Извлекает все импорты из Python файла"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        imports = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
        
        return imports
    except Exception as e:
        print(f"Ошибка при анализе {filepath}: {e}")
        return set()

def get_requirements(req_file):
    """Извлекает имена пакетов из requirements.txt"""
    requirements = set()
    try:
        with open(req_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Убираем версии и опции
                    pkg = line.split('==')[0]
                    pkg = pkg.split('>=')[0]
                    pkg = pkg.split('<=')[0]
                    pkg = pkg.split('~=')[0]
                    pkg = pkg.split('[')[0]
                    pkg = pkg.split(';')[0]
                    requirements.add(pkg.lower().strip())
    except FileNotFoundError:
        print(f"Файл {req_file} не найден")
        return set()
    
    return requirements

def main():
    # Стандартные библиотеки Python
    std_libs = {
        'sys', 'os', 're', 'json', 'datetime', 'math', 'random',
        'time', 'collections', 'itertools', 'functools', 'pathlib',
        'typing', 'logging', 'argparse', 'copy', 'enum', 'hashlib',
        'hmac', 'glob', 'shutil', 'subprocess', 'threading',
        'unittest', 'urllib', 'uuid', 'warnings', 'abc', 'io',
        'pickle', 'socket', 'ssl', 'tempfile', 'zipfile', 'csv',
        'xml', 'html', 'http', 'ftplib', 'select', 'asyncio'
    }
    
    # Получаем импорты из main.py
    if not Path('main.py').exists():
        print("❌ Файл main.py не найден в текущей директории")
        sys.exit(1)
    
    imports = get_imports_from_file('main.py')
    
    # Убираем стандартные библиотеки
    third_party_imports = {imp for imp in imports if imp not in std_libs}
    
    print("=" * 60)
    print("СРАВНЕНИЕ main.py С requirements.txt")
    print("=" * 60)
    
    print(f"\n📊 Статистика:")
    print(f"  - Всего импортов в main.py: {len(imports)}")
    print(f"  - Сторонних библиотек: {len(third_party_imports)}")
    
    if third_party_imports:
        print(f"\n📦 Сторонние библиотеки в main.py:")
        for imp in sorted(third_party_imports):
            print(f"  • {imp}")
    
    # Получаем зависимости из requirements.txt
    requirements = get_requirements('requirements.txt')
    
    if requirements:
        print(f"\n📋 Пакеты в requirements.txt ({len(requirements)}):")
        for req in sorted(requirements):
            print(f"  • {req}")
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:")
    print("=" * 60)
    
    # Импорты, которых нет в requirements.txt
    missing = third_party_imports - requirements
    if missing:
        print("\n❌ Импорты из main.py, ОТСУТСТВУЮЩИЕ в requirements.txt:")
        for imp in sorted(missing):
            print(f"  • {imp}")
        print(f"\n  💡 Добавьте в requirements.txt: pip install {' '.join(missing)}")
    
    # Лишние пакеты в requirements.txt (не используются в main.py)
    extra = requirements - third_party_imports
    if extra:
        print("\n⚠️  Пакеты в requirements.txt, НЕ ИСПОЛЬЗУЕМЫЕ в main.py:")
        for pkg in sorted(extra):
            print(f"  • {pkg}")
        print(f"\n  💡 Возможно, они используются в других файлах")
    
    # Совпадающие пакеты
    common = third_party_imports & requirements
    if common:
        print(f"\n✅ Совпадающие пакеты ({len(common)}):")
        # Показываем первые 10, если их много
        common_list = sorted(common)
        if len(common_list) > 10:
            print(f"  {', '.join(common_list[:10])} ... и еще {len(common_list)-10}")
        else:
            print(f"  {', '.join(common_list)}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    main()
import sys, os


def install_package(name):
    print(f"{name}尚未安装,开始自动安装")
    from pip._internal.cli.main import main as _main

    try:
        _main(["install", name, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    except:
        print("安装失败!")
        sys.exit(0)


try:
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
except ModuleNotFoundError:
    install_package("pyyaml")
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper


def handler(filename):
    def a(func):
        def b():
            print(f"开始配置{filename}")
            if not os.path.exists(filename):
                print(f"{filename}不存在,跳过")
                return
            try:
                with open(filename, 'r+', encoding="utf8") as fp:
                    config = yaml.load(fp, Loader=Loader)

                func(config)
                with open(filename, 'w+', encoding="utf8") as fp:
                    yaml.dump(config, fp, Dumper=Dumper)
            except Exception as e:
                print(f"错误:{e}")
            else:
                print(f"完成配置{filename}")

        return b

    return a


def ask(title):
    select = input(title + "(y/n):")
    if select.lower().startswith("y"):
        return True
    return False


def exit_():
    print("回车退出")
    input()
    sys.exit(0)
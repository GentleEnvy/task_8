from src.data_parser import Parser
from src.data_renderer import Renderer


def main():
    parser = Parser()
    render = Renderer(parser.data)
    render.figure.show()


if __name__ == '__main__':
    main()

import argparse
import ast


def main(methods, params):
    methods_list = ast.literal_eval(methods)
    params_list = ast.literal_eval(params)

    for i in range(len(methods_list)):
        print(f'{methods_list[i]}({params_list[i]});')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert two string representations of lists to actual lists')
    parser.add_argument('methods', type=str, help='First list of methods')
    parser.add_argument('params', type=str, help='Second list of parameters')

    args = parser.parse_args()

    main(args.methods, args.params)

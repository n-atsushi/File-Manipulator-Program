import os
import sys

def reverse(input_file, output_path):
    with open(input_file) as i_f:
        contents = i_f.read()
        output_file = os.path.join(output_path, 'r_' + os.path.basename(input_file))
        with open(output_file, 'w') as o_p:
            o_p.write(contents[::-1])
        print(f'=== create {output_file} ===')

def copy(input_file, output_path):
    with open(input_file) as i_f:
        contents = i_f.read()
        output_file = os.path.join(output_path, 'c_' + os.path.basename(input_file))
        with open(output_file, 'w') as o_p:
            o_p.write(contents)
        print(f'=== create {output_file} ===')

def duplicate_contents(input_file, n):
    with open(input_file) as i_f:
        contents = i_f.read()
        print(f'=== duplicate {n} files ===')
        for i in range(n):
            output_file = os.path.join(os.path.dirname(input_file), f'd_{i + 1}_' + os.path.basename(input_file))
            with open(output_file, 'w') as o_p:
                o_p.write(contents)
        print('=========================')

def replace_string(input_file, before_word, after_word):
    with open(input_file, 'r') as i_f:
        contents = i_f.read()
    with open(input_file, 'w') as i_w:
        i_w.write(contents.replace(before_word, after_word))   

def main():
    cmd = {
       'reverse': [reverse, 4],
       'copy' : [copy, 4],
       'duplicate_contents' : [duplicate_contents, 4],
       'replace_string' : [replace_string, 5]
    }    
    try:
        print(f'*** {sys.argv[1]} ***')
        
        func, arg_num = cmd.get(sys.argv[1])
        
        if func is None or len(sys.argv) < arg_num:
            raise Exception('Invalid arguments')
        
        func(*sys.argv[2:arg_num])
        
        print(f'*** Success {func.__name__} ***')
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
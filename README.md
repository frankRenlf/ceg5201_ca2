# ceg5201_ca2

use this to get the latest version of the code

```bash
git pull
```

use this to run all, and the time consumption result will print in the terminal.

```bash
python main.py
```

choose this func to print the result in the terminal

```text
run2terminal()
```

and if you want to save the result to file, you can use

```text
run2file()
```

if you want to change the process, you can change the 'algorithm'_multiprocessing.py in
matricx_multiply_algorithms/'algorithm'.
However, it has some constraints with the depth of the recursion, and you need to adjust the depth of the recursion to
make it work well, or the speed will not grow up with the number of the process.

```text
processes = cpu_count()
```
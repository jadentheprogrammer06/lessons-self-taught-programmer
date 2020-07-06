# code in module4. code in module3 will not run when imported to this new script because it is not the original "name" of the code's originating module.

import module3

# functions from the imported module still work properly. But test code and the like is not ran.
module3.print_hello()

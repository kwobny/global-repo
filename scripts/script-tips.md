# Some tips related to scripts (making, using, etc.)  

## Cool Bash utilities:  
1. `realpath`
    - Allows you to:
        - Get the absolute path of a file or directory given relative path.
        - Get the path of something relative to another path (file or directory).

## Cool tricks:  
1. If there is a script that you want to run repeatedly but don't want to type out its path every time, you can set an alias to the absolute path of the script (or relative, maybe but idk why you would do that). To get the absolute path, use the realpath command.
    - Ex. `alias scriptname=$(realpath RELATIVE_PATH)`

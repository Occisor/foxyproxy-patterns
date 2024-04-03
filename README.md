### Features

Patterns for [FoxyProxy](https://getfoxyproxy.org/help/browsers/), used to access some sites.  
Also a script for creating your own.  
Often used as samples of GitHub  [Domain list community](https://github.com/v2fly/domain-list-community)  

### How to use patterns
Find the patterns you need in the [directory](https://github.com/Occisor/foxyproxy-patterns/tree/main/patterns) and import into FoxyProxy

### How to use script
Scripts name is [fp-pat.py](https://github.com/Occisor/foxyproxy-patterns/blob/main/fp-pat.py)
Before using it, make sure that you have prepared the files for subsequent processing by the script.
These must be files without an extension containing site names. There is only one site on each line.  
For example, the [protonmail](https://github.com/v2fly/domain-list-community/blob/master/data/protonmail) file contains the lines:
```
pm.me
proton.me
protonmail.ch
protonmail.com
protonstatus.com
```
Place the prepared files in an empty separate directory, copy the script into it and run it.
```
python3 ./fp-pat.py
```
After it processes all the files, files with the .json extension will appear in the folder; they can be imported into FoxyProxy.  
`protonmail.json` example:
```
[
  {
    "include": "include",
    "type": "wildcard",
    "title": "protonmail",
    "pattern": "*://*.pm.me",
    "active": true
  },
  {
    "include": "include",
    "type": "wildcard",
    "title": "protonmail",
    "pattern": "*://*.proton.me",
    "active": true
  },
  {
    "include": "include",
    "type": "wildcard",
    "title": "protonmail",
    "pattern": "*://*.protonmail.ch",
    "active": true
  },
  {
    "include": "include",
    "type": "wildcard",
    "title": "protonmail",
    "pattern": "*://*.protonmail.com",
    "active": true
  },
  {
    "include": "include",
    "type": "wildcard",
    "title": "protonmail",
    "pattern": "*://*.protonstatus.com",
    "active": true
  }
]
```


### What to do in the future:
Improve the cleaning script for files (it is not publicly available at the moment) from domain-list-community. Now it removes lines containing: #, :, @. Which may contain additional instructions for [V2Ray](https://www.v2ray.com/), or full paths.  
.  
..  
...   
Donat  
[![](https://upload.wikimedia.org/wikipedia/ru/thumb/a/ad/DA_Logo_Color.svg/440px-DA_Logo_Color.svg.png)](https://www.donationalerts.com/r/sociophobenoob)

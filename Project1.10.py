Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> "modules"

Please wait a moment while I gather a list of all available modules...

__future__          asyncio             history             scrolledlist
__main__            asyncore            hmac                search
_abc                atexit              html                searchbase
_ast                audioop             http                searchengine
_asyncio            autocomplete        hyperparser         secrets
_bisect             autocomplete_w      idle                select
_blake2             autoexpand          idle_test           selectors
_bootlocale         base64              idlelib             setuptools
_bz2                bdb                 imaplib             shelve
_codecs             binascii            imghdr              shlex
_codecs_cn          binhex              imp                 shutil
_codecs_hk          bisect              importlib           sidebar
_codecs_iso2022     browser             inspect             signal
_codecs_jp          builtins            io                  site
_codecs_kr          bz2                 iomenu              smtpd
_codecs_tw          cProfile            ipaddress           smtplib
_collections        calendar            itertools           sndhdr
_collections_abc    calltip             json                socket
_compat_pickle      calltip_w           keyword             socketserver
_compression        cgi                 lib2to3             sqlite3
_contextvars        cgitb               linecache           squeezer
_csv                chunk               locale              sre_compile
_ctypes             cmath               logging             sre_constants
_ctypes_test        cmd                 lzma                sre_parse
_datetime           code                macosx              ssl
_decimal            codecontext         mailbox             stackviewer
_dummy_thread       codecs              mailcap             stat
_elementtree        codeop              mainmenu            statistics
_functools          collections         marshal             statusbar
_hashlib            colorizer           math                string
_heapq              colorsys            mimetypes           stringprep
_imp                compileall          mmap                struct
_io                 concurrent          modulefinder        subprocess
_json               config              msilib              sunau
_locale             config_key          msvcrt              symbol
_lsprof             configdialog        multicall           symtable
_lzma               configparser        multiprocessing     sys
_markupbase         contextlib          netrc               sysconfig
_md5                contextvars         nntplib             tabnanny
_msi                copy                nt                  tarfile
_multibytecodec     copyreg             ntpath              telnetlib
_multiprocessing    crypt               nturl2path          tempfile
_opcode             csv                 numbers             test
_operator           ctypes              opcode              textview
_osx_support        curses              operator            textwrap
_overlapped         dataclasses         optparse            this
_pickle             datetime            os                  threading
_py_abc             dbm                 outwin              time
_pydecimal          debugger            parenmatch          timeit
_pyio               debugger_r          parser              tkinter
_queue              debugobj            pathbrowser         token
_random             debugobj_r          pathlib             tokenize
_sha1               decimal             pdb                 tooltip
_sha256             delegator           percolator          trace
_sha3               difflib             pickle              traceback
_sha512             dis                 pickletools         tracemalloc
_signal             distutils           pip                 tree
_sitebuiltins       doctest             pipes               tty
_socket             dummy_threading     pkg_resources       turtle
_sqlite3            dynoption           pkgutil             turtledemo
_sre                easy_install        platform            types
_ssl                editor              plistlib            typing
_stat               email               poplib              undo
_statistics         encodings           posixpath           unicodedata
_string             ensurepip           pprint              unittest
_strptime           enum                profile             urllib
_struct             errno               pstats              uu
_symtable           faulthandler        pty                 uuid
_testbuffer         filecmp             py_compile          venv
_testcapi           fileinput           pyclbr              warnings
_testconsole        filelist            pydoc               wave
_testimportmultiple fnmatch             pydoc_data          weakref
_testmultiphase     format              pyexpat             webbrowser
_thread             formatter           pyparse             window
_threading_local    fractions           pyshell             winreg
_tkinter            ftplib              query               winsound
_tracemalloc        functools           queue               wsgiref
_warnings           gc                  quopri              xdrlib
_weakref            genericpath         random              xml
_weakrefset         getopt              re                  xmlrpc
_winapi             getpass             redirector          xxsubtype
_xxsubinterpreters  gettext             replace             zipapp
abc                 glob                reprlib             zipfile
aifc                grep                rlcompleter         zipimport
antigravity         gzip                rpc                 zlib
argparse            hashlib             run                 zoomheight
array               heapq               runpy               zzdummy
ast                 help                runscript           
asynchat            help_about          sched               

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> "topics"

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> "keywords"

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> "symbols"

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> 
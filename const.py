"""Jd2chm constants"""

# Set to 1 uses a custom CSS. If 0, uses the default Javadoc CSS (recommended)
CUSTOM_CSS = 0

# Reuse temp file (mostly for development or to avoid copying large Javadoc like the JDK API
REUSE_TEMP_FILES = 0

MAX_SIZE_KEYWORD = 300

# jd2chm version
VERSION = "1.0.0b1"

# Temporary working directory
WORKING_DIR = "jd2chm"

# Uses the HTML Help compiler installed via HTML Help Workshop (default)
EXTERNAL_COMPILER = 1

# CRITICAL = 5, ERROR = 4, WARNING = 3, INFO = 2, DEBUG = 1, NOTSET = 0.
LOG_LEVEL = 2

HTML_HELP_WSHOP_KEY = r"Software\Microsoft\HTML Help Workshop"

MIT_LICENSE = """Copyright (c) 2001-2016 Andre Burgaud (http://www.burgaud.com)

Permission  is hereby granted, free of charge, to any person obtaining
a copy  of  this  software  and  associated documentation  files  (the
"Software"), to  deal  in  the Software without restriction, including
without limitation the  rights to use,  copy, modify,  merge, publish,
distribute,  sublicense, and/or  sell copies of the Software,  and  to
permit persons to whom the Software  is furnished to do so, subject to
the following conditions:

The  above  copyright  notice  and  this permission  notice  shall  be
included in all copies or substantial portions of the Software.

THE SOFTWARE  IS  PROVIDED  "AS  IS",  WITHOUT WARRANTY  OF ANY  KIND,
EXPRESS OR IMPLIED, INCLUDING  BUT  NOT LIMITED TO  THE  WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT  HOLDERS BE LIABLE FOR  ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER  IN AN  ACTION OF CONTRACT,
TORT  OR OTHERWISE, ARISING  FROM, OUT  OF OR  IN CONNECTION WITH  THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

USAGE = r"""Usage:

  jd2chm [ -h | -c | -l | [-p path] [-o output] [-t title] [-v] ]

  -h: Displays usage.
  -c: Checks if the HHC compiler is installed.
  -l: Displays license.
  -v: Verbose (displays debug information)
  -p path:   'path' is the path of a  directory containing a Javadoc
             documentation (default: current directory).
  -o output: base name of the CHM output file
             Ex: -o 'product' will result in a CHM file named 'product.chm'.
  -t title:  Assign 'title' as the title of the project.

Notes:
- The user is prompted if the output and document title are not
  provided at the command line. The default values are extracted from
  the Javadoc index.html (see examples below).
- The Javadoc path is the path containing the file index.html.

Examples:
jd2chm.py -p C:\beanshell\javadoc
  The user is prompted to possibly modify the default values for the
  project name and document title.

jd2chm.py -p C:\beanshell\javadoc -o bsh20b4 -t "Beanshell 2.0b4" -v

jd2chm.py -p C:\j2se\docs\api -o j2se142_02 -t "Java(TM) 2 SDK 1.4.2"

jd2chm.py -o jython21 -t "Jython 2.1"
  The Javadoc is assumed to be in the current directory.

jd2chm.py -o SWT30M7 -t "Standard Widget toolkit 3.0M7"
  The Javadoc is assumed to be in the current directory."""

NOT_JAVADOC_DIR_MESSAGE = """\
The directory '{}' is not a Javadoc directory (%s not found).
Run jd2chm from a directory that contains a generated Javadoc documentation,
or use the parameter -p to provide the path of a Javadoc directory.

To display additional help, run jd2chm -h"""

NOT_DIR_MESSAGE = """\
Directory '{}' not found.
Run jd2chm from a directory that contains a generated Javadoc documentation,
or use the parameter -p to provide the path of a Javadoc directory.

To display additional help, run jd2chm -h"""

CSS_FILE_NAME = "stylesheet.css"
JDK_BOOK_FILE = "overview-frame.html"
OVERVIEW_TREE = "overview-tree.html"
PACKAGE_TREE_HTML = "package-tree.html"
PACKAGE_SUMMARY = "package-summary.html"
PACKAGE_USE = "package-use.html"
INDEX_HTML = "index.html"
INDEX_DIR = "index-files"     # Either a directory with splitted index files
INDEX_ALL = "index-all.html"  # or one unique index file
ABOUT_FILE = "about.html"     # About file generated by jd2chm
PACKAGE_LIST = "package-list" # Raw list of the packages

DEFAULT_TERM_WIDTH = 80
DEFAULT_TERM_HEIGHT = 40
TERM_MARGIN = 10

MSG_THANKS = """
Thank you for using jd2chm!
Visit http://www.burgaud.com/jd2chm to check if new versions are available
Source code is available on GitHub: https://github.com/andreburgaud/jd2chm
"""

MSG_WELCOME = """
jd2chm version %s
Copyright (c) 2001-2016 Andre Burgaud
http://www.burgaud.com/
"""

FORMAT_PROJECT = """[OPTIONS]
Compatibility=1.1 or later
Binary TOC=Yes
Binary Index=Yes
Compiled file=%s.chm
Contents file=%s.hhc
Index file=%s.hhk
Default Window=main
Default topic=%s
Error log file=hhc.log
Display compile progress=Yes
Display compile notes=No
Full-text search=Yes
Language=0x409 English (United States)
Title=%s

[WINDOWS]
main="%s","%s.hhc","%s.hhk","%s","%s","about.html","Jd2chm",,,0x23520,,0x44387e,,,,,,,,0

[FILES]
"""

FORMAT_TOC_HEADER = """<html>
<head>
  <!-- HTML Help Contents File -->
  <!-- Generated: %s with jd2chm.py -->
  <!-- http://www.burgaud.com -->
</head>
<body>
<object type="text/site properties">
  <param name="FrameName" value="main">
</object>
"""

FORMAT_ALLCLASSES_CONTENT_ITEM = """<li><object type="text/sitemap">
  <param name="Name" value="All Classes">
  <param name="Local" value="allclasses-noframe.html">
</object>
<ul>
"""

FORMAT_INDEX_HEADER = """<html>
<head>
  <!-- HTML Help Index File -->
  <!-- Generated: %s with jd2chm.py -->
  <!-- http://www.burgaud.com -->
</head>
<body>
"""

# Represents the index keyword. Sub-entries (next format)
# pointing to the proper class or interface
FORMAT_INDEX_KEYWORD = """<li><object type="text/sitemap">
<param name="Name" value="%s">
<param name="See Also" value="%s">
</object>
"""

FORMAT_INDEX_ITEM = """<li><object type="text/sitemap">
  <param name="Local" value="%s">
  <param name="Name" value="%s">
</object>
"""

FORMAT_CONTENT_BOOK_ITEM = """<li><object type="text/sitemap">
  <param name="Name" value="%s">
  <param name="Local" value="%s">
</object>
"""

FORMAT_CONTENT_CLASS_ITEM = """<li><object type="text/sitemap">
  <param name="Local" value="%s">
  <param name="Name" value="%s">
</object>
"""

FORMAT_CONTENT_METHOD_ITEM = """<li><object type="text/sitemap">
  <param name="Name" value="%s">
  <param name="Local" value="%s">
</object>
"""

FORMAT_CSS = """/* The original CSS file has been saved under stylesheet.css.bak */
body { background-color: #FFFFFF; font-size: 10pt; font-family: Helvetica, Arial, sans-serif }
td { background-color: #FFFFFF; font-size: 10pt; font-family: Helvetica, Arial, sans-serif }
/* Table colors */
.TableHeadingColor     { background: #CCCCFF } /* Dark mauve */
.TableSubHeadingColor  { background: #EEEEFF } /* Light mauve */
.TableRowColor         { background: #FFFFFF } /* White */
/* Font used in left-hand frame lists */
.FrameTitleFont   { font-size: 10pt; font-family: Helvetica, Arial, sans-serif}
.FrameHeadingFont { font-size: 10pt; font-family: Helvetica, Arial, sans-serif }
.FrameItemFont    { font-size: 10pt; font-family: Helvetica, Arial, sans-serif }
/* Links */
a:link { color: #0000FF; text-decoration: underligne;}
a:visited { color: #A9A9A9 ; text-decoration: underligne;}
a:active { color: #FF0000; text-decoration: underligne;}
a:hover { color: #FF0000; text-decoration: underligne;}
/* Navigation bar fonts and colors */
.NavBarCell1    { background-color:#EEEEFF;} /* Light mauve */
.NavBarCell1Rev { background-color:#00008B;} /* Dark Blue */
.NavBarFont1    { font-family: Helvetica, Arial, sans-serif; color:#000000;}
.NavBarFont1Rev { font-family: Helvetica, Arial, sans-serif; color:#FFFFFF;}
.NavBarCell2    { font-family: Helvetica, Arial, sans-serif; background-color:#FFFFFF;}
.NavBarCell3    { font-family: Helvetica, Arial, sans-serif; background-color:#FFFFFF;}
"""

ABOUT_TEXT = """
<html><head><title>About Jd2chm</title></head>
<body><center>
<table width="50%" border="2" cellspacing="0" cellpadding="0">
<tr><td height="50%" bgcolor="#C0C0C0" bordercolorlight="#000000" bordercolordark="#FFFFFF">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr><td bgcolor="#000080"><font face="Microsoft Sans Serif" size="2" color="#FFFFFF">
<b>&nbsp;&nbsp; About Jd2chm...</b>
</font></tr></tr>
<tr><td><center><br/>
<font face="Microsoft Sans Serif" size="2">
This HTML Help file<br/>was generated with Jd2chm version 1.0.0<br/>
Copyright &copy; 2000-20016 <a href="mailto:andre@burgaud.com">Andre Burgaud</a><br/>
<a href="http://www.burgaud.com/">http://www.burgaud.com</a></font><br/>&nbsp;
</td></tr>
</table>
</td></tr></table></center></body></html>
"""

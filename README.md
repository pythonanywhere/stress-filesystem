Filesystem stress-testing tools
===============================

We're building a few tools to test various new filesystems + fileservers
against.  We thought we'd put them out there, partially in case anyone else
finds them useful, but mostly in the hope that someone will come along and
say "You idiots! You're doing it all wrong! And besides, the perfect tool
for this already exists, it has done since the 70s, here's a link".

Or something.  Contributions and suggestions welcome.

The PythonAnywhere gang

http://www.pythonanywhere.com

Current state
=============

There is one tool called "multiprocess-reader-writer", which spaws lots of
processes that read and write to a given directory.  Some parameters in the
command-line, some as constants in the file.

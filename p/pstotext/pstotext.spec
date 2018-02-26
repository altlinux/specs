Name: pstotext
Version: 1.9
Release: alt2

Summary: PostScript to text converter
License: Digital's paranoid but open-source license
Group: Text tools

Url: http://pages.cs.wisc.edu/~ghost/doc/pstotext.htm
Source: ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/contrib/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

Requires: ghostscript

Summary(pl): Konwerter PostScriptu do czystego tekstu

%description
This utility reads in postscript files and outputs an ASCII rendering.
While the rendering is not always accurate, it is often sufficient.

%prep
%setup

%build
%make

%install
install -pDm755 pstotext %buildroot%_bindir/%name
install -pDm644 pstotext.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.9-alt2
- updated Url:
- spec cleanup

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 1.9-alt1
- built for ALT Linux (based on spec by Eugene Chernov
  which was in its turn adapted from PLD)


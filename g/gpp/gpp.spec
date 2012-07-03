Name: gpp
Version: 2.24
Release: alt1

Summary: General-purpose preprocessor with customizable syntax
License: GPL
Group: Text tools
URL: http://www.nothingisreal.com/gpp/

Requires: gcc

Source: gpp-%version.tar.bz2

%description
GPP is a general-purpose preprocessor with customizable syntax, suitable
for a wide range of preprocessing tasks. Its independence from any one
programming language makes it much more versatile than the C
preprocessor (cpp), while its syntax is lighter and more flexible than
that of GNU m4. There are built-in macros for use with C/C++, LaTeX,
HTML, XHTML, and Prolog files.

GPP is Free Software. It is distributed under the terms of the GNU
Lesser General Public Licence.

%prep
%setup

%build
%configure
%make

%install
%makeinstall

%files
%doc README THANKS NEWS AUTHORS BUGS COPYING INSTALL ChangeLog TODO doc
%_mandir/man1/*
%_bindir/*

%changelog
* Mon Sep 20 2004 Mikhail Yakshin <greycat@altlinux.ru> 2.24-alt1
- 2.24

* Fri Sep 03 2004 Mikhail Yakshin <greycat@altlinux.ru> 2.23-alt1
- Initial build for ALT Linux


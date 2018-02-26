Name: t1utils
Version: 1.37
Release: alt1

Summary: Programs for manipulating PostScript Type 1 fonts
License: freely modifiable and distributable
Group: Publishing

Url: http://www.lcdf.org/type
Source: %url/%name-%version.tar.gz

%description
The t1utils package is a set of programs for manipulating PostScript Type 1
fonts. It contains programs to change between binary PFB format (for storage),
ASCII PFA format (for printing), a human-readable and -editable ASCII format,
and Macintosh resource forks.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Jul 01 2011 Victor Forsiuk <force@altlinux.org> 1.37-alt1
- 1.37

* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 1.36-alt1
- 1.36

* Tue Dec 22 2009 Victor Forsyuk <force@altlinux.org> 1.35-alt1
- 1.35

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 1.34-alt1
- 1.34
- added (hopefully) Packager:
- fixed FTBFS against recent glibc with gentoo patch

* Wed Jul 20 2005 Victor Forsyuk <force@altlinux.ru> 1.32-alt1
- 1.32

* Wed May 07 2003 Rider <rider@altlinux.ru> 1.27-alt1
- new version

* Thu Oct 17 2002 Rider <rider@altlinux.ru> 1.26-alt2
- gcc 3.2 rebuild

* Sat Aug 24 2002 Rider <rider@altlinux.ru> 1.26-alt1
- 1.26

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.25-alt1
- 1.25

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 1.24-alt1
- 1.24

* Sun Feb 18 2001 AEN <aen@logic.ru>
- group name fixed
- 1.21

* Tue Aug 16 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- updated to version 1.13.

* Tue Aug 03 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- mandrake adaptions

* Sat May 29 1999 Eddie Kohler <eddietwo@lcs.mit.edu>
- initial release.

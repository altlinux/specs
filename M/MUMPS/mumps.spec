Name: MUMPS
Version: 1.71
Release: alt1
Summary: Massachusetts General Hospital Utility Multi-Programming System
Group: Development/Other
License: BSD

Source: mumps-%version-src.tar.gz
Source1: http://mumps.sourceforge.net/docs.html

%description
MUMPS (Massachusetts General Hospital Utility Multi-Programming System)
or alternatively M, is a general-purpose computer programming language
that provides ACID (Atomic, Consistent, Isolated, and Durable)
transaction processing. Its most unique and differentiating feature is
its "built-in" database, enabling high-level access to disk storage
using simple symbolic program variables and subscripted arrays, similar
to the variables used by most languages to access main memory.

%prep
%setup -n mumps
cp %SOURCE1 .
%make_build

%install
install -D mumps %buildroot%_bindir/mumps
install -D utils %buildroot%_datadir/mumps/utils

%files
%doc *.html README
%_bindir/*
%_datadir/mumps

%changelog
* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 1.71-alt1
- Autobuild version bump to 1.71

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 1.70-alt1
- Autobuild version bump to 1.70

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.66-alt1
- Autobuild version bump to 1.66

* Fri Aug 07 2015 Fr. Br. George <george@altlinux.ru> 1.64-alt1
- Initial build for ALT


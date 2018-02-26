Name: gambit-signal
Version: 1.0
Release: alt6
Summary: UNIX signal handling library for Gambit-C Scheme programming system
License: GPL
Group: Development/Scheme

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildPreReq: gambit glibc-devel

Source: %name-%version.tar.gz

%description
UNIX signal handling library for Gambit-C Scheme programming system

%package devel
Summary: UNIX signal handling library link file for Gambit-C Scheme programming system
Group: Development/Scheme
Requires: %name = %version-%release
BuildArch: noarch

%description devel
UNIX signal handling library for Gambit-C Scheme programming system

This package contains the library link file

%prep
%setup -q

%build
gsc -:daq- -link -flat -o libgambc-signal.c signal.scm
gsc -:daq- -obj -cc-options "-D___LIBRARY -D___SHARED -D___PRIMAL" signal.c libgambc-signal.c
gcc -shared signal.o libgambc-signal.o -lgambc -o libgambc-signal.so

%install
install -Dp -m0644 libgambc-signal.so %buildroot%{_libdir}/gambit/libgambc-signal.so
install -Dp -m0644 libgambc-signal.c %buildroot%{_includedir}/gambit/libgambc-signal.c

%files
%{_libdir}/gambit/libgambc-signal.so

%files devel
%{_includedir}/gambit/libgambc-signal.c

%changelog
* Thu May 03 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Rebuild with a new version of Gambit.

* Fri Feb 24 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Rebuild with a new version of Gambit.

* Tue Oct 25 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Rebuild with a new version of Gambit.

* Fri Jun 10 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Rebuild with a new version of Gambit.

* Mon Feb 01 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Rebuild with a new version of Gambit.

* Wed Sep 30 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux.

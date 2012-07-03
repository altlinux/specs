Name: gambit-sqlite3
Version: 1.2
Release: alt2
Summary: SQLite3 database library for Gambit-C Scheme programming system
License: GPL
Group: Development/Scheme
URL: http://okmij.org/ftp/Scheme/#databases

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildPreReq: gambit sqlite3 libsqlite3-devel

Source: %name-%version.tar.gz

%description
SQLite3 database library for Gambit-C Scheme programming system

%package devel
Summary: SQLite3 database library link file for Gambit-C Scheme programming system
Group: Development/Scheme
Requires: %name = %version-%release
BuildArch: noarch

%description devel
SQLite3 database library for Gambit-C Scheme programming system

This package contains the library link file

%prep
%setup -q

%build
gsc -:daq- -link -flat -o libgambc-sqlite3.c sqlite3.scm
gsc -:daq- -obj -cc-options "-D___LIBRARY -D___SHARED -D___PRIMAL" sqlite3.c libgambc-sqlite3.c
gcc -shared sqlite3.o libgambc-sqlite3.o -lgambc -lsqlite3 -o libgambc-sqlite3.so

%install
install -Dp -m0644 libgambc-sqlite3.so %buildroot%{_libdir}/gambit/libgambc-sqlite3.so
install -Dp -m0644 libgambc-sqlite3.c %buildroot%{_includedir}/gambit/libgambc-sqlite3.c

%check
echo "Run sqlite3-test.scm to verify the library"
gsc -:daq- -link %buildroot%{_includedir}/gambit/libgambc-sqlite3.c sqlite3-test.scm
gsc -:daq- -obj sqlite3-test.c sqlite3-test_.c
gcc sqlite3-test.o sqlite3-test_.o -lgambc -L%buildroot%{_libdir}/gambit -lgambc-sqlite3 -o sqlite3-test
export LD_LIBRARY_PATH=%buildroot%{_libdir}/gambit
./sqlite3-test -:daq-

%files
%doc README COPYRIGHT
%{_libdir}/gambit/libgambc-sqlite3.so

%files devel
%{_includedir}/gambit/libgambc-sqlite3.c

%changelog
* Fri May 11 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt2
- Rebuild with a new version of Gambit.

* Thu Mar 15 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt1
- Fix more: always finalize the query on fetch exit.

* Tue Mar 13 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Fix: finalize the query on unfinished fetch.

* Fri Feb 24 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Rebuild with a new version of Gambit.

* Tue Oct 25 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Rebuild with a new version of Gambit.

* Fri Jun 10 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Rebuild with a new version of Gambit.

* Thu Dec 24 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Add sqlite3-specific exception handling.

* Mon Sep 21 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Correct C compiler flags.

* Thu Sep 10 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux.

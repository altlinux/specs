Name: gambit-sqlite3
Version: 1.3.1
Release: alt1
Summary: SQLite3 database library for Gambit-C Scheme programming system
License: GPLv3+
Group: Development/Scheme
URL: http://okmij.org/ftp/Scheme/#databases

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildRequires: gambit-devel sqlite3 libsqlite3-devel

Source: %name-%version.tar

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
%make_build

%install
%makeinstall

%check
%make check

%files
%doc README COPYRIGHT
%{_libdir}/gambit/*.so

%files devel
%{_includedir}/gambit/*.c

%changelog
* Mon Feb 13 2023 Paul Wolneykien <manowar@altlinux.org> 1.3.1-alt1
- Fix compilation with new Gambit: Replace [] with ().

* Mon Feb 11 2019 Paul Wolneykien <manowar@altlinux.org> 1.3-alt3
- Rebuild with a new version of Gambit

* Wed Jan 23 2019 Paul Wolneykien <manowar@altlinux.org> 1.3-alt2
- Rebuild with a new version of Gambit

* Tue Nov 27 2018 Paul Wolneykien <manowar@altlinux.org> 1.3-alt1
- Rebuild with a new version of Gambit.
- Adapt to the new version of Gambit library: gambc -> gambit.

* Mon Apr 03 2017 Paul Wolneykien <manowar@altlinux.org> 1.2-alt11
- Rebuild with a new version of Gambit

* Tue Sep 23 2014 Paul Wolneykien <manowar@altlinux.org> 1.2-alt10
- Rebuild with a new version of Gambit

* Mon Mar 10 2014 Paul Wolneykien <manowar@altlinux.org> 1.2-alt9
- Rebuild with a new version of Gambit

* Sun Jan 19 2014 Paul Wolneykien <manowar@altlinux.org> 1.2-alt8
- Rebuild with a new version of Gambit

* Wed May 22 2013 Paul Wolneykien <manowar@altlinux.org> 1.2-alt7
- Add procs to access fields in a sqlite3 exception.

* Mon May 20 2013 Paul Wolneykien <manowar@altlinux.org> 1.2-alt6
- Bundle sources in plain tar.
- Take care of the return code of the sqlite3-test.scm.
- Use the universal Makefile.

* Tue May 14 2013 Paul Wolneykien <manowar@altlinux.org> 1.2-alt5
- Rebuild with a new version of Gambit

* Mon Apr 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt4
- Rebuild with a new version of Gambit.
- Revert the query-finalization wrappers.

* Fri Jan 04 2013 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt3
- Rebuild with Gambit v4.6.6.

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

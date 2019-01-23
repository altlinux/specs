Name: gambit-signal
Version: 1.2
Release: alt2
Summary: UNIX signal handling library for Gambit-C Scheme programming system
License: GPLv3+
Group: Development/Scheme

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildRequires: gambit-devel glibc-devel

Source: %name-%version.tar

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
%make_build

%install
%makeinstall

%check
%make check

%files
%{_libdir}/gambit/*.so

%files devel
%{_includedir}/gambit/*.c

%changelog
* Wed Jan 23 2019 Paul Wolneykien <manowar@altlinux.org> 1.2-alt2
- Rebuild with a new version of Gambit

* Tue Nov 27 2018 Paul Wolneykien <manowar@altlinux.org> 1.2-alt1
- Rebuild with a new version of Gambit
- Adapt to the new library name: gambc -> gambit.
- Fix: Use code 3 (user interrupt) with ##interrupt-vector-set!.

* Mon Apr 03 2017 Paul Wolneykien <manowar@altlinux.org> 1.1-alt5
- Rebuild with a new version of Gambit

* Tue Sep 23 2014 Paul Wolneykien <manowar@altlinux.org> 1.1-alt4
- Rebuild with a new version of Gambit

* Mon Mar 10 2014 Paul Wolneykien <manowar@altlinux.org> 1.1-alt3
- Rebuild with a new version of Gambit

* Sun Jan 19 2014 Paul Wolneykien <manowar@altlinux.org> 1.1-alt2
- Rebuild with a new version of Gambit

* Wed Jun 26 2013 Paul Wolneykien <manowar@altlinux.org> 1.1-alt1
- Use Gambit's interrupts to pass on the received signals.
- Raise the exception interrupting the recipient thread.
- Exit with status of 1 when the test fails.

* Wed May 22 2013 Paul Wolneykien <manowar@altlinux.org> 1.0-alt11
- Add the proc to access the signal number field in a signal
  exception.

* Mon May 20 2013 Paul Wolneykien <manowar@altlinux.org> 1.0-alt10
- Bundle sources in plain tar.
- Add the test program.
- Add getpid and getppid wrappers.
- Add the Makefile and use it.
- Refactor the sources, update the licensing information.

* Tue May 14 2013 Paul Wolneykien <manowar@altlinux.org> 1.0-alt9
- Rebuild with a new version of Gambit

* Mon Apr 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt8
- Rebuild with a new version of Gambit.

* Fri Jan 04 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt7
- Rebuild with Gambit v4.6.6.

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

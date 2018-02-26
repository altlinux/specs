Name: rlog14
Summary: Runtime Logging for C++
Version: 1.4
Release: alt3
License: LGPL
Group: Development/C++
Url: http://pobox.com/~vgough/rlog

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: rlog.tar

# Automatically added by buildreq on Wed Oct 18 2006
BuildRequires: doxygen gcc-c++ /usr/bin/latex

Patch: rlog.gcc43.patch

%description
RLog provides a flexible message logging facility for C++ programs and
libraries.  It is meant to be fast enough to leave in production code.

%package -n librlog14
Group: %group
Summary: %summary

Conflicts: librlog < %version-%release
Conflicts: librlog > %version-%release

%description -n librlog14
RLog provides a flexible message logging facility for C++ programs and
libraries.  It is meant to be fast enough to leave in production code.

%package -n librlog14-devel
Group: %group
Summary: %summary
Requires: librlog14 = %version-%release

Conflicts: librlog13-devel

Provides: librlog-devel = %version-%release
Conflicts: librlog-devel < %version-%release
Conflicts: librlog-devel > %version-%release

Conflicts: librlog < %version-%release
Conflicts: librlog > %version-%release
Obsoletes: librlog < %version-%release

%description -n librlog14-devel
RLog provides a flexible message logging facility for C++ programs and
libraries.  It is meant to be fast enough to leave in production code.

%package -n librlog14-devel-doc
Group: %group
Summary: %summary

BuildArch: noarch

Conflicts: librlog13-devel-doc

Provides: librlog-devel-doc = %version-%release
Conflicts: librlog-devel-doc < %version-%release
Conflicts: librlog-devel-doc > %version-%release

Conflicts: librlog < %version-%release
Conflicts: librlog > %version-%release

%description -n librlog14-devel-doc
RLog provides a flexible message logging facility for C++ programs and
libraries.  It is meant to be fast enough to leave in production code.

%prep
%setup -q -c %name
%patch -p2

%build
%configure
%make_build

%install
%make_build DESTDIR=%buildroot install

%files -n librlog14-devel-doc
%_docdir/rlog

%files -n librlog14-devel
%_libdir/librlog.so
%_pkgconfigdir/*
%_includedir/rlog

%files -n librlog14
%_libdir/librlog.so.*

%changelog
* Mon Sep 27 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt3
- fix latex requires

* Thu Dec 18 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt2
- add conflicts with librlog13-devel*

* Thu Nov 20 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt1
- update to 1.4
- split to subpackages librlog13/librlog13-devel/librlog13-devel-doc

* Wed Oct 29 2008 Denis Smirnov <mithraen@altlinux.ru> 1.3.7-alt3
- fix build with gcc 4.3

* Wed Oct 18 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.7-alt2
- try to fix x86_64 build

* Tue Oct 17 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.7-alt1
- version update
- rebuild with gcc 4.1 (instead of 3.4)

* Fri Feb 11 2005 Denis Smirnov <mithraen@altlinux.ru> 1.3.6-alt1
- version update

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.4-alt1.1
- Rebuilt with libstdc++.so.6.

* Thu Oct 28 2004 Denis Smirnov <mithraen@altlinux.ru> 1.3.4-alt1
- sisyphus build

* Mon May 31 2004 Valient Gough <vgough@pobox.com>
- Release v1.3.4
- Portibility changes to allow rlog to build with older C++ compilers and on
  non-x86 computers.
- Add extra ERROR_FMT() macro which allows format string to be passed on Error
  construction.
- Add valgrind support to allow valgrind trace from any assert when running
  under valgrind.
- Update admin dir.

* Sat Mar 13 2004 Valient Gough <vgough@pobox.com>
- Release v1.3.1
- added pkg-config file librlog.pc
- changed license to LGPL
- added rAssertSilent macro
- fixes for special case checks of printf attribute

* Sat Feb 8 2004 Valient Gough <vgough@pobox.com>
- Release v1.3


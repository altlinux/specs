%define _libexecdir %_prefix/libexec
%define modname dbus-python

%def_enable doc
%def_enable check
%def_disable installed_tests
#%%add_findreq_skiplist %_libexecdir/installed-tests/%modname/test/*.py

Name: python3-module-dbus
Version: 1.3.2
Release: alt1.1

Summary: Python bindings for D-BUS library
License: MIT
Group: Development/Python3
Url: https://www.freedesktop.org/wiki/Software/DBusBindings

Source: https://dbus.freedesktop.org/releases/dbus-python/dbus-python-%version.tar.gz

%define dbus_ver 1.8
%define glib_ver 2.40
%define python3_ver 3.7

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson libdbus-devel >= %dbus_ver libgio-devel >= %glib_ver
BuildRequires: python3-devel python3-module-pygobject3
%{?_enable_check:BuildRequires: /proc dbus-tools dbus-tools-gui glibc-i18ndata python3-module-tappy}
%{?_enable_doc:BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme}

%description
D-Bus python bindings for use with python programs.

%package gobject
Summary: Python bindings for D-BUS library
Group: Development/Python
Requires: %name = %EVR

%description gobject
D-Bus bindings for use with python programs
(gobject introspection bindings).

%package -n %modname-devel
Summary: Python bindings for D-BUS library (devel package)
Group: Development/Python3
Provides: python3-module-dbus-devel = %EVR
Provides: python-module-dbus-devel  = %EVR

%description -n %modname-devel
D-Bus python bindings for use with python programs.
Development package.

%package devel-doc
Summary: Development documentation for %modname
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
Development documentation for %modname.

%package tests
Summary: Tests for the %name package
Group: Development/Python3
Requires: %name = %EVR
Requires: dbus-tools

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed python-dbus package.

%prep
%setup -n %modname-%version

%build
%meson \
    %{?_enable_installed_tests:-Dinstalled-tests=true} \
    %{?_enable_doc:-Ddoc=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test -t 2

%files
%python3_sitelibdir/*.so
%python3_sitelibdir/dbus/
%doc AUTHORS COPYING NEWS

%exclude %python3_sitelibdir/dbus/gi_service.py
%exclude %python3_sitelibdir/dbus/__pycache__/gi_service.*.pyc

%files gobject
%python3_sitelibdir/dbus/gi_service.py
%python3_sitelibdir/dbus/__pycache__/gi_service.*.pyc

%files -n %modname-devel
%_includedir/dbus-1.0/dbus/%modname.h
%_pkgconfigdir/%modname.pc
%doc doc/*.txt

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%modname/
%_datadir/installed-tests/%modname/
%endif

%if_enabled doc
%files devel-doc
%_docdir/%modname/
%endif

%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1.1
- increased tests timeout for some slower machines, e.g. most modern
  riscv64 boards (voropaevdmtr@)

* Wed Sep 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2 (ported to Meson build system)

* Mon Jul 26 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.18-alt2
- python3-only build
- new dbus-python-devel subpackage provides both python{,3}-module-dbus-devel

* Wed Jul 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.18-alt1
- 1.2.18

* Tue Jul 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.16-alt2
- made -devel subpackage Python-version-independent (ALT #40475)

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.16-alt1
- 1.2.16
- fixed License tag

* Wed Jan 29 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.14-alt3
- Fix build with python3.8.

* Thu Nov 28 2019 Anton Midyukov <antohami@altlinux.org> 1.2.14-alt2
- Allocated a separate subpackages with pygobject bindings (Closes: 34351)

* Wed Nov 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.14-alt1
- 1.2.14

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.12-alt1
- 1.2.12

* Wed Sep 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.10-alt1
- 1.2.10
- updated {build,}reqs
- made python2 build optional

* Sat May 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.8-alt1
- 1.2.8
- new devel-doc subpackage

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4
- removed obsolete patches

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Feb 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 07 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0
- use automake_1.11

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt4
- rebuilt to remove separate python3-module-dbus from Sisyphus

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt3
- new python3-module-dbus subpackage
- %%check temporarily disabled

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2
- fix for our usc4-impaired python 2.7 build as patch2
  thanks to vsu@ and ldv@. (closes: #28202)

* Sat Dec 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- after 1.1.1 snapshot (c57c4d28)
- %%check section

* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.83.1-alt2.1
- Rebuild with Python-2.7

* Sat Mar 13 2010 Sergey Vlasov <vsu@altlinux.ru> 0.83.1-alt2
- Make the whole package arch-specific again to fix problems with the
  dbus.mainloop.qt module in python-module-PyQt4 on x86_64 (ALT#23134);
  remove and obsolete the python-module-dbus-data subpackage.

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 0.83.1-alt1
- 0.83.1

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.83.0-alt3
- arch independent python scripts moved to separate subpackage

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.83.0-alt2.1
- Rebuilt with python 2.6

* Tue Dec 16 2008 Dmitry V. Levin <ldv@altlinux.org> 0.83.0-alt2
- Reintroduced %%setup_python_module.

* Fri Dec 05 2008 Yuri N. Sedunov <aris@altlinux.org> 0.83.0-alt1
- 0.83.0
- removed broken %%setup_python_module macros

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.82.4-alt2.1
- Rebuilt with python-2.5.

* Mon Dec 31 2007 Ivan Fedorov <ns@altlinux.org> 0.82.4-alt2
- fix python policy compatibility

* Mon Dec 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.82.4-alt1
- 0.82.4

* Mon Aug 27 2007 Igor Zubkov <icesik@altlinux.org> 0.82.2-alt1
- 0.81.1 -> 0.82.2
- add devel subpackage and move in them devel files (closes #11650)

* Mon Jul 09 2007 Igor Zubkov <icesik@altlinux.org> 0.81.1-alt2
- add Provides dbus-python (closes #12273)

* Mon Jun 11 2007 Igor Zubkov <icesik@altlinux.org> 0.81.1-alt1
- 0.80.1 -> 0.81.1

* Thu Apr 26 2007 Igor Zubkov <icesik@altlinux.org> 0.80.1-alt1
- 0.71 -> 0.80.1
- buildreq

* Sun Dec 24 2006 Igor Zubkov <icesik@altlinux.org> 0.71-alt2
- add libdbus-devel >= 0.94 to buildprereq

* Sun Dec 03 2006 Igor Zubkov <icesik@altlinux.org> 0.71-alt1
- add packager tag
- bzip2 ChangeLog
- buildreq

* Tue Nov 14 2006 Alexey Shabalin <shaba@altlinux.ru> 0.71-alt0.1
- initial build

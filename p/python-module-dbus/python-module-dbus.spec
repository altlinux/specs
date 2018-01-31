%define _libexecdir %_prefix/libexec
%define _name dbus-python
%def_enable check
# required dbus_py_test.so for both pythons
%def_disable installed_tests
%add_findreq_skiplist %_libexecdir/installed-tests/%_name/test/*.py

Name: python-module-dbus
Version: 1.2.6
Release: alt1

Summary: Python bindings for D-BUS library
License: AFL/GPL
Group: Development/Python
Url: http://www.freedesktop.org/wiki/Software/DBusBindings

##Source: dbus-python-%version.tar
Source: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%version.tar.gz

%setup_python_module dbus

Requires: dbus
Provides: %_name = %version-%release
Provides: %name-data = %version-%release
Obsoletes: %name-data < %version-%release

BuildRequires: autoconf-archive libdbus-devel >= 1.8 libgio-devel >= 2.40
BuildRequires: python-devel >= 2.7 python3-devel >= 3.4 python-modules-unittest
BuildRequires: python-module-pygobject3 python-module-tappy
# for python3
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3
%{?_enable_check:BuildRequires: /proc dbus-tools dbus-tools-gui glibc-i18ndata python3-module-tappy}

%description
D-Bus python bindings for use with python programs.

%package -n python3-module-dbus
Summary: Python3 bindings for D-BUS library
License: AFL/GPL
Group: Development/Python3
Requires: dbus

%description -n python3-module-dbus
D-Bus python bindings for use with python programs.

%package devel
Summary: Python bindings for D-BUS library (devel package)
Group: Development/Python
Requires: %name = %version-%release
%py_package_provides %modulename-devel = %version-%release
Provides: python3-module-dbus-devel = %version-%release

%description devel
D-Bus python bindings for use with python programs.
Development package.

%package tests
Summary: Tests for the %name package
Group: Development/Python
Requires: %name = %version-%release
Requires: dbus-tools

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed python-dbus package.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%define options %{?_enable_installed_tests:--enable-installed-tests}

# Install python code into arch-specific dir for PyQt4 (ALT#23134)
export am_cv_python_pythondir=%python_sitelibdir
export am_cv_python_pyexecdir=%python_sitelibdir

%autoreconf
%configure %options \
	PYTHON=%__python \
	PYTHON_LIBS="$(python-config --libs)"
%make_build

pushd py3build
export am_cv_python_pythondir=%python3_sitelibdir
export am_cv_python_pyexecdir=%python3_sitelibdir
%autoreconf
%configure %options \
	PYTHON=/usr/bin/python3 \
	PYTHON_LIBS="$(python3-config --libs)"
%make_build
popd

%install
for d in {.,py3build}; do
pushd $d
%makeinstall_std
popd
done

%if_enabled check
%check
%make check
%make check -C py3build
%endif

%files
%python_sitelibdir/*.so
%python_sitelibdir/dbus/
%doc AUTHORS COPYING NEWS

%files devel
%doc doc/*.txt
%_includedir/dbus-1.0/dbus/dbus-python.h
%_pkgconfigdir/dbus-python.pc

%exclude %python_sitelibdir/*.la

%files -n python3-module-dbus
%python3_sitelibdir/*.so
%python3_sitelibdir/dbus/

%exclude %python3_sitelibdir/*.la

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%exclude %_libexecdir/installed-tests/%_name/test/__pycache__
%_datadir/installed-tests/%_name/
%endif

%exclude %_docdir/%_name

%changelog
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

Name: python3-module-dbus
Version: 1.0.0
Release: alt2

Summary: Python 3 bindings for D-BUS library
License: AFL/GPL
Group: Development/Python3
Url: http://www.freedesktop.org/wiki/Software/DBusBindings

Source: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%version.tar.gz
Patch: dbus-python-1.0.0-alt-link.patch

Requires: dbus

BuildRequires(pre): rpm-build-python3
BuildRequires: libdbus-glib-devel python3-devel

%description
D-Bus python bindings for use with python programs.

%package devel
Summary: Python 3 bindings for D-BUS library (devel package)
Group: Development/Python3
Requires: %name = %version-%release
%py3_provides dbus-devel

%description devel
D-Bus python bindings for use with python programs.
Development package.

%prep
%setup -q -n dbus-python-%version
%patch -p1

%build
# Install python code into arch-specific dir for PyQt4 (ALT#23134)
export am_cv_python_pythondir=%python3_sitelibdir
export PYTHON=python3
export PYTHON_LIBS="$(python3-config --libs)"

%autoreconf
%configure
sed -i \
	's|^\(_dbus_bindings_la_LIBADD\).*|\1 =|' \
	_dbus_bindings/Makefile
sed -i \
	's|^\(_dbus_glib_bindings_la_LIBADD\).*|\1 =|' \
	_dbus_glib_bindings/Makefile
%make_build

%install
%makeinstall_std

%files
%python3_sitelibdir/*.so
%python3_sitelibdir/dbus/
%doc AUTHORS COPYING NEWS

%files devel
%doc doc/*.txt TODO
%_includedir/dbus-1.0/dbus/dbus-python.h
%_pkgconfigdir/dbus-python.pc

%exclude %python3_sitelibdir/*.la
%exclude %_docdir/dbus-python

%changelog
* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Built for Python 3

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

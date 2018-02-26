%define oname Ice
%define major 3.3
Name: python-module-Ice
Version: %major.1
Release: alt4

Summary: The Ice runtime for Python applications

License: GPL
Group: System/Libraries
Url: http://www.zeroc.com/

Source: http://www.zeroc.com/download/Ice/%major/Ice-%version.tar.bz2
Source1: http://www.zeroc.com/download/Ice/%major/Ice-rpmbuild-%version.tar.bz2
Patch0: Ice-3.3.1-alt-gcc4.6.patch

%setup_python_module Ice

Requires: libice = %version

Provides: python-module-ice
Obsoletes: python-module-ice

# Automatically added by buildreq on Fri Aug 03 2007
BuildRequires: gcc-c++ ice libice-devel python-devel

BuildRequires: ice = %version

%description
Ice is a modern alternative to object middleware such as CORBA or
COM/DCOM/COM+.  It is easy to learn, yet provides a powerful network
infrastructure for demanding technical applications. It features an
object-oriented specification language, easy to use C++, C#, Java,
Python, Ruby, PHP, and Visual Basic mappings, a highly efficient
protocol, asynchronous method invocation and dispatch, dynamic
transport plug-ins, TCP/IP and UDP/IP support, SSL-based security, a
firewall solution, and much more.

%package -n %name-devel
Summary: Tools for developing Ice applications in Python
Group: Development/Other
Requires: %name = %version-%release
Provides: python-module-ice-devel
Obsoletes: python-module-Ice-devel

%description -n %name-devel
Ice is a modern alternative to object middleware such as CORBA or
COM/DCOM/COM+.  It is easy to learn, yet provides a powerful network
infrastructure for demanding technical applications. It features an
object-oriented specification language, easy to use C++, C#, Java,
Python, Ruby, PHP, and Visual Basic mappings, a highly efficient
protocol, asynchronous method invocation and dispatch, dynamic
transport plug-ins, TCP/IP and UDP/IP support, SSL-based security, a
firewall solution, and much more.

%prep
%setup -n IcePy-%version
%patch0 -p2
ln -s %_datadir/Ice-%version/slice slice
ln -s %_datadir/Ice-%version/certs certs
ln -s %_datadir/Ice-%version/config config
ln -s %_datadir/Ice-%version/config/Make.rules.Linux py/config
mkdir -p cpp
ln -s %_includedir cpp/include
tar xfj %SOURCE1

sed -i 's|^\(CPPFLAGS.*\)|\1 -g|' py/config/Make.rules

%build
cd py
%make_build OPTIMIZE=yes embedded_runpath_prefix="" SLICE2PY=slice2py

%install
cd py

# do not use make_install, it overrides INSTALL_DATA
mkdir -p %buildroot%python_sitelibdir/Ice
echo Ice >%buildroot%python_sitelibdir/Ice.pth
make prefix=%buildroot \
	embedded_runpath_prefix="" \
	install_pythondir=%buildroot%python_sitelibdir/Ice \
	install_libdir=%buildroot%python_sitelibdir/Ice \
	install

rm -f %buildroot/ICE_LICENSE %buildroot/LICENSE
rm -rf %buildroot/slice

%files
%doc ICE_LICENSE LICENSE
%doc py/demo
%python_sitelibdir/Ice/
%python_sitelibdir/Ice.pth

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt4
- Fixed build

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.1-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.1-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt3
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt2
- Rebuilt with python 2.6

* Mon Jun 15 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.1-alt1
- Update to new release

* Tue Jul 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt2
- fixed source URL
 + rename IcePy to Ice for new common style with Ice/py

* Mon Jul 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt1
- Update to new release

* Fri Jul 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.1-alt2.2
- fixed bugs with retrun of NullHandled proxies:
 + fixed bug in Ice.Communicator.stringToProxy(...)
 + fixed bug in Ice.Communicator.propertyToProxy(...)

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 3.2.1-alt2.1
- Rebuilt with python-2.5.

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt2
- rename package (module name is Ice)
- fix install (IcePy.so was missed), add Ice.pth

* Fri Sep 21 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1 (with rpmrb script)

* Mon Aug 06 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- add IcePy provides, change python module name to Ice

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Dec 6 2006 ZeroC Staff
- See source distributions or the ZeroC website for more information
  about the changes in this release


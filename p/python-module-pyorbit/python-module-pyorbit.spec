# TODO: tests contains compiled modules
%define major 2.24
Name: python-module-pyorbit
Version: %major.0
Release: alt1.2.1.1

Summary: Python bindings for ORBit2

Group: Development/Python
License: LGPL
Url: http://www.daa.com.au/~james/software/pygtk/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.gnome.org/pub/GNOME/sources/pyorbit/%major/pyorbit-%version.tar.bz2

%setup_python_module pyorbit

Obsoletes: orbit-python
Obsoletes: pyorbit
Provides: pyorbit

# Automatically added by buildreq on Tue Oct 07 2008 (-bi)
BuildRequires: ORBit2-devel

%description
pyorbit is an extension module for python that provides a Python
language mapping for the ORBit2 CORBA ORB.

%package devel
Summary: Files needed to build wrappers for pyorbit addon libraries
Group: Development/Python
Obsoletes: orbit-python-devel
Requires: %name = %version-%release

%description devel
This package contains files required to build extensions that
interoperate with pyorbit.

%prep
%setup -n pyorbit-%version
%configure

%build
%make_build

%install
%makeinstall
find %buildroot -name "*.la" -exec rm {} \;

%files
%python_sitelibdir/*.so
%python_sitelibdir/*.py*
%doc AUTHORS INSTALL NEWS README TODO ChangeLog
%doc tests

%files devel
%dir %_includedir/pyorbit-2/
%_includedir/pyorbit-2/*.h
%_pkgconfigdir/pyorbit-2.pc

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.0-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.0-alt1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.0-alt1.2
- Rebuilt for debuginfo

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.0-alt1.1
- Rebuilt with python 2.6

* Tue Oct 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- updated buildreqs

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.14.3-alt1.1
- Rebuilt with python-2.5.

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 2.14.3-alt1
- new version 2.14.3 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.1-alt0.1
- new version
- change URL, Source URL

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- rebuild with python 2.4

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version
- cleanup spec

* Tue Jul 13 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt5
- renamed
- cleanup spec
- adopted to python policy

* Tue Feb 10 2004 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt4
- python23 build

* Fri Nov 14 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt3
- fixed release to alt3

* Tue Nov 11 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-3
- Fixed obsoletes orbit-python

* Thu Oct 23 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-2
- hasher build

* Wed Oct 01 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-1
- initial spec for Sisyphus

* Tue Nov 12 2002  James Henstridge  <james@daa.com.au>
- initial spec file based on orbit-python's one.


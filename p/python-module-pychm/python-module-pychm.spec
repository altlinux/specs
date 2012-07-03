Name: python-module-pychm
Version: 0.8.4
Release: alt1.1.2.1.1

Summary: Python package to handle CHM files

License: GPL
Group: Development/Python
Url: http://gnochm.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/gnochm/pychm-%version.tar.bz2

Provides: pychm
%setup_python_module chm

# manually removed: eric
# Automatically added by buildreq on Mon Nov 29 2004
BuildRequires: libchm-devel python-devel python-modules-encodings

%description
The chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library
chmlib and some additional classes and functions.
They are used to access MS-ITSS encoded files -
Compressed Html Help files (.chm).

%prep
%setup -n pychm-%version

%build
%python_build_debug

%install
%python_build_install

%files
%doc README NEWS ChangeLog
%python_sitelibdir/%modulename
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt1.1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt1.1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.1.2
- Rebuilt for debuginfo

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.8.4-alt1.1
- Rebuilt with python-2.5.

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Sat Jun 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- new version
- update Source, fix files section

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version
- build with python 2.4

* Mon Nov 29 2004 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- first build for ALT Linux Sisyphus

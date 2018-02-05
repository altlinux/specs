%define oname pychm

%def_without python3

Name: python-module-%oname
Version: 0.8.4.1
Release: alt2.1

Summary: Python package to handle CHM files

License: GPL
Group: Development/Python
Url: http://gnochm.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/gnochm/%oname-%version.tar.bz2

Provides: %oname
%setup_python_module chm

BuildPreReq: libchm-devel python-devel python-modules-encodings swig

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
The chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library
chmlib and some additional classes and functions.
They are used to access MS-ITSS encoded files -
Compressed Html Help files (.chm).

%if_with python3
%package -n python3-module-%oname
Summary: Python package to handle CHM files
Group: Development/Python3
Provides: %oname-py3
%py3_provides %oname

%description -n python3-module-%oname
The chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library
chmlib and some additional classes and functions.
They are used to access MS-ITSS encoded files -
Compressed Html Help files (.chm).
%endif

%prep
%setup -n %oname-%version

rm -f chm/swig_chm.c

%if_with python3
cp -fR . ../python3
%endif

%build
swig -python -o chm/swig_chm.c chm/swig_chm.i
%python_build_debug

%if_with python3
pushd ../python3
swig -python -py3 -o chm/swig_chm.c chm/swig_chm.i
%python3_build_debug
popd
%endif

%install
%python_build_install

%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

%files
%doc AUTHORS HACKING NEWS README
%python_sitelibdir/%modulename
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS HACKING NEWS README
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.4.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4.1-alt2
- Fixed build

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4.1-alt1
- Version 0.8.4.1

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

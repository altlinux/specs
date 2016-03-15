%define oname projex_xqt

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1.git20150111.1.1
Summary: Wrapper system for Qt to bridge the gap between PySide and PyQt4 syntaxes
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/projex_xqt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/xqt.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-projex python-module-PyQt4
#BuildPreReq: python-module-PySide
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-projex python3-module-PyQt4
#BuildPreReq: python3-module-PySide
#BuildPreReq: python-tools-2to3
%endif

%py_provides xqt

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-pycrypto python-module-setuptools-tests python3-module-pycrypto python3-module-setuptools-tests rpm-build-python3 time

%description
The xqt library is a wrapper system on top of the various Python Qt
frameworks. This project will try to bridge the gap between some of the
differences between the frameworks so that developers can easily write
code that will work for any Qt implementation.

Right now, the supported wrappers are:

* PyQt4
* PySide

%package -n python3-module-%oname
Summary: Wrapper system for Qt to bridge the gap between PySide and PyQt4 syntaxes
Group: Development/Python3
%py3_provides xqt

%description -n python3-module-%oname
The xqt library is a wrapper system on top of the various Python Qt
frameworks. This project will try to bridge the gap between some of the
differences between the frameworks so that developers can easily write
code that will work for any Qt implementation.

Right now, the supported wrappers are:

* PyQt4
* PySide

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
pushd src
%python_build_debug
popd

%if_with python3
pushd ../python3/src
%python3_build_debug
popd
%endif

%install
pushd src
%python_install
for i in core gui wrappers; do
	cp -fR xqt/$i %buildroot%python_sitelibdir/xqt/
done
popd

%if_with python3
pushd ../python3/src
%python3_install
for i in core gui wrappers; do
	cp -fR xqt/$i %buildroot%python3_sitelibdir/xqt/
done
popd
%endif

%check
pushd src
python setup.py test
popd
%if_with python3
pushd ../python3/src
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.git20150111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.2-alt1.git20150111.1
- NMU: Use buildreq for BR.

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20150111
- Version 2.0.2

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141013
- Initial build for Sisyphus


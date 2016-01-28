%define oname projexui

%def_with python3

Name: python-module-%oname
Version: 3.0.3
Release: alt1.git20150217.1
Summary: Library of additional Qt widgets and plugins for PyQt4 and PySide
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/projexui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/projexui.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-projex python-module-projex_xqt
#BuildPreReq: python-module-PyQt4 python-module-PySide
#BuildPreReq: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-projex python3-module-projex_xqt
#BuildPreReq: python3-module-PyQt4 python3-module-PySide
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires logging

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: fontconfig libqt4-core libqt4-gui python-base python-devel python-module-PyQt4 python-module-projex python-module-pycrypto python-module-pytest python-module-setuptools python-module-sip python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-PyQt4 python3-module-projex python3-module-pycrypto python3-module-pytest python3-module-setuptools python3-module-sip
BuildRequires: python-module-projex_xqt python-module-setuptools-tests python3-module-projex_xqt python3-module-setuptools-tests rpm-build-python3 time

%description
Library of additional Qt widgets and plugins for PyQt4 and PySide.

http://www.projexsoftware.com/

%package -n python3-module-%oname
Summary: Library of additional Qt widgets and plugins for PyQt4 and PySide
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Library of additional Qt widgets and plugins for PyQt4 and PySide.

http://www.projexsoftware.com/

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
cp -fR ../resources/* %buildroot%python_sitelibdir/%oname/resources/
popd

%if_with python3
pushd ../python3/src
%python3_install
cp -fR ../resources/* %buildroot%python3_sitelibdir/%oname/resources/
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.3-alt1.git20150217.1
- NMU: Use buildreq for BR.

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.git20150217
- Version 3.0.3
- Added module for Python 3

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.git20141103
- Initial build for Sisyphus


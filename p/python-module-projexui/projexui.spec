%define oname projexui

%def_without python3

Name: python-module-%oname
Version: 3.0.2
Release: alt1.git20141103
Summary: Library of additional Qt widgets and plugins for PyQt4 and PySide
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/projexui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/projexui.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-projex python-module-projex_xqt
BuildPreReq: python-module-PyQt4 python-module-PySide
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-projex python3-module-projex_xqt
BuildPreReq: python3-module-PyQt4 python3-module-PySide
%endif

%py_provides %oname

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
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.git20141103
- Initial build for Sisyphus


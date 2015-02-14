%define oname axf

%def_with python3

Name: python-module-%oname
Version: 0.0.15
Release: alt1
Summary: AXANT ToscaWidget2 Widgets collection
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/axf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.forms python-module-Pillow
BuildPreReq: python-module-tw2.core python-module-TurboGears2
BuildPreReq: python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.forms python3-module-Pillow
BuildPreReq: python3-module-tw2.core python3-module-TurboGears2
BuildPreReq: python3-module-repoze.lru
%endif

%py_provides %oname
%py_requires tw2.forms PIL tw2.core tg repoze.lru

%description
AXF is a collection of ToscaWidgets2 widgets with resources loading
based on the AXEL Loader to perform resources loading so that it is
possible to replace resources and load widgets from ajax requests.

%package -n python3-module-%oname
Summary: AXANT ToscaWidget2 Widgets collection
Group: Development/Python3
%py3_provides %oname
%py3_requires tw2.forms PIL tw2.core tg repoze.lru

%description -n python3-module-%oname
AXF is a collection of ToscaWidgets2 widgets with resources loading
based on the AXEL Loader to perform resources loading so that it is
possible to replace resources and load widgets from ajax requests.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1
- Initial build for Sisyphus


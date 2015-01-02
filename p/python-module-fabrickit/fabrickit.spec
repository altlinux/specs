%define oname fabrickit

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.8
Release: alt1
Summary: Fabric API wrapper
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/fabrickit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Fabric
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Fabric
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires fabric

%description
This is a simple fabric wrapper for emitting Exceptions and several
utils.

%package -n python3-module-%oname
Summary: Fabric API wrapper
Group: Development/Python3
%py3_provides %oname
%py3_requires fabric

%description -n python3-module-%oname
This is a simple fabric wrapper for emitting Exceptions and several
utils.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Version 0.1.8

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus


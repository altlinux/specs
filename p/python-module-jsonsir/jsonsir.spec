%define oname jsonsir

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141121
Summary: A serializer for JSON-like data in Python
License: MIT
Group: Development/Python
Url: https://github.com/RussellLuo/jsonsir
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RussellLuo/jsonsir.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
A serializer for JSON-like data in Python.

%package -n python3-module-%oname
Summary: A serializer for JSON-like data in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A serializer for JSON-like data in Python.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
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
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141121
- Initial build for Sisyphus


%define oname jsonsir

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150116.1.1
Summary: A serializer for JSON-like data in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/JsonSir/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RussellLuo/jsonsir.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
BuildRequires: python-module-bson
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildRequires: python3-module-bson
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
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.git20150116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20150116.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150116
- Version 0.0.2

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141121
- Initial build for Sisyphus


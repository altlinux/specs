%define oname Resource

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20141121
Summary: A Python library concentrated on the Resource layer of RESTful APIs
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Resource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RussellLuo/resource.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jsonpatch python-module-pymongo
BuildPreReq: python-module-SQLAlchemy python-module-jsonform
BuildPreReq: python-module-jsonsir python-module-mongosql
BuildPreReq: python-module-itsdangerous python-module-requests
BuildPreReq: python-module-jsonschema
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jsonpatch python3-module-pymongo
BuildPreReq: python3-module-SQLAlchemy python3-module-jsonform
BuildPreReq: python3-module-jsonsir python3-module-mongosql
BuildPreReq: python3-module-itsdangerous python3-module-requests
BuildPreReq: python3-module-jsonschema
%endif

%py_provides rsrc

%description
A Python library concentrated on the Resource layer of RESTful APIs.

%package -n python3-module-%oname
Summary: A Python library concentrated on the Resource layer of RESTful APIs
Group: Development/Python3
%py3_provides rsrc

%description -n python3-module-%oname
A Python library concentrated on the Resource layer of RESTful APIs.

%package demos
Summary: Demos for %oname
Group: Development/Python
BuildArch: noarch

%description demos
A Python library concentrated on the Resource layer of RESTful APIs.

This package contains demos for %oname.

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
%doc *.md docs/*
%python_sitelibdir/*

%files demos
%doc demo/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141121
- Initial build for Sisyphus


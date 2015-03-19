%define oname redis_structures

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.a0.git20150318
Summary: Redis data structures wrapped with Python 3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/redis_structures/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jaredlunde/redis_structures.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-redis-py python-module-ujson
BuildPreReq: python-module-pip
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-redis-py python3-module-ujson
BuildPreReq: python3-module-pip python-tools-2to3
%endif

%py_provides %oname
%py_requires redis ujson

%description
Pythonic data structures backed by Redis.

%if_with python3
%package -n python3-module-%oname
Summary: Redis data structures wrapped with Python 3
Group: Development/Python3
%py3_provides %oname
%py3_requires redis ujson

%description -n python3-module-%oname
Pythonic data structures backed by Redis.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
2to3 -w -n %oname/__init__.py
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
py.test -vv $(find %oname -name '*.py')
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version -vv $(find %oname -name '*.py')
popd
%endif

%if_with python2
%files
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.a0.git20150318
- Initial build for Sisyphus


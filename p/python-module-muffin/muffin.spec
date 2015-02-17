%define oname muffin

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150216
Summary: A web framework based on Asyncio stack
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/muffin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/klen/muffin.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-aiohttp python-module-cached-property
BuildPreReq: python-module-peewee python-module-pyjade
BuildPreReq: python-module-werkzeug python-module-pytest-pythonpath
BuildPreReq: python-module-webtest python-module-mixer
BuildPreReq: python-module-ujson
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-aiohttp python3-module-cached-property
BuildPreReq: python3-module-peewee python3-module-pyjade
BuildPreReq: python3-module-werkzeug python3-module-pytest-pythonpath
BuildPreReq: python3-module-webtest python3-module-mixer
BuildPreReq: python3-module-ujson python3-module-gunicorn
%endif

%py_provides %oname
%py_requires aiohttp cached_property peewee pyjade werkzeug mixer ujson
%py_requires gunicorn
%add_python_req_skip pytest

%description
The Muffin - A web framework based on Asyncio stack.

%package -n python3-module-%oname
Summary: A web framework based on Asyncio stack
Group: Development/Python3
%py3_provides %oname
%py3_requires aiohttp cached_property peewee pyjade werkzeug mixer ujson
%py3_requires gunicorn
%add_python3_req_skip pytest

%description -n python3-module-%oname
The Muffin - A web framework based on Asyncio stack.

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
python setup.py test
export PYTHONPATH=$PWD
py.test -vv
%endif
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc Changelog *.rst example
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.rst example
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150216
- Version 0.0.2

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150209
- Initial build for Sisyphus


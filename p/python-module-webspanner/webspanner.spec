%define oname webspanner

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1
Summary: Micro web framework based on asyncio inspired by Flask & Express.js
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/webspanner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-routes
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-routes
%endif

%py_provides %oname
%py_requires asyncio routes

%description
Spanner is a micro web framework based on asyncio inspired by Flask &
Express.js.

%package -n python3-module-%oname
Summary: Micro web framework based on asyncio inspired by Flask & Express.js
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio routes

%description -n python3-module-%oname
Spanner is a micro web framework based on asyncio inspired by Flask &
Express.js.

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
py.test -vv %oname/*.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv %oname/*.py
popd
%endif

%if_with python2
%files
%doc PKG-INFO
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus


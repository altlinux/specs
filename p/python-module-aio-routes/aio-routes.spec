%define oname aio-routes

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20141212.1
Summary: URL routing library for asyncio 
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aio-routes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tailhook/aio-routes.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-pathlib
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-pathlib
%endif

%py_provides aioroutes
%py_requires asyncio pathlib

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-asyncio python3-module-pathlib python3-module-pytest rpm-build-python3 time

%description
Aio-routes is a URL routing library for web applications. It doesn't
support typical pattern-based or regular-expression bases routing. But
rather it traverses objects while resolving an url. See examples below,
for more info

Aioroutes works not only for HTTP but for any kind of RPC, for example
for method invocation over WebSockets. HTTP support is built-in, for
other kinds of things small pieces of glue code is needed.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Aio-routes is a URL routing library for web applications. It doesn't
support typical pattern-based or regular-expression bases routing. But
rather it traverses objects while resolving an url. See examples below,
for more info

Aioroutes works not only for HTTP but for any kind of RPC, for example
for method invocation over WebSockets. HTTP support is built-in, for
other kinds of things small pieces of glue code is needed.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: URL routing library for asyncio 
Group: Development/Python3
%py3_provides aioroutes
%py3_requires asyncio pathlib

%description -n python3-module-%oname
Aio-routes is a URL routing library for web applications. It doesn't
support typical pattern-based or regular-expression bases routing. But
rather it traverses objects while resolving an url. See examples below,
for more info

Aioroutes works not only for HTTP but for any kind of RPC, for example
for method invocation over WebSockets. HTTP support is built-in, for
other kinds of things small pieces of glue code is needed.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Aio-routes is a URL routing library for web applications. It doesn't
support typical pattern-based or regular-expression bases routing. But
rather it traverses objects while resolving an url. See examples below,
for more info

Aioroutes works not only for HTTP but for any kind of RPC, for example
for method invocation over WebSockets. HTTP support is built-in, for
other kinds of things small pieces of glue code is needed.

This package contains tests for %oname.

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
rm -fR build
py.test -vv
%endif
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.rst example.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst example.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.git20141212.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20141212
- Initial build for Sisyphus


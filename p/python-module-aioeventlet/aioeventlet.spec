%define oname aioeventlet

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1
Summary: asyncio event loop scheduling callbacks in eventlet
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aioeventlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-eventlet python-module-coverage
BuildPreReq: python-module-trollius python-module-futures
BuildPreReq: python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-eventlet python3-module-coverage
BuildPreReq: python3-module-asyncio
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires eventlet trollius

%description
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: asyncio event loop scheduling callbacks in eventlet
Group: Development/Python3
%py3_provides %oname
%py3_requires eventlet asyncio

%description -n python3-module-%oname
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#python runtests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus


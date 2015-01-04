%define oname aiopyramid

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20141211
Summary: Tools for running pyramid using asyncio
License: BSD-derived
Group: Development/Python
Url: https://pypi.python.org/pypi/aiopyramid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/housleyjk/aiopyramid.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-pyramid-tests
BuildPreReq: python-module-greenlet python-module-gunicorn
BuildPreReq: python-module-aiohttp python-module-websockets
%endif
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-pyramid-tests
BuildPreReq: python3-module-greenlet python3-module-gunicorn
BuildPreReq: python3-module-aiohttp python3-module-websockets
%endif

%py_provides %oname
%py_requires asyncio pyramid greenlet gunicorn aiohttp websockets

%description
A library for leveraging pyramid infrastructure asynchronously using the
new asyncio.

Aiopyramid provides tools for making web applications with Pyramid and
asyncio. It will not necessarily make your application run faster.
Instead, it gives you some tools and patterns to build an application on
asynchronous servers. Bear in mind that you will need to use
asynchronous libraries for io where appropriate.

%package -n python3-module-%oname
Summary: Tools for running pyramid using asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio pyramid greenlet gunicorn aiohttp websockets

%description -n python3-module-%oname
A library for leveraging pyramid infrastructure asynchronously using the
new asyncio.

Aiopyramid provides tools for making web applications with Pyramid and
asyncio. It will not necessarily make your application run faster.
Instead, it gives you some tools and patterns to build an application on
asynchronous servers. Bear in mind that you will need to use
asynchronous libraries for io where appropriate.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A library for leveraging pyramid infrastructure asynchronously using the
new asyncio.

Aiopyramid provides tools for making web applications with Pyramid and
asyncio. It will not necessarily make your application run faster.
Instead, it gives you some tools and patterns to build an application on
asynchronous servers. Bear in mind that you will need to use
asynchronous libraries for io where appropriate.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A library for leveraging pyramid infrastructure asynchronously using the
new asyncio.

Aiopyramid provides tools for making web applications with Pyramid and
asyncio. It will not necessarily make your application run faster.
Instead, it gives you some tools and patterns to build an application on
asynchronous servers. Bear in mind that you will need to use
asynchronous libraries for io where appropriate.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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
%else
install -d %buildroot%python_sitelibdir/%oname
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%doc COPYRIGHT LICENSE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc COPYRIGHT LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141211
- Initial build for Sisyphus


%define oname txaio

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150407
Summary: Compatibility API between asyncio/Twisted/Trollius
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/txaio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tavendo/txaio.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-twisted-core
BuildPreReq: python-module-pytest-cov python-tools-pep8
BuildPreReq: python-module-trollius
BuildPreReq: python-module-alabaster python-module-sphinx_rtd_theme
BuildPreReq: python-module-sphinx-devel python-module-twisted-logger
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-twisted-core
BuildPreReq: python3-module-pytest-cov python3-tools-pep8
BuildPreReq: python3-module-asyncio
BuildPreReq: python3-module-alabaster python3-module-sphinx_rtd_theme
BuildPreReq: python3-module-sphinx
%endif

%py_provides %oname
%py_requires six trollius
Requires: python-module-twisted-core
Requires: python-module-twisted-logger

%description
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

Note that, with this approach, user code runs under the native event
loop of either Twisted or asyncio. This is different from attaching
either one's event loop to the other using some event loop adapter.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Compatibility API between asyncio/Twisted/Trollius
Group: Development/Python3
%py3_provides %oname
%py3_requires six asyncio
Requires: python3-module-twisted-core

%description -n python3-module-%oname
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

Note that, with this approach, user code runs under the native event
loop of either Twisted or asyncio. This is different from attaching
either one's event loop to the other using some event loop adapter.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

This package contains pickles for %oname.

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
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=$PWD
py.test test/ -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
py.test-%_python3_version test/ -vv
popd
%endif

%files
%doc *.rst examples doc/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples doc/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150407
- Initial build for Sisyphus


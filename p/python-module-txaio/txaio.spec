%define oname txaio

%def_with python3

Name: python-module-%oname
Version: 2.8.1
Release: alt1.1
Summary: Compatibility API between asyncio/Twisted/Trollius
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/txaio/

# https://github.com/tavendo/txaio.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
Patch2: python-txaio-skip-packaging-tests.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest-cov
BuildRequires: python-module-setuptools python-module-trollius python-module-twisted-logger python-tools-pep8
BuildRequires: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pytest-cov python3-module-setuptools python3-module-sphinx
BuildRequires: python3-module-twisted-core python3-tools-pep8
BuildRequires: python3-module-mock
%endif

%py_provides %oname
%py_requires six trollius

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
%patch1 -p1
%patch2 -p0

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=$PWD
py.test test/ -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
py.test3 test/ -vv
popd
%endif

%files
%doc *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.1-alt1
- Updated to upstream version 2.8.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150407.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20150407.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150407
- Initial build for Sisyphus


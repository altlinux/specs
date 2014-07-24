%define oname zope.hookable

%def_with python3

Name: python-module-%oname
Version: 4.0.4
Release: alt1
Summary: Hookable object support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.hookable/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope

%description
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

%package -n python3-module-%oname
Summary: Hookable object support
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

%package -n python3-module-%oname-tests
Summary: Tests for zope.hookable
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

This package contains tests for zope.hookable.

%package tests
Summary: Tests for zope.hookable
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

This package contains tests for zope.hookable.

%package pickles
Summary: Pickles for zope.hookable
Group: Development/Python

%description pickles
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

This package contains pickles for zope.hookable.

%package docs
Summary: Documentation for zope.hookable
Group: Development/Documentation
BuildArch: noarch

%description docs
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

This package contains documentation for zope.hookable.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus


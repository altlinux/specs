%define oname crochet

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1.git20150505
Summary: Use Twisted anywhere!
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/crochet
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/itamarst/crochet.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-twisted-core-test
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests git
BuildPreReq: python3-module-twisted-core-test
%endif

%py_provides %oname
%py_requires twisted.internet

%description
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-twisted-core-test

%description tests
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Use Twisted anywhere!
Group: Development/Python3
%py3_provides %oname
%py3_requires twisted.internet
Requires: python3-module-twisted-core-test

%description -n python3-module-%oname
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

This package contains pickles for %oname.

%prep
%setup
sed -i 's|@VERSION@|%version|' %oname/_version.py

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

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
python -m unittest discover -v
%if_with python3
pushd ../python3
python3 setup.py test -v
#python3 -m unittest discover -v
popd
%endif

%files
%doc *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20150505
- Initial build for Sisyphus


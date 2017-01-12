%define _unpackaged_files_terminate_build 1
%define oname crochet

%def_with python3

Name: python-module-%oname
Version: 1.6.0
Release: alt1
Summary: Use Twisted anywhere!
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/crochet
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/itamarst/crochet.git
Source0: https://pypi.python.org/packages/d8/25/97bdfed382ce9087e0d8b4aa0f097774fd8c53c1a76e2310613808c9d8ba/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests git
#BuildPreReq: python-module-twisted-core-test
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests git
#BuildPreReq: python3-module-twisted-core-test
%endif

%py_provides %oname
%py_requires twisted.internet

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-twisted-core python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-pycparser python3-module-pygobject3 python3-module-pytest python3-module-serial python3-module-setuptools python3-module-zope python3-module-zope.interface
BuildRequires: git-core python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools-tests python-module-twisted-core-test python-module-twisted-logger python3-module-setuptools-tests python3-module-twisted-core rpm-build-python3 time

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
%setup -q -n %{oname}-%{version}
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.git20150505.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.git20150505.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20150505
- Initial build for Sisyphus


%define oname aiohttp

%def_without python2
%def_with python3
%def_without docs

Name: python-module-%oname
Version: 1.2.0
Release: alt1
Summary: http client/server for asyncio
License: ASLv2.0
Group: Development/Python
Url: https://github.com/KeepSafe/aiohttp.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib  python3-module-Cython

#BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius python-module-nose
#BuildPreReq: python-module-gunicorn 
#BuildPreReq: python-module-gunicorn 
BuildPreReq: python-module-chardet
BuildPreReq: python-module-objects

#BuildPreReq: python-module-flake8 python-module-coverage
#BuildPreReq: python-module-path 
#python-module-bumpversion
#BuildPreReq: python-module-Cython
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-setuptools-tests python3-module-multidict python3-module-yarl python3-module-async-timeout python3-module-trollius python3-module-asyncio python3-module-pytest-mock python3-module-chardet
%endif
%if_with docs
BuildRequires(pre): python3-module-sphinx-devel
BuildRequires: python3-module-sphinxcontrib-asyncio python3-module-sphinxcontrib-newsfeed
%endif

%py_provides %oname
#%%py_requires trollius chardet

%description
http client/server for asyncio (PEP-3156).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: http client/server for asyncio
Group: Development/Python3
%py3_provides %oname
#%%py3_requires asyncio chardet

%description -n python3-module-%oname
http client/server for asyncio (PEP-3156).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
http client/server for asyncio (PEP-3156).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
http client/server for asyncio (PEP-3156).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
rm -rf ../python3-module-%oname-%version
cp -R . ../python3-module-%oname-%version
%endif

%if_with python2
find -type f -name '*.py' -exec \
	sed -i 's|asyncio.streams|trollius.streams|g' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|import asyncio|import trollius|' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|from asyncio|from trollius|' '{}' +
%endif

%if_with docs
pushd ../python3-module-%oname-%version
%prepare_sphinx3 .
ln -s ../objects.inv docs/
popd
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3-module-%oname-%version
%python3_build_debug
popd
%endif

%if_with docs
pushd ../python3-module-%oname-%version
%make_build -C docs html SPHINXBUILD=py3_sphinx-build
#%%make_build -C docs pickle
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%if_with docs
#install -d %buildroot%python_sitelibdir/%oname
#cp -R docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
%if_with python2
python setup.py test
nosetests -s -v ./tests/
%endif
%if_with python3
pushd ../python3-module-%oname-%version
python3 setup.py test
#sed -i 's|nosetests|nosetests3|' Makefile
#sed -i 's|flake8|python3-flake8|' Makefile
#nosetests3 -s -v ./tests/
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%if_with docs
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Jan 13 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Disabled build documentation

* Sun Aug 07 2016 Anton Midyukov <antohami@altlinux.org> 0.21.5-alt1
- New version 0.21.5 (Closes: 32363)
- Disable tests (girar not support IPv6)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 0.15.3-alt7.git20150425.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)
  
* Sat Mar  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt7.git20150425
- (.spec) cleanup unneeded BuildRequires(pre): rpm-macros-sphinx
  (and other BuildReq cleanups)

* Fri Mar 04 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt6.git20150425
- Removed dependence to python-module-gunicorn, which created selfdeps.

* Thu Mar  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt5.git20150425
- (.spec) Safer build: cleanup ../python3/ before use.
  (Nevertheless, beware: using ../python3/ for the build is very dirty
  because it is not cleaned up automatically afterwards and can cause
  side-effects in other unsafe specs, similar to this one. This dirty
  use of ../python3/ is very wide-spread in Sisyphus packages.)
- (.spec) Fail if the maintainer's intentions are not fulfilled
  (because the sources or the build environment have changed since the
  spec was written): rm/cp without -f

* Thu Mar 03 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt4.git20150425.2
- Remove self dependence.

* Wed Mar 02 2016 Denis Medvedev <nbr@altlinux.org>  0.15.3-alt3.git20150425.2
- File "inv"  for sphynx is in python-sphinx-objects.inv. 

* Mon Feb 08 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt2.git20150425.2
- NMU: manual build

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.15.3-alt2.git20150425.1
- NMU: Use buildreq for BR.

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 0.15.3-alt2.git20150425
- rebuild with cleaned build requires

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.3-alt1.git20150425
- Version 0.15.3

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20150217
- Version 0.14.4

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1.git20150123
- Version 0.14.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2.git20141231
- Version 0.13.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.a0.git20141229
- Version 0.13.1a0

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20141129
- Version 0.11.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.a.git20141125
- Initial build for Sisyphus


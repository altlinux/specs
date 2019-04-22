%define _unpackaged_files_terminate_build 1

%define oname testtools

Name: python-module-%oname
Version: 2.3.0
Release: alt2
Summary: extensions to the Python standard library's unit testing framework
Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/testtools
BuildArch: noarch

# https://github.com/testing-cabal/testtools.git
Source: %name-%version.tar

Patch1: %oname-1.8.0-fedora-py3.patch

# https://github.com/testing-cabal/testtools/pull/271
Patch2: %oname-2.3.0-py37.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils
BuildRequires: python-module-extras python-module-html5lib python-module-mimeparse
BuildRequires: python-module-objects.inv python-module-pbr python-module-pytest
BuildRequires: python-module-unittest2
BuildRequires: python2.7(testscenarios) python2.7(fixtures) python-module-twisted-core-test

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-extras python3-module-html5lib python3-module-mimeparse
BuildRequires: python3-module-pbr python3-module-pytest python3-module-unittest2
BuildRequires: python3(testscenarios) python3(fixtures) python3-module-twisted-core-test

%py_requires mimeparse traceback2

%description
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: extensions to the Python 3 standard library's unit testing framework
Group: Development/Python3
%add_python3_req_skip twisted
%add_findreq_skiplist %python3_sitelibdir/%oname/_compat2x.py
%py3_requires traceback2 mimeparse

%description -n python3-module-%oname
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%prep
%setup

cp -a . ../python3

pushd ../python3
%patch1 -p1
%patch2 -p1
popd

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
export PBR_VERSION=%version

%python_build

pushd ../python3
%python3_build
popd

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

%install
export PBR_VERSION=%version

%python_install

pushd ../python3
%python3_install
popd

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PBR_VERSION=%version

%make check

pushd ../python3
%make check PYTHON=python3
popd

%files
%python_sitelibdir/testtools*
%doc LICENSE NEWS README*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%files -n python3-module-%oname
%doc LICENSE NEWS README*
%python3_sitelibdir/*


%changelog
* Mon Apr 22 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2
- Fixed build for python3.7.

* Mon Aug 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.8.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2
- Fixed requirements

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Fixed requirements

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added docs

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.8-alt1.2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.2
- Added module for Python 3 (bootstrap)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1.1
- Rebuild with Python-2.7

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9.8-alt1
- New version 0.9.8

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.7-alt1
- New version 0.9.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.6-alt1
- initial build


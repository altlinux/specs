%define _unpackaged_files_terminate_build 1

%define oname testtools

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: Extensions to the Python standard library's unit testing framework

Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/testtools

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

# https://github.com/testing-cabal/testtools/pull/271
Patch2: %oname-2.3.0-py37.patch
Patch3: testtools-2.4.0-fix_py39_test.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-extras python3-module-mimeparse
BuildRequires: python3-module-pbr python3-module-pytest python3-module-unittest2
BuildRequires: python3(testscenarios) python3(fixtures) python3-module-twisted-core-test

%add_python3_req_skip twisted
%add_findreq_skiplist %python3_sitelibdir/%oname/_compat2x.py
%py3_requires traceback2 mimeparse

%description
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

%prep
%setup
%patch3 -p1

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
export PBR_VERSION=%version
%python3_build

export PYTHONPATH=$PWD
%make -C doc html SPHINXBUILD=sphinx-build-3

%install
export PBR_VERSION=%version
%python3_install

%check
export PBR_VERSION=%version
%make check PYTHON=python3

%files
%doc LICENSE NEWS README*
%python3_sitelibdir/*

%files docs
%doc doc/_build/html/*


%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt3
- build python3 package separately
- drop BR: html5lib

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


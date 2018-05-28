%define _unpackaged_files_terminate_build 1

%define oname gitdb

%def_with python3

Name: python-module-%oname
Version: 2.0.3
Release: alt1%ubt
Summary: IO of git-style object databases
License: BSD
BuildArch: noarch
Group: Development/Python
Url: https://pypi.python.org/pypi/gitdb/

# https://github.com/gitpython-developers/gitdb.git
Source: %name-%version.tar
Patch1: %oname-alt-build.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: git-core
BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(smmap)
BuildRequires: python2.7(nose)
BuildRequires: python2.7(coverage)
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(smmap)
BuildRequires: python3(nose)
BuildRequires: python3(coverage)
%endif

%description
IO of git-style object databases.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
IO of git-style object databases.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: IO of git-style object databases
Group: Development/Python3

%description -n python3-module-%oname
IO of git-style object databases.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
IO of git-style object databases.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
IO of git-style object databases.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
IO of git-style object databases.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing
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

%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
# needed for tests
git config --global user.email "darktemplar at altlinux.org"
git config --global user.name "darktemplar"

git init
git add -A
git commit -m "%version"
git tag %version -m "%version"

# TODO: This test doesn't work, remove it for now
rm -f gitdb/test/performance/test_pack_streaming.py

%make coverage

%if_with python3
pushd ../python3

# needed for tests
git init
git add -A
git commit -m "%version"
git tag %version -m "%version"

# TODO: This test doesn't work, remove it for now
rm -f gitdb/test/performance/test_pack_streaming.py

%make coverage PYTHON=python3 TESTRUNNER=$(which nosetests3)
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.3-alt1%ubt
- Updated to upstream version 2.0.3.

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.4-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.git20150112
- Version 0.6.4

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141114
- Version 0.6.0
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALTLinux Sisyphus


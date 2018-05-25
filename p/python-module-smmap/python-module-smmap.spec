%define _unpackaged_files_terminate_build 1

%define oname smmap

%def_with python3

Name: python-module-%oname
Version: 2.0.3
Release: alt1%ubt
Summary:  Sliding window memory map manager
License: BSD
BuildArch: noarch
Group: Development/Python
Url: https://pypi.org/project/smmap2

# https://github.com/gitpython-developers/smmap.git
Source: %name-%version.tar
Patch1: %oname-alt-docs.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-coverage python-module-nosexcover
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-coverage python3-module-nosexcover
%endif

%description
A pure python implementation of a sliding window memory map manager

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary:  Sliding window memory map manager
Group: Development/Python3

%description -n python3-module-%oname
A pure python implementation of a sliding window memory map manager

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

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

export PYTHONOPATH=%buildroot%python_sitelibdir
%make -C doc html

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.md doc/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%if_with python3
%files -n python3-module-%oname
%doc README.md doc/build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.3-alt1%ubt
- Updated to upstream version 2.0.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.git20150107.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150107.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150107.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150107
- Version 0.9.0

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141113
- Version 0.8.3

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140714
- New snapshot
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- initial

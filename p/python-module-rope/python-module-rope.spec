%define _unpackaged_files_terminate_build 1
%define real_name rope

%def_without python3

Summary: python refactoring library
Name: python-module-%real_name
Version: 0.10.3
Release: alt1.1
License: GPLv2
Group: Development/Python
Url: http://rope.sf.net
BuildArch: noarch

Source0: https://pypi.python.org/packages/e1/5e/fe00383d52d0a1e0be42e6f1ee98d53902bfffb6b2835616c0fceca45597/rope-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %real_name

%description
%summary

%if_with python3
%package -n python3-module-%real_name
Summary: python refactoring library
Group: Development/Python3
%py3_provides %real_name

%description -n python3-module-%real_name
%summary

%package -n python3-module-%real_name-tests
Summary: Tests for rope
Group: Development/Python3
Requires: python3-module-%real_name = %version-%release

%description -n python3-module-%real_name-tests
%summary

This package contains tests for rope.
%endif

%package tests
Summary: Tests for rope
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for rope.

%prep
%setup -q -n rope-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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
cp -fR ropetest %buildroot%python3_sitelibdir/
popd
%endif

cp -fR ropetest %buildroot%python_sitelibdir/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc COPYING README* docs PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/ropetest

%files tests
%python_sitelibdir/ropetest

%if_with python3
%files -n python3-module-%real_name
%doc COPYING README* docs PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/ropetest

%files -n python3-module-%real_name-tests
%python3_sitelibdir/ropetest
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.3-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20150111
- New snapshot

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20141228
- New snapshot

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1
- Version 0.10.2

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.3-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2 (ALT #17977)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Rebuilt with python 2.6

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.8.2-alt1
- Initial ALT build

%define oname signalfd

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.3.1
Summary: Python bindings for sigprocmask(2) and signalfd(2)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-signalfd/

Source: %name-%version.tar

BuildRequires: python-module-pytest python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pytest
%endif

%py_provides %oname

%description
Python bindings for sigprocmask(2) and signalfd(2).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python bindings for sigprocmask(2) and signalfd(2).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python bindings for sigprocmask(2) and signalfd(2)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python bindings for sigprocmask(2) and signalfd(2).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python bindings for sigprocmask(2) and signalfd(2).

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
rm build -fR
python setup.py build_ext -i
py.test -vv
%if_with python3
pushd ../python3
rm build -fR
python3 setup.py build_ext -i
py.test3 -vv
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.3
- Fixed build.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 0.1-alt1.2
- Fix test for python3.5

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus


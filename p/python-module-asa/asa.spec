%define oname asa

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt3.1
Summary: Python bindings for the ASA
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyasa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython libnumpy-devel
BuildRequires: python-module-html5lib python-module-notebook python-module-numpy-testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-html5lib python3-module-notebook python3-module-numpy-testing
%endif

%description
Python bindings for the Adaptive Simulated Annealing (ASA).

%package -n python3-module-%oname
Summary: Python bindings for the ASA
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for the Adaptive Simulated Annealing (ASA).

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

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt3
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt2.1
- NMU: Use buildreq for BR.

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added module for Python 3

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus


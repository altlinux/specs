%define oname asa

Name: python-module-%oname
Version: 0.4
Release: alt1
Summary: Python bindings for the ASA
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyasa/0.4
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython libnumpy-devel

%description
Python bindings for the Adaptive Simulated Annealing (ASA).

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus


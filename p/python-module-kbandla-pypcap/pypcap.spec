%define oname pypcap
Name: python-module-kbandla-%oname
Version: 0.3
Release: alt1.git20150224
Summary: Python/C bindings for the libpcap library 
License: BSD
Group: Development/Python
Url: https://github.com/kbandla/pypcap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kbandla/pypcap.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests libpcap-devel

%py_provides %oname
Provides: python-module-%oname = %EVR

%description
Python/C bindings for the libpcap library. Most of the functions are 1:1
mapped to the libpcap library.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc *.html *.md
%python_sitelibdir/*

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150224
- Initial build for Sisyphus


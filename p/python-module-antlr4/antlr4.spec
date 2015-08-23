%define oname antlr4
Name: python-module-%oname
Version: 4.5.2
Release: alt1
Summary: ANTLR 4.5 runtime for Python 2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/antlr4-python2-runtime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests

%py_provides %oname

%description
ANTLR 4.5 runtime for Python 2.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.2-alt1
- Version 4.5.2

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5-alt1
- Initial build for Sisyphus


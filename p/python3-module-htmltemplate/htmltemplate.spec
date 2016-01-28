%define oname htmltemplate
Name: python3-module-%oname
Version: 2.2.0
Release: alt1.1
Summary: A simple, powerful [X]HTML templating library for Python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/htmltemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests

%py3_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-pytest rpm-build-python3 time

%description
htmltemplate converts [X]HTML documents into simple template object
models easily manipulated using ordinary Python code. It is powerful,
flexible, and easy to use.

%package docs
Summary: Documentation and samples for %oname
Group: Development/Python3

%description docs
htmltemplate converts [X]HTML documents into simple template object
models easily manipulated using ordinary Python code. It is powerful,
flexible, and easy to use.

This package contains documentation and samples for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
py.test-%_python3_version

%files
%python3_sitelibdir/*

%files docs
%doc doc sample

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.2.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus


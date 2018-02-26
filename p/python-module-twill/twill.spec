%define oname twill
Name: python-module-%oname
Version: 0.9
Release: alt1.1
Summary: twill Web browsing language
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/twill/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

%package docs
Summary: Documentation for twill
Group: Development/Documentation

%description docs
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

This package contains documentation and examples for twill.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README*
%_bindir/*
%python_sitelibdir/*

%files docs
%doc doc/* examples

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt1.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus


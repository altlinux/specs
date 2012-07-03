%define oname pyramid_formalchemy
Name: python-module-%oname
Version: 0.4.2
Release: alt1
Summary: FormAlchemy plugins and helpers for Pyramid
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_formalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute python-module-babel

%py_requires pyramid

%description
This module provide a set of utilities for using FormAlchemy with
Pyramid.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus


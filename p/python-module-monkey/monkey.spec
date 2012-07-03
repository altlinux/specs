%define oname monkey
Name: python-module-%oname
Version: 0.1
Release: alt1.1
Summary: A package that provides tools for guerilla (monkey)-patching
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/monkey/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Provides tools for guerilla (monkey)-patching.

The package provides two methods, patch and wrap, that are used to
decorate the patch method.

Patching is only allowed if a signature on the original method is
provided. Multiple signatures can be provided corresponding to various
bona fide versions of the method.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus


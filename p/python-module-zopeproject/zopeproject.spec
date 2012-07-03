%define oname zopeproject
Name: python-module-%oname
Version: 0.4.2
Release: alt1.1
Summary: Tools for creating development sandboxes for web applications that primarily use Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zopeproject/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Tools and scripts for creating development sandboxes for web
applications that primarily use Zope.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus


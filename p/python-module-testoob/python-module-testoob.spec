%define oname testoob
Name: python-module-%oname
Version: 1.15
Release: alt1.1
Summary: Testing Out Of (The) Box

Group: Development/Python
License: Apache License, Version 2.0
URL: http://testoob.sourceforge.net/
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel

%description
Testoob is an advanced Python unit testing framework that
integrates effortlessly with Python's standard 'unittest'
module.

%prep
%setup

%build
%python_build

%install
%python_install 

cp -fR tests %buildroot%python_sitelibdir/%oname/
touch %buildroot%python_sitelibdir/%oname/tests/__init__.py

%files
%doc README docs/CHANGELOG docs/COPYING docs/LICENSE-2.0.txt
%python_sitelibdir/*
%_bindir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.15-alt1.1
- Rebuild with Python-2.7

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1
- Version 1.15

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt2
- Rebuilt with python 2.6

* Thu Oct 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1
- Initial build for Sisyphus


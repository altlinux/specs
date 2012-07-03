%define oname BlastOff
Name: python-module-%oname
Version: 0.3a2
Release: alt1.1
Summary: A Pylons application template providing a working site skeleton
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/BlastOff/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_provides %oname

%description
A Pylons application template providing a working site skeleton
configured with SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail,
WebFlash and (optionally) SchemaBot. The generated app is pre-configured
with authentication, login and registration forms, and (optionally)
email confirmation.

BlastOff helps accelerate Pylons application development by generating a
project with a number of pre-configured dependencies.

%package tests
Summary: Tests for BlastOff
Group: Development/Python
Requires: %name = %version-%release
%add_findreq_skiplist %python_sitelibdir/blastoff/template/+package+/tests/*.py_tmpl

%description tests
A Pylons application template providing a working site skeleton
configured with SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail,
WebFlash and (optionally) SchemaBot. The generated app is pre-configured
with authentication, login and registration forms, and (optionally)
email confirmation.

BlastOff helps accelerate Pylons application development by generating a
project with a number of pre-configured dependencies.

This package contains tests for BlastOff.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test.*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/test.*
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3a2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3a2-alt1
- Initial build for Sisyphus


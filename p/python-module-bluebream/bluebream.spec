%define oname bluebream
Name: python-module-%oname
Version: 1.0
Release: alt3.1
Summary: The Zope Web Framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/bluebream/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-zc.buildout python-module-PasteScript
BuildPreReq: python-module-PasteDeploy

%py_requires paste.script

%description
BlueBream -- formerly known as Zope 3 -- is a web framework written in
the Python programming language.

%package tests
Summary: Tests for BlueBream
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout

%description tests
BlueBream -- formerly known as Zope 3 -- is a web framework written in
the Python programming language.

This package contains tests for BlueBream.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Really added necessary requirements

* Mon Jun 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


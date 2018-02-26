%define oname z3c.jbot
Name: python-module-%oname
Version: 0.6.3
Release: alt2.1
Summary: Drop-in template overrides
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.jbot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.pagetemplate zope.component zope.configuration
%py_requires zope.security zope.publisher

%description
The z3c.jbot (or "Just a bunch of templates") package allows easy
customization of existing templates and images. It works on Zope 2 and
Zope 3.

%package tests
Summary: Tests for z3c.jbot
Group: Development/Python
Requires: %name = %version-%release

%description tests
The z3c.jbot (or "Just a bunch of templates") package allows easy
customization of existing templates and images. It works on Zope 2 and
Zope 3.

This package contains tests for z3c.jbot.

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
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.3-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus


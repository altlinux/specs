%define oname z3c.relationfieldui
Name: python-module-%oname
Version: 0.5
Release: alt2.1
Summary: A widget for z3c.relationfield
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.relationfieldui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.relationfield z3c.schema2xml zc.sourcefactory
%py_requires grokcore.component grokcore.view hurry.resource
%py_requires zope.fanstatic

%description
This package implements a zope.formlib compatible widget for relations
as defined by z3c.relationfield.

This package does not provide a z3c.form widget for z3c.relationfield,
but it is hoped that will eventually be developed as well (in another
package).

%package tests
Summary: Tests for z3c.relationfieldui
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements a zope.formlib compatible widget for relations
as defined by z3c.relationfield.

This package does not provide a z3c.form widget for z3c.relationfield,
but it is hoped that will eventually be developed as well (in another
package).

This package contains tests for z3c.relationfieldui.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus


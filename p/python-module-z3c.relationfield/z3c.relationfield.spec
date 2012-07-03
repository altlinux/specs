%define oname z3c.relationfield
Name: python-module-%oname
Version: 0.6.1
Release: alt2.1
Summary: A relation field framework for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.relationfield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 grokcore.component zope.app.intid zope.app.container
%py_requires z3c.objpath zc.relation zope.app.zcmlfiles
%py_requires zope.securitypolicy

%description
This package implements a new schema field Relation, and the
RelationValue objects that store actual relations. It can index these
relations using the zc.relation infractructure, and using these indexes
can efficiently answer questions about the relations.

%package tests
Summary: Tests for z3c.relationfield
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements a new schema field Relation, and the
RelationValue objects that store actual relations. It can index these
relations using the zc.relation infractructure, and using these indexes
can efficiently answer questions about the relations.

This package contains tests for z3c.relationfield.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus


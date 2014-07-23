%define oname z3c.relationfield

%def_with python3

Name: python-module-%oname
Version: 0.6.3
Release: alt1
Summary: A relation field framework for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.relationfield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 grokcore.component zope.app.intid zope.app.container
%py_requires z3c.objpath zc.relation zope.app.zcmlfiles
%py_requires zope.securitypolicy

%description
This package implements a new schema field Relation, and the
RelationValue objects that store actual relations. It can index these
relations using the zc.relation infractructure, and using these indexes
can efficiently answer questions about the relations.

%package -n python3-module-%oname
Summary: A relation field framework for Zope 3
Group: Development/Python3
%py3_requires ZODB3 grokcore.component zope.app.intid zope.app.container
%py3_requires z3c.objpath zc.relation zope.app.zcmlfiles
%py3_requires zope.securitypolicy

%description -n python3-module-%oname
This package implements a new schema field Relation, and the
RelationValue objects that store actual relations. It can index these
relations using the zc.relation infractructure, and using these indexes
can efficiently answer questions about the relations.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.relationfield
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package implements a new schema field Relation, and the
RelationValue objects that store actual relations. It can index these
relations using the zc.relation infractructure, and using these indexes
can efficiently answer questions about the relations.

This package contains tests for z3c.relationfield.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1
- Version 0.6.3
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus


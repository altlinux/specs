%define oname z3c.relationfieldui

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt3
Summary: A widget for z3c.relationfield
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.relationfieldui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.relationfield z3c.schema2xml zc.sourcefactory
%py_requires grokcore.component grokcore.view hurry.resource
%py_requires zope.fanstatic

%description
This package implements a zope.formlib compatible widget for relations
as defined by z3c.relationfield.

This package does not provide a z3c.form widget for z3c.relationfield,
but it is hoped that will eventually be developed as well (in another
package).

%package -n python3-module-%oname
Summary: A widget for z3c.relationfield
Group: Development/Python3
%py3_requires z3c.relationfield z3c.schema2xml zc.sourcefactory
%py3_requires grokcore.component grokcore.view hurry.resource
%py3_requires zope.fanstatic

%description -n python3-module-%oname
This package implements a zope.formlib compatible widget for relations
as defined by z3c.relationfield.

This package does not provide a z3c.form widget for z3c.relationfield,
but it is hoped that will eventually be developed as well (in another
package).

%package -n python3-module-%oname-tests
Summary: Tests for z3c.relationfieldui
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package implements a zope.formlib compatible widget for relations
as defined by z3c.relationfield.

This package does not provide a z3c.form widget for z3c.relationfield,
but it is hoped that will eventually be developed as well (in another
package).

This package contains tests for z3c.relationfieldui.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus


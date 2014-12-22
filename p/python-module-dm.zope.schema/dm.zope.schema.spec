%define mname dm.zope
%define oname %mname.schema

%def_disable check

Name: python-module-%oname
Version: 2.1
Release: alt1
Summary: 'zope.schema' extensions
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.zope.schema/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-decorator
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-dm.reuse
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.form

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.schema dm.reuse decorator zope.formlib zope.publisher
%py_requires zope.interface zope.i18nmessageid zope.app.form

%description
This package contains extensions for zope.schema.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains extensions for zope.schema.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires dm

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 dm/zope/__init__.py \
	%buildroot%python_sitelibdir/dm/zope/

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/dm/zope/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/dm/zope/*/tests.*
%exclude %python_sitelibdir/dm/zope/__init__.py*

%files tests
%python_sitelibdir/dm/zope/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/dm/zope
%python_sitelibdir/dm/zope/__init__.py*

%changelog
* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1
- Initial build for Sisyphus


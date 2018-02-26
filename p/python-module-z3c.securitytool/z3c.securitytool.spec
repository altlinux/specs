%define oname z3c.securitytool
Name: python-module-%oname
Version: 0.5.1
Release: alt2.1
Summary: A security audit tool and demo for Zope3 views
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.securitytool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.publisher zope.component zope.interface
%py_requires zope.app.pagetemplate zope.pagetemplate zope.app.zapi
%py_requires zope.security zope.session zope.testing zope.app.testing
%py_requires zope.app.twisted zope.app.apidoc zope.securitypolicy
%py_requires zope.app.security zope.app.securitypolicy zope.annotation
%py_requires zope.app.authentication zope.app.folder zope.testbrowser
%py_requires zope.i18n zope.i18nmessageid zope.configuration zope.event
%py_requires zope.lifecycleevent zope.location zope.schema z3c.macro
%py_requires z3c.layer.minimal zope.viewlet

%description
z3c.securitytool is a Zope3 package aimed at providing component level
security information to assist in analyzing security problems and to
potentially expose weaknesses. The goal of the security tool is to
provide a matrix of users and their effective permissions for all
available views for any given component and context. We also provide two
further levels of detail. You can view the details of how a user came to
have the permission on a given view, by clicking on the permission in
the matrix.

%package tests
Summary: Tests for a security audit tool and demo for Zope3 views
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.container zope.testing z3c.coverage z3c.template
%py_requires zope.app.i18n zope.dublincore

%description tests
z3c.securitytool is a Zope3 package aimed at providing component level
security information to assist in analyzing security problems and to
potentially expose weaknesses. The goal of the security tool is to
provide a matrix of users and their effective permissions for all
available views for any given component and context. We also provide two
further levels of detail. You can view the details of how a user came to
have the permission on a given view, by clicking on the permission in
the matrix.

This package contains tests for a security audit tool and demo for Zope3
views.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus


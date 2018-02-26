%define oname zc.displayname
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: A Zope 3 extension for pluggable display names
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.displayname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.container zope.app.pagetemplate zope.component
%py_requires zope.dublincore zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.location zope.proxy zope.publisher zope.security
%py_requires zope.testing zope.traversing

%description
The default display name generator simply takes a Dublin Core title or a
__name__ and returns it, truncated if desired. It uses a helper function
intended to make writing other display name generators easier,
convertName.

No help is offered yet for using HTML with the
IBrowserDisplayNameGenerator interface.

Given an ILocation that can be adapted to
zope.dublincore.interfaces.IDCDescriptiveProperties, and that actually
has a value for it, it returns the DC title; otherwise, it uses
__name__.

%package tests
Summary: Tests for zc.displayname
Group: Development/Python
Requires: %name = %version-%release

%description tests
The default display name generator simply takes a Dublin Core title or a
__name__ and returns it, truncated if desired. It uses a helper function
intended to make writing other display name generators easier,
convertName.

No help is offered yet for using HTML with the
IBrowserDisplayNameGenerator interface.

Given an ILocation that can be adapted to
zope.dublincore.interfaces.IDCDescriptiveProperties, and that actually
has a value for it, it returns the DC title; otherwise, it uses
__name__.

This package contains tests for zc.displayname.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


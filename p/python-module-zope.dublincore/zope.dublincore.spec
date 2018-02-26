%define oname zope.dublincore
Name: python-module-%oname
Version: 3.8.2
Release: alt2.1
Summary: Zope Dublin Core implementation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.dublincore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope pytz zope.component zope.datetime zope.interface
%py_requires zope.lifecycleevent zope.location zope.schema zope.security

%description
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

%package tests
Summary: Tests for zope.dublincore
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.annotation zope.configuration

%description tests
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

This package contains tests for zope.dublincore.

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

#files tests
#python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1
- Initial build for Sisyphus


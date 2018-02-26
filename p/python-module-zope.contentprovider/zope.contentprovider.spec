%define oname zope.contentprovider
Name: python-module-%oname
Version: 3.7.2
Release: alt2.1
Summary: Content Provider Framework for Zope Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.contentprovider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.component zope.event zope.interface zope.location
%py_requires zope.publisher zope.schema zope.tales

%description
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

%package tests
Summary: Tests for zope.contentprovider
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.browserpage zope.testing

%description tests
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

This package contains tests for zope.contentprovider.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus


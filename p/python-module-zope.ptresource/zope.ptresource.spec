%define oname zope.ptresource
Name: python-module-%oname
Version: 3.9.0
Release: alt3.1
Summary: Page template resource plugin for zope.browserresource
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.ptresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.browserresource zope.interface zope.pagetemplate
%py_requires zope.publisher zope.security

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

%package tests
Summary: Tests for zope.ptresource
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

This package contains tests for zope.ptresource.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus


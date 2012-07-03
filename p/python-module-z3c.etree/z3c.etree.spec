%define oname z3c.etree
Name: python-module-%oname
Version: 0.9.2
Release: alt2.1
Summary: Integrating any ElementTree engine with the Zope component architecture
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.etree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
z3c.etree provides some mechanisms (a common interface) for integrating
any ElementTree engine with the Zope component architecture. This allows
applications to look up a engine against this interface. As such this
package does not implement the ElementTree API.

z3c.etree also provides a set of utilities that can be used to make
testing XML output in doctests easier. This functionality can also be
called from a python based unit test via the assertXMLEqual method.

%package tests
Summary: Tests for z3c.etree
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component elementtree cElementTree lxml

%description tests
z3c.etree provides some mechanisms (a common interface) for integrating
any ElementTree engine with the Zope component architecture. This allows
applications to look up a engine against this interface. As such this
package does not implement the ElementTree API.

z3c.etree also provides a set of utilities that can be used to make
testing XML output in doctests easier. This functionality can also be
called from a python based unit test via the assertXMLEqual method.

This package contains tests for z3c.etree.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus


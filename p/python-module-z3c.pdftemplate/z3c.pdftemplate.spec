%define oname z3c.pdftemplate
Name: python-module-%oname
Version: 0.2.0
Release: alt2.1
Summary: PDF Template
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pdftemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.rml reportlab zope.app.pagetemplate zope.app.publisher
%py_requires zope.component zope.interface zope.publisher zope.schema

%description
Quickly generate PDF files using page templates and RML.

%package tests
Summary: Tests for PDF Template
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.principalannotation
%py_requires zope.copypastemove zope.app.container zope.app.folder

%description tests
Quickly generate PDF files using page templates and RML.

This package contains tests for PDF Template.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus


%define oname z3c.rmldocument
Name: python-module-%oname
Version: 1.0
Release: alt3.1
Summary: User-editable RML documents
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rmldocument/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.rml zope.app.pagetemplate lxml

%description
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

%package tests
Summary: Tests for User-editable RML documents
Group: Development/Python
Requires: %name = %version-%release

%description tests
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

This package contains tests for User-editable RML documents.

%package examples
Summary: Examples for User-editable RML documents
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

This package contains examples for User-editable RML documents.

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
%exclude %python_sitelibdir/*/*/examples

%files tests
%python_sitelibdir/*/*/tests.*

%files examples
%python_sitelibdir/*/*/examples

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Extracted examples into separate package

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


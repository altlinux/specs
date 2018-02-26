%define oname z3c.rml
Name: python-module-%oname
Version: 0.9.1
Release: alt2.1
Summary: An alternative implementation of RML
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires lxml pyPdf reportlab zope.interface zope.schema

%description
This is an alternative implementation of ReportLab's RML PDF generation
XML format. Like the original implementation, it is based on ReportLab's
reportlab library.

You can read all about z3c.rml and see many examples on how to use it,
see the "RML Reference":
http://svn.zope.org/z3c.rml/trunk/src/z3c/rml/rml-reference.pdf?view=auto

%package tests
Summary: Tests for alternative implementation of RML
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.pagetemplate zope.testing

%description tests
This is an alternative implementation of ReportLab's RML PDF generation
XML format. Like the original implementation, it is based on ReportLab's
reportlab library.

You can read all about z3c.rml and see many examples on how to use it,
see the "RML Reference":
http://svn.zope.org/z3c.rml/trunk/src/z3c/rml/rml-reference.pdf?view=auto

This package contains tests for alternative implementation of RML.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus


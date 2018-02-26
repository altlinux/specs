%define oname DocumentTemplate
Name: python-module-%oname
Version: 2.13.2
Release: alt1.1
Summary: Document Templating Markup Language (DTML)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/DocumentTemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires AccessControl Acquisition ExtensionClass RestrictedPython
%py_requires zExceptions zope.sequencesort zope.structuredtext

%description
This package implements the original Document Templating Markup Language
(DTML). It uses custom SGML tags to implement simple programmatic
features, such as variable replacement, conditional logic and loops.

Inside Zope environments page templates and TAL have superseded DTML for
most use cases.

%package tests
Summary: Tests for DocumentTemplate
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements the original Document Templating Markup Language
(DTML). It uses custom SGML tags to implement simple programmatic
features, such as variable replacement, conditional logic and loops.

Inside Zope environments page templates and TAL have superseded DTML for
most use cases.

This package contains tests for DocumentTemplate.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.2-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Version 2.13.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt2
- Added necessary requirements

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1
- Initial build for Sisyphus


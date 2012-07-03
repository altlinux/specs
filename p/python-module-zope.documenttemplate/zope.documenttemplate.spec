%define oname zope.documenttemplate
Name: python-module-%oname
Version: 3.4.3
Release: alt1
Summary: Document Templating Markup Language (DTML)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.documenttemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.structuredtext

%description
This package implements the Document Templating Markup Language (DTML).
It uses custom SGML tags to implement simple programmatic feratures,
such as variable replacement, conditional logic and loops.

DTML was the first templating language developed for Zope 2 and is still
preferred by some over newer templating solutions due to its speed and
simplicity.

%package tests
Summary: Tests for Document Templating Markup Language (DTML)
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.security zope.testing

%description tests
This package implements the Document Templating Markup Language (DTML).
It uses custom SGML tags to implement simple programmatic feratures,
such as variable replacement, conditional logic and loops.

DTML was the first templating language developed for Zope 2 and is still
preferred by some over newer templating solutions due to its speed and
simplicity.

This package contains tests for Document Templating Markup Language
(DTML).

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
%exclude %python_sitelibdir/*/*/tests*
%exclude %python_sitelibdir/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests*
%python_sitelibdir/*/*/*/tests*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.3-alt1
- Version 3.4.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1
- Initial build for Sisyphus


%define oname grokcore.message
Name: python-module-%oname
Version: 0.4.2
Release: alt2.1
Summary: Grok messaging machinery
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.message/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component z3c.flashmessage zope.component
%py_requires zope.traversing

%description
This package provides integration of z3c.flashmessage for a grok setup.
This means taking care of:

* Registering a global message receiver with the component
  architechture.
* Registering by default a global session-based message source named
  session.
* Optionally (if including ram.zcml) registering a global RAM stored
  message source named ram.
* Providing components to make use of global message receivers and
  sources.

%package tests
Summary: Tests for grokcore.message
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.publisher zope.security zope.session

%description tests
This package provides integration of z3c.flashmessage for a grok setup.
This means taking care of:

* Registering a global message receiver with the component
  architechture.
* Registering by default a global session-based message source named
  session.
* Optionally (if including ram.zcml) registering a global RAM stored
  message source named ram.
* Providing components to make use of global message receivers and
  sources.

This package contains tests for grokcore.message.

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
%python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus


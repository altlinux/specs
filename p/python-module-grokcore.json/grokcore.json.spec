%define oname grokcore.json
Name: python-module-%oname
Version: 1.1
Release: alt1.1
Summary: JSON View component for Grok
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.json/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component grokcore.security grokcore.view
%py_requires martian simplejson zope.component zope.interface
%py_requires zope.publisher

%description
JSON View component for Grok.

%package tests
Summary: Tests for grokcore.json
Group: Development/Python
Requires: %name = %version-%release

%description tests
JSON View component for Grok.

This package contains tests for grokcore.json.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


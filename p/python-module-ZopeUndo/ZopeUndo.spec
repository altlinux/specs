%define oname ZopeUndo
Name: python-module-%oname
Version: 2.12.0
Release: alt1.1
Summary: ZODB undo support for Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/ZopeUndo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package is included in Zope 2. It can be used in a ZEO server to
allow it to support Zope 2's undo log , without pulling in all of Zope
2.

%package tests
Summary: Tests for ZopeUndo
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package contains tests for ZopeUndo.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12.0-alt1.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus


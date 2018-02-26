Name: grokproject
Version: 2.6
Release: alt2.1
Summary: Creates complete skeleton for a new Grok web application
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokproject/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

Requires: python-module-%name = %version-%release

%description
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

%package -n python-module-%name
Summary: Python files for grokproject
Group: Development/Python
Requires: python-module-PasteScript

%description -n python-module-%name
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

This package contains python files for grokproject.

%package -n python-module-%name-tests
Summary: Tests for grokproject
Group: Development/Python
Requires: python-module-%name = %version-%release

%description -n python-module-%name-tests
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

This package contains tests for grokproject.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%_bindir/*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/*/tests

%files -n python-module-%name-tests
%python_sitelibdir/*/*/*/*/tests

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt2
- Added necessary requirements

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Initial build for Sisyphus


%def_with python3

Name: grokproject
Version: 2.9
Release: alt2
Summary: Creates complete skeleton for a new Grok web application
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokproject/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%name = %version-%release

%description
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

%package -n python-module-%name
Summary: Python files for grokproject
Group: Development/Python
Requires: python-module-PasteScript
%py_requires grok zc.buildout

%description -n python-module-%name
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

This package contains python files for grokproject.

%package -n python3-module-%name
Summary: Python files for grokproject
Group: Development/Python3
Requires: python3-module-PasteScript
%py3_requires grok zc.buildout

%description -n python3-module-%name
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

%package -n python3-module-%name-tests
Summary: Tests for grokproject
Group: Development/Python3
Requires: python3-module-%name = %version-%release
%py3_requires zope.component zope.publisher.browser
%py3_requires zope.fanstatic.testing

%description -n python3-module-%name-tests
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

This package contains tests for grokproject.

%package -n python-module-%name-tests
Summary: Tests for grokproject
Group: Development/Python
Requires: python-module-%name = %version-%release
%py_requires zope.component zope.publisher.browser
%py_requires zope.fanstatic.testing

%description -n python-module-%name-tests
Script that creates a Grok project directory, installs Grok, the Grok
Toolkit and the Zope Toolkit and sets up a complete skeleton for a new
Grok web application.

This package contains tests for grokproject.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/*/tests

%files -n python-module-%name-tests
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%name
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%name-tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version 2.9

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1
- Version 2.7

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt2
- Added necessary requirements

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Initial build for Sisyphus


%define oname zest.releaser

Name: python-module-%oname
Version: 3.48
Release: alt1

Summary: Software releasing made easy and repeatable
License: GPLv2+
Group: Development/Python

Url: https://pypi.python.org/pypi/zest.releaser

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-distribute

%setup_python_module %oname

Requires: python-module-zest = %EVR

%description
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

%package tests
Summary: Tests for zest.releaser
Group: Development/Python
Requires: %name = %EVR

%description tests
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

This package contains tests for zest.releaser.

%package -n python-module-zest
Summary: Core package of zest
Group: Development/Python

%description -n python-module-zest
This package contains core package of zest.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

touch %buildroot%python_sitelibdir/zest/__init__.py

%files
%doc *.rst
%doc doc/source/*
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/zest/__init__.py*

%files tests
%python_sitelibdir/*/*/tests

%files -n python-module-zest
%dir %python_sitelibdir/zest
%python_sitelibdir/zest/__init__.py*

%changelog
* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.48-alt1
- Version 3.48

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.46-alt1
- Version 3.46

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.44-alt1
- Initial build for Sisyphus


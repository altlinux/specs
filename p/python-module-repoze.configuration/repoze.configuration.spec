%define oname repoze.configuration
Name: python-module-%oname
Version: 0.7
Release: alt1.git20110222.1.1
Summary: Extensible, YAML-based configuration for Python applications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.configuration
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.configuration.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze yaml

%description
``repoze.configuration`` is a package that software developers can use
as a configuration system.  It allows the use of ``YAML`` as a
configuration language.  Application-defined "directives" can be
plugged in to ``repoze.configuration`` using one or more Python
setuptools entry points.

%package tests
Summary: Tests for repoze.configuration
Group: Development/Python
Requires: %name = %version-%release

%description tests
``repoze.configuration`` is a package that software developers can use
as a configuration system.  It allows the use of ``YAML`` as a
configuration language.  Application-defined "directives" can be
plugged in to ``repoze.configuration`` using one or more Python
setuptools entry points.

This package contains tests for repoze.configuration.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20110222
- Initial build for Sisyphus


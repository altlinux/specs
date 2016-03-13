%define oname repoze.configuration

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt2.git20120329.1
Summary: Extensible, YAML-based configuration for Python applications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.configuration
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.configuration.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze yaml

%description
``repoze.configuration`` is a package that software developers can use
as a configuration system.  It allows the use of ``YAML`` as a
configuration language.  Application-defined "directives" can be
plugged in to ``repoze.configuration`` using one or more Python
setuptools entry points.

%package -n python3-module-%oname
Summary: Extensible, YAML-based configuration for Python applications
Group: Development/Python3
%py3_requires repoze yaml

%description -n python3-module-%oname
``repoze.configuration`` is a package that software developers can use
as a configuration system.  It allows the use of ``YAML`` as a
configuration language.  Application-defined "directives" can be
plugged in to ``repoze.configuration`` using one or more Python
setuptools entry points.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.configuration
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
``repoze.configuration`` is a package that software developers can use
as a configuration system.  It allows the use of ``YAML`` as a
configuration language.  Application-defined "directives" can be
plugged in to ``repoze.configuration`` using one or more Python
setuptools entry points.

This package contains tests for repoze.configuration.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.git20120329.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.git20120329
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20120329
- Version 0.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20110222
- Initial build for Sisyphus


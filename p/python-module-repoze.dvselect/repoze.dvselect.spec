%define oname repoze.dvselect
Name: python-module-%oname
Version: 0.1.2
Release: alt2.1
Summary: Select Deliverance rules / theme based on URI
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.dvselect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze deliverance repoze.urispace

%description
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

%package tests
Summary: Tests for repoze.dvselect
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

This package contains tests for repoze.dvselect.

%package docs
Summary: Documentation for repoze.dvselect
Group: Development/Documentation
BuildArch: noarch

%description docs
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

This package contains documentation for repoze.dvselect.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files docs
%doc docs/*.rst
%doc docs/docroot
%doc docs/etc

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus


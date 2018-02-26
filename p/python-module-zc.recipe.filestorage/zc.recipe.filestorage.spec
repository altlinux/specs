%define oname zc.recipe.filestorage
Name: python-module-%oname
Version: 1.0.1
Release: alt1.1
Summary: ZC Buildout recipe for defining a file-storage
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.filestorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe zc.buildout zope.testing

%description
This recipe can be used to define a file-storage. It creates a ZConfig
file-storage database specification that can be used by other recipes to
generate ZConfig configuration files.

This recipe takes an optional path option. If none is given, it creates
and uses a subdirectory of the buildout parts directory with the same
name as the part.

The recipe records a zconfig option for use by other recipes.

%package tests
Summary: Tests for zc.recipe.filestorage
Group: Development/Python
Requires: %name = %version-%release

%description tests
This recipe can be used to define a file-storage. It creates a ZConfig
file-storage database specification that can be used by other recipes to
generate ZConfig configuration files.

This recipe takes an optional path option. If none is given, it creates
and uses a subdirectory of the buildout parts directory with the same
name as the part.

The recipe records a zconfig option for use by other recipes.

This package contains tests for zc.recipe.filestorage.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus


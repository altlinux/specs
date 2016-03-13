%define oname zc.recipe.filestorage

%def_with python3

Name: python-module-%oname
Version: 1.1.2
Release: alt1.1
Summary: ZC Buildout recipe for defining a file-storage
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.filestorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.recipe zc.buildout
Requires: python-module-zc.recipe

%description
This recipe can be used to define a file-storage. It creates a ZConfig
file-storage database specification that can be used by other recipes to
generate ZConfig configuration files.

This recipe takes an optional path option. If none is given, it creates
and uses a subdirectory of the buildout parts directory with the same
name as the part.

The recipe records a zconfig option for use by other recipes.

%package -n python3-module-%oname
Summary: ZC Buildout recipe for defining a file-storage
Group: Development/Python3
%py3_requires z3c.recipe zc.buildout
Requires: python3-module-zc.recipe

%description -n python3-module-%oname
This recipe can be used to define a file-storage. It creates a ZConfig
file-storage database specification that can be used by other recipes to
generate ZConfig configuration files.

This recipe takes an optional path option. If none is given, it creates
and uses a subdirectory of the buildout parts directory with the same
name as the part.

The recipe records a zconfig option for use by other recipes.

%package -n python3-module-%oname-tests
Summary: Tests for zc.recipe.filestorage
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This recipe can be used to define a file-storage. It creates a ZConfig
file-storage database specification that can be used by other recipes to
generate ZConfig configuration files.

This recipe takes an optional path option. If none is given, it creates
and uses a subdirectory of the buildout parts directory with the same
name as the part.

The recipe records a zconfig option for use by other recipes.

This package contains tests for zc.recipe.filestorage.

%package tests
Summary: Tests for zc.recipe.filestorage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

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

%if_with python3
cp -fR . ../python3
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added requirement on python-module-zc.recipe

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus


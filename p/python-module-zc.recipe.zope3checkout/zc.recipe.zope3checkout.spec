%define oname zc.recipe.zope3checkout
Name: python-module-%oname
Version: 3.5.0
Release: alt1.svn20090727.1.1
Summary: Zope Release and Known-Good-Set (KGS) Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.release/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.zope.org/repos/main/zope.release/trunk
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.recipe zc.buildout zc.lockfile zope.kgs

%description
This package has been developed to support the maintenance of a stable
set of Zope project distributions. It manages the controlled packages
configuration file and supports the generation of buildout configuration
files that can be used by developers.

Another use of this package is to use it for testing new distributions
against the index.

%package tests
Summary: Tests for zc.recipe.zope3checkout
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package has been developed to support the maintenance of a stable
set of Zope project distributions. It manages the controlled packages
configuration file and supports the generation of buildout configuration
files that can be used by developers.

Another use of this package is to use it for testing new distributions
against the index.

This package contains tests for zc.recipe.zope3checkout.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt1.svn20090727.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.svn20090727.1
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.svn20090727
- Initial build for Sisyphus


%define oname zc.zdaemonrecipe
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: ZC Buildout recipe for zdaemon scripts
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zdaemonrecipe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.buildout zc.recipe.egg ZConfig

%description
The zdaemon recipe provides support for generating zdaemon-based run
scripts.

%package tests
Summary: Tests for zc.zdaemonrecipe
Group: Development/Python
Requires: %name = %version-%release
%py_requires zdaemon

%description tests
The zdaemon recipe provides support for generating zdaemon-based run
scripts.

This package contains tests for zc.zdaemonrecipe.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus


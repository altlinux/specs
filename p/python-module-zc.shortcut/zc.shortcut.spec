%define oname zc.shortcut
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Symlinks for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.shortcut/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.displayname

%description
Shortcuts are objects that allow other objects (their target) to appear
to be located in places other than the target's actual location. They
are somewhat like a symbolic link in Unix-like operating systems.

%package tests
Summary: Tests for Symlinks for Zope 3
Group: Development/Python
Requires: %name = %version-%release

%description tests
Shortcuts are objects that allow other objects (their target) to appear
to be located in places other than the target's actual location. They
are somewhat like a symbolic link in Unix-like operating systems.

This package contains tests for Symlinks for Zope 3.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


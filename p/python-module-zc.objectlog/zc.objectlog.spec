%define oname zc.objectlog
Name: python-module-%oname
Version: 0.2.2
Release: alt1
Summary: A customizable log for a single object in Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.objectlog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.copy zope.app.keyreference

%description
The objectlog package provides a customizable log for a single object.
The system was designed to provide information for a visual log of
important object changes and to provide analyzable information for
metrics.

%package tests
Summary: Tests for zc.objectlog
Group: Development/Python
Requires: %name = %version-%release

%description tests
The objectlog package provides a customizable log for a single object.
The system was designed to provide information for a visual log of
important object changes and to provide analyzable information for
metrics.

This package contains tests for zc.objectlog.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Version 0.2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus


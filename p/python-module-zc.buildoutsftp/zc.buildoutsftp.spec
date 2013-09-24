%define oname zc.buildoutsftp
Name: python-module-%oname
Version: 0.11.0
Release: alt1
Summary: Specialized zc.buildout plugin to add sftp support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.buildoutsftp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires paramiko

%description
The zc.buildoutsftp package provides a zc.buildout extension that
provides support for SFTP.

%package tests
Summary: Tests for zc.buildoutsftp
Group: Development/Python
Requires: %name = %EVR

%description tests
The zc.buildoutsftp package provides a zc.buildout extension that
provides support for SFTP.

This package contains tests for zc.buildoutsftp.

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
* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1
- Version 0.11.0

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Version 0.9.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus


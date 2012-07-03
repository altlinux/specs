%define oname zc.zodbactivitylog
Name: python-module-%oname
Version: 0.1.1
Release: alt2.1
Summary: ZODB Activity Monitor that just logs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zodbactivitylog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc

%description
This package provides an activity log that lets you track database
activity.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus


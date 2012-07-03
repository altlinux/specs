%define oname zope.app.debug
Name: python-module-%oname
Version: 3.4.1
Release: alt2.1
Summary: Zope Debug Mode
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.debug/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.publisher zope.app.appsetup zope.app.publication

%description
This package provides a debugger for the Zope publisher. After Zope is
isntantiated, it drops the user into an interactive Python shell where
the full Zope environment and the database root are available.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus


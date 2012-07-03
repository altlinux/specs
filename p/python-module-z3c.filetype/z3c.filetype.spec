%define oname z3c.filetype
Name: python-module-%oname
Version: 1.2.1
Release: alt1.1
Summary: mime filetypes
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.filetype/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.cachedescriptors zope.component zope.contenttype
%py_requires zope.event zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.proxy zope.schema zope.size 

%description
mime filetypes.

%package tests
Summary: Tests for z3c.filetype
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
mime filetypes.

This package contains tests for z3c.filetype.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus


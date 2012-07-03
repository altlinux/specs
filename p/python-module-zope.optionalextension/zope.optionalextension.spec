%define oname zope.optionalextension
Name: python-module-%oname
Version: 1.1
Release: alt3.1
Summary: Optional compilation of C extensions
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.optionalextension/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
This package provides a distutils extension for building optional C
extensions. It is intended for use in projects which have a Python
reference implementation of one or more features, and which can function
without needing any C extensions to be successfully compiled.

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
%exclude %python_sitelibdir/zope/__init__*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added necessary requirements

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Avoid conflict with python-module-zope

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


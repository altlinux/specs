%define oname z3c.javascript
Name: python-module-%oname
Version: 0.2
Release: alt1.svn20080428.1
Summary: Javascript libraries Zope 3
License: BSD-like
Group: Development/Python
Url: http://svn.zope.org/z3c.javascript/?rev=80712#dirlist
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.zope.org/repos/main/z3c.javascript/trunk/
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c

%description
Summary: Javascript libraries Zope 3.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.svn20080428.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20080428
- Initial build for Sisyphus


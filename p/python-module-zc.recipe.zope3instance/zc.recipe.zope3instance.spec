%define oname zc.recipe.zope3instance
Name: python-module-%oname
Version: 1.0.0a1
Release: alt1.git20110408.1.1
Summary: ZC Buildout recipe for defining a Zope 3 instance
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.zope3instance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.zope.org/repos/main/zc.recipe.zope3instance/trunk/
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.recipe zc.buildout zope.testing zc.recipe.egg

%description
This recipe creates a Zope instance that has been extended by a
collection of eggs.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0a1-alt1.git20110408.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a1-alt1.git20110408.1
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a1-alt1.git20110408
- Initial build for Sisyphus


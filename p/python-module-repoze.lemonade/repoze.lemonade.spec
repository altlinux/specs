%define oname repoze.lemonade
Name: python-module-%oname
Version: 0.7.5
Release: alt1.git20110225.1.1
Summary: Library for content-management applications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.lemonade
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.lemonade.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze zope.component zope.interface zope.configuration
%py_requires zope.testing nose

%description
repoze.lemonade is a collection of utilties that make it possible to
create Zope CMF-like applications without requiring any particular
persistence mechanism.

%package tests
Summary: Tests for repoze.lemonade
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.lemonade is a collection of utilties that make it possible to
create Zope CMF-like applications without requiring any particular
persistence mechanism.

This package contains tests for repoze.lemonade.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1.git20110225
- Initial build for Sisyphus


%define oname repoze.bfg.viewgroup
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: An anlologue of Zope 3 "content providers" for repoze.bfg
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.viewgroup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg

%description
repoze.bfg.viewgroup is an extension for repoze.bfg which makes it
possible to make a bfg:viewgroup declaration in ZCML which acts much
like bfg:view inasmuch as it results in a bfg view registration. Unlike
a "normal" bfg:view registration, however, a bfg:viewgroup registration
refers to one or more other bfg views (matching them by name, for
interface, and request type). When a bfg:viewgroup is invoked (either
via traversal or via programmatic view execution), a viewgroup will
return a response which appends all the referenced view renderings
together in a single body.

%package tests
Summary: Tests for repoze.bfg.viewgroup
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.bfg.viewgroup is an extension for repoze.bfg which makes it
possible to make a bfg:viewgroup declaration in ZCML which acts much
like bfg:view inasmuch as it results in a bfg view registration. Unlike
a "normal" bfg:view registration, however, a bfg:viewgroup registration
refers to one or more other bfg views (matching them by name, for
interface, and request type). When a bfg:viewgroup is invoked (either
via traversal or via programmatic view execution), a viewgroup will
return a response which appends all the referenced view renderings
together in a single body.

This package contains tests for repoze.bfg.viewgroup.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus


%define oname repoze.bfg.viewgroup

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt3
Summary: An anlologue of Zope 3 "content providers" for repoze.bfg
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.viewgroup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.bfg zope.schema zope.configuration zope.interface

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

%package -n python3-module-%oname
Summary: An anlologue of Zope 3 "content providers" for repoze.bfg
Group: Development/Python3
%py3_requires repoze.bfg zope.schema zope.configuration zope.interface

%description -n python3-module-%oname
repoze.bfg.viewgroup is an extension for repoze.bfg which makes it
possible to make a bfg:viewgroup declaration in ZCML which acts much
like bfg:view inasmuch as it results in a bfg view registration. Unlike
a "normal" bfg:view registration, however, a bfg:viewgroup registration
refers to one or more other bfg views (matching them by name, for
interface, and request type). When a bfg:viewgroup is invoked (either
via traversal or via programmatic view execution), a viewgroup will
return a response which appends all the referenced view renderings
together in a single body.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.viewgroup
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus


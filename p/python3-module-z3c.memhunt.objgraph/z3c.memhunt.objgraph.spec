%define oname z3c.memhunt.objgraph

%def_without tests

Name: python3-module-%oname
Version: 0.1dev.r118724
Release: alt3

Summary: Help locate and diagnose memory leaks in zope applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.memhunt.objgraph/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires guppy objgraph


%description
z3c.memhunt.objgraph was created to help locate and diagnose memory
leaks in zope applications. This package uses objgraph and guppy to help
with this task.

%if_with tests
%package tests
Summary: Tests for z3c.memhunt.objgraph
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
z3c.memhunt.objgraph was created to help locate and diagnose memory
leaks in zope applications. This package uses objgraph and guppy to help
with this task.

This package contains tests for z3c.memhunt.objgraph.
%endif

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

touch %buildroot%python3_sitelibdir/z3c/memhunt/__init__.py

%files
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*

%if_with tests
%files tests
%python3_sitelibdir/*/*/*/tests.*
%endif


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1dev.r118724-alt3
- porting on python3

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1dev.r118724-alt2.1.1
- (AUTO) subst_x86_64.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1dev.r118724-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1dev.r118724-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1dev.r118724-alt1
- Initial build for Sisyphus


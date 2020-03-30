%define mname dm
%define oname %mname.reuse

Name:       python3-module-%oname
Version:    2.1.1
Release:    alt2

Summary:    Support for object reuse with slight modifications
License:    BSD
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/dm.reuse/

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Utilities to reuse (slightly modified) objects in new contexts.

Currently, there is a single utility: rebindFunction. It allows to reuse
the code of a function while changing name, globals, default arguments,
properties and/or names used.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Utilities to reuse (slightly modified) objects in new contexts.

Currently, there is a single utility: rebindFunction. It allows to reuse
the code of a function while changing name, globals, default arguments,
properties and/or names used.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/tests.*

%files tests
%python3_sitelibdir/%mname/*/tests.*



%changelog
* Mon Mar 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.1-alt2
- Fix build.

* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.1-alt1
- Version updated to 2.1.1
- porting to python3.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt2
- Rebuilded with new setuptools.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


%define _unpackaged_files_terminate_build 1
%define mname collective
%define oname %mname.monkeypatcher

%def_with check

Name: python3-module-%oname
Version: 1.2
Release: alt1
Summary: Support for applying monkey patches late in the startup cycle
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/collective.monkeypatcher/
#Git: https://github.com/plone/collective.monkeypatcher.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.configuration
%endif

%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires zope.component zope.schema zope.interface zope.event
%py3_requires zope.configuration

%description
Sometimes, a monkey patch is a necessary evil.

This package makes it easier to apply a monkey patch during Zope
startup. It uses the ZCML configuration machinery to ensure that patches
are loaded "late" in the startup cycle, so that the original code has
had time to be fully initialised and configured. This is similar to
using the initialize() method in a product's __init__.py, except it does
not require that the package be a full-blown Zope 2 product with a
persistent Control_Panel entry.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.component.testing

%description tests
Sometimes, a monkey patch is a necessary evil.

This package makes it easier to apply a monkey patch during Zope
startup. It uses the ZCML configuration machinery to ensure that patches
are loaded "late" in the startup cycle, so that the original code has
had time to be fully initialised and configured. This is similar to
using the initialize() method in a product's __init__.py, except it does
not require that the package be a full-blown Zope 2 product with a
persistent Control_Panel entry.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 build/lib/%mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%check
sed -i 's|zope-testrunner |zope-testrunner3 |g' tox.ini
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/*/tests
%exclude %python3_sitelibdir/%mname/__init__.py*

%files tests
%python3_sitelibdir/%mname/*/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/__init__.py*

%changelog
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.2-alt1
- NMU: 1.1.3 -> 1.2
- Remove python2 module build
- Rearrange unittests execution

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt1
- Updated to upstream version 1.1.3.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20141210.1
- (AUTO) subst_x86_64.

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141210
- Version 1.1.1

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140826
- Initial build for Sisyphus


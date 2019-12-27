%define _unpackaged_files_terminate_build 1
%define oname z3c.unconfigure

# unittests are unable to pass, so keep disabled
%def_without check

Name: python3-module-%oname
Version: 1.1
Release: alt3
Summary: Disable specific ZCML directives in other package's configuration
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/z3c.unconfigure/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python-tools-2to3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.testing

# TODO: rewiew while unittest fixing
#BuildRequires: python3-module-zope.configuration
#BuildRequires: python3-module-zope.component
#BuildRequires: python3-module-zope.security
#BuildRequires: python3-module-zope.event
%endif

%py3_provides %oname
#%py3_requires z3c zope.configuration zope.component zope.security
#%py3_requires zope.event

%description
This package allows you to disable specific bits of ZCML configuration
that may occur in other packages.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
#%py3_requires zope.testing

%description tests
This package allows you to disable specific bits of ZCML configuration
that may occur in other packages.

This package contains tests for %oname.

%prep
%setup
find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python3 setup.py test
rm -fR build
py.test3

%files
%doc *.txt
%python3_sitelibdir/z3c/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/z3c/*/test*

%files tests
%python3_sitelibdir/z3c/*/test*

%changelog
* Fri Dec 27 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.1-alt3
- NMU: Remove python2 module build
- Rearrange unittests execution

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt2.1
- (AUTO) subst_x86_64.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.1-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


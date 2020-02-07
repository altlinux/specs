%define mname jarn
%define oname %mname.mkrelease

%def_disable check

Name: python3-module-%oname
Version: 3.9
Release: alt2

Summary: Python egg releaser
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jarn.mkrelease/

# https://github.com/Jarn/jarn.mkrelease.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname
Requires: python3-module-%mname = %EVR


%description
mkrelease is a no-frills Python egg releaser. It is designed to take the
cumber out of building and distributing Python eggs.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
mkrelease is a no-frills Python egg releaser. It is designed to take the
cumber out of building and distributing Python eggs.

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

install -p -m644 %mname/__init__.py \
    %buildroot%python3_sitelibdir/%mname/

%check
%__python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/test*
%exclude %python3_sitelibdir/%mname/__init__.py*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/__init__.py*

%files tests
%python3_sitelibdir/%mname/*/test*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.9-alt2
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.9-alt1.git20131125.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9-alt1.git20131125.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9-alt1.git20131125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.9-alt1.git20131125.1
- NMU: Use buildreq for BR.

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt1.git20131125
- Initial build for Sisyphus


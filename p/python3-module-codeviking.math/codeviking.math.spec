%define mname codeviking
%define oname %mname.math
Name: python3-module-%oname
Version: 0.18.1
Release: alt1.1
Summary: Function and method call math
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/CodeViking.math/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-pytest

%py3_provides %oname

%description
A collection of mathematical utility functions.

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
PYTHONPATH=$(pwd) py.test3

%files
%doc *.rst
%python3_sitelibdir/%mname/math
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/CodeViking.math-*.pth

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.1-alt1
- Updated to upstream version 0.18.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus


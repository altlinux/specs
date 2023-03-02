%define mname gocept
%define oname %mname.testing

%def_with check

Name: python3-module-%oname
Version: 3.0
Release: alt1

Summary: A collection of test helpers, additional assertions, and the like
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/gocept.testing/
VCS: https://github.com/gocept/gocept.testing

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
This package collects various helpers for writing tests.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%tox_check

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/%mname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%mname/*/tests


%changelog
* Wed Mar 01 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- new version 3.0

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.1-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1
- (AUTO) subst_x86_64.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Initial build for Sisyphus


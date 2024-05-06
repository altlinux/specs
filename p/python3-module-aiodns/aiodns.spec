Name: python3-module-aiodns
Version: 3.2.0
Release: alt1

Summary: Simple DNS resolver for asyncio
License: MIT
Group: Development/Python
Url: https://github.com/saghul/aiodns

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pycares)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aiodns
%python3_sitelibdir/aiodns-%version.dist-info

%check
#online tests
%pyproject_run -- python3 tests.py ||:

%changelog
* Fri May 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.0-alt1
- 3.2.0 released

* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt2
- Drop python2 support.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1
- Drop tests (did not run actually)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20141207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20141207.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141207
- Initial build for Sisyphus


%define sname retrying

Name: python3-module-%sname
Version: 1.4.2
Release: alt1
Summary: Retrying library
Group: Development/Python3
License: Apache-2.0
URL:  https://pypi.org/project/retrying
VCS:  https://github.com/groodt/retrying
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Simplify the task of adding retry behavior to just about anything.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test_retrying.py

%files
%doc README.md LICENSE.txt HISTORY.rst
%python3_sitelibdir/%sname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%sname-%version.dist-info

%changelog
* Sun Aug 03 2025 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Build new version.
- Build with check.

* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3.3-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.3-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- initial build

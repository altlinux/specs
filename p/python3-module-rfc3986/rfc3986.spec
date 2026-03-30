%define _unpackaged_files_terminate_build 1
%define pypi_name rfc3986
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1.1
Summary: Validating URI References per RFC 3986
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/rfc3986/
Vcs: https://github.com/python-hyper/rfc3986
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-attrs
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov

BuildRequires: python3-module-idna
%endif

%description
A Python implementation of RFC 3986 including validation and authority parsing.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1.1
- Demodernized packaging.

* Wed May 08 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.4.0 -> 2.0.0.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1.1
- NMU: moved on modern pyproject macros.

* Tue Sep 29 2020 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.1 -> 1.4.0.
- Stopped Python2 package build.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1.3.1-alt2
- Fixed testing against Pytest 5.

* Sat Apr 27 2019 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 0.4.1 -> 1.3.1.
- Enabled testing.

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial package

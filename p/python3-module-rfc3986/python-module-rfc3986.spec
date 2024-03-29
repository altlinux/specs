%define _unpackaged_files_terminate_build 1
%define pypi_name rfc3986

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1.1
Summary: Validating URI References per RFC 3986
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.python.org/pypi/rfc3986
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(idna)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
%endif

%description
A Python implementation of RFC 3986 including validation and authority parsing.

%py3_requires idna

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst LICENSE
%python3_sitelibdir/rfc3986/
%python3_sitelibdir/rfc3986-%version.dist-info/

%changelog
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

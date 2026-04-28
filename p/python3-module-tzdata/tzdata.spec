%define  oname tzdata

%def_with check

Name:    python3-module-%oname
Version: 2026.2
Release: alt1

Summary: Python package wrapping the IANA time zone database

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/tzdata

# https://github.com/python/tzdata
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
This is a Python package containing zic-compiled binaries for the IANA time zone
database. It is intended to be a fallback for systems that do not have
system time zone data installed (or don't have it installed in a
standard location), as a part of PEP 615

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Apr 28 2026 Alexander Burmatov <thatman@altlinux.org> 2026.2-alt1
- Updated to 2026.2.

* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 2026.1-alt1
- Updated to 2026.1.

* Tue Feb 24 2026 Stanislav Levin <slev@altlinux.org> 2025.3-alt2
- NMU: dropped dependency on incorporated pytest-subtests.

* Mon Jan 12 2026 Alexander Burmatov <thatman@altlinux.org> 2025.3-alt1
- Updated to 2025.3.

* Tue Mar 25 2025 Grigory Ustinov <grenka@altlinux.org> 2025.2-alt1
- Automatically updated to 2025.2.

* Thu Jan 23 2025 Grigory Ustinov <grenka@altlinux.org> 2025.1-alt1
- Automatically updated to 2025.1.

* Wed Oct 02 2024 Grigory Ustinov <grenka@altlinux.org> 2024.2-alt1
- Automatically updated to 2024.2.

* Mon Feb 26 2024 Grigory Ustinov <grenka@altlinux.org> 2024.1-alt1
- Automatically updated to 2024.1.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 2023.4-alt1
- Automatically updated to 2023.4.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 2023.3-alt1
- Automatically updated to 2023.3.

* Thu Dec 01 2022 Grigory Ustinov <grenka@altlinux.org> 2022.7-alt1
- Automatically updated to 2022.7.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 2022.6-alt1
- Initial build for Sisyphus.

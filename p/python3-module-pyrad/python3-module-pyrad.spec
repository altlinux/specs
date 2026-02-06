%define  modulename pyrad

%def_with check

Name:    python3-module-%modulename
Version: 2.5.4
Release: alt1

Summary: Python RADIUS Implementation
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/pyradius/pyrad

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-six
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
pyrad is an implementation of a RADIUS client as described in RFC2865. It takes
care of all the details like building RADIUS packets, sending them and
decoding responses.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}
%doc *.rst

%changelog
* Fri Feb 06 2026 Grigory Ustinov <grenka@altlinux.org> 2.5.4-alt1
- Automatically updated to 2.5.4.

* Thu Jan 29 2026 Grigory Ustinov <grenka@altlinux.org> 2.5.2-alt1
- Automatically updated to 2.5.2.

* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 2.4-alt5
- Fixed FTBFS (poetry-core 2.0).

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 2.4-alt4
- Fixed FTBFS.

* Wed Oct 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.4-alt3
- Fixed BuildRequires.

* Tue Apr 04 2023 Anton Vyatkin <toni@altlinux.org> 2.4-alt2
- (NMU) Fix BuildRequires.

* Thu Nov 26 2020 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1
- Automatically updated to 2.4.

* Fri May 29 2020 Grigory Ustinov <grenka@altlinux.org> 2.3-alt1
- Initial build for Sisyphus.

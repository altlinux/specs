%define  modulename pyrad

%def_with check

Name:    python3-module-%modulename
Version: 2.4
Release: alt2

Summary: Python RADIUS Implementation
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/pyradius/pyrad

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
%if_with check
BuildRequires: python3-module-netaddr
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
pyrad is an implementation of a RADIUS client as described in RFC2865. It takes
care of all the details like building RADIUS packets, sending them and
decoding responses.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}
%exclude %python3_sitelibdir/example
%doc *.rst

%changelog
* Tue Apr 04 2023 Anton Vyatkin <toni@altlinux.org> 2.4-alt2
- (NMU) Fix BuildRequires.

* Thu Nov 26 2020 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1
- Automatically updated to 2.4.

* Fri May 29 2020 Grigory Ustinov <grenka@altlinux.org> 2.3-alt1
- Initial build for Sisyphus.

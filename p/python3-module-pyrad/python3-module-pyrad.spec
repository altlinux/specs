%define  modulename pyrad

Name:    python3-module-%modulename
Version: 2.4
Release: alt1

Summary: Python RADIUS Implementation
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/pyradius/pyrad

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-nose python3-module-netaddr python3-module-six

BuildArch: noarch

Source:  %modulename-%version.tar

%description
pyrad is an implementation of a RADIUS client as described in RFC2865. It takes
care of all the details like building RADIUS packets, sending them and
decoding responses.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%check
%{__python3} setup.py test

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Nov 26 2020 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1
- Automatically updated to 2.4.

* Fri May 29 2020 Grigory Ustinov <grenka@altlinux.org> 2.3-alt1
- Initial build for Sisyphus.

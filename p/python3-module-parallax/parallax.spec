%global pypi_name parallax

Name: python3-module-%pypi_name
Version: 1.0.5
Release: alt1
Summary: Execute commands and copy files over SSH to multiple machines at once

Group: Development/Python3
License: ASL 2.0
URL: https://pypi.org/project/parallax/
Source: %pypi_name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-oslosphinx >= 2.5.0
BuildRequires: python3-module-oslo.config >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-six >= 1.9.0

%description
Execute commands and copy files over SSH to multiple machines at once.

%prep
%setup -n %pypi_name-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md COPYING
%_bindir/parallax-askpass
%python3_sitelibdir/*

%changelog
* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1
- Build new version.
- Build without python2.

* Mon Sep 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build

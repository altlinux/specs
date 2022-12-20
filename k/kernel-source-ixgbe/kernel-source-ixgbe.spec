%define module_name ixgbe
%define module_version 5.18.6

%define module_source %module_name.tar

Name: kernel-source-%module_name
Version: %module_version
Release: alt1

Group: Development/Kernel
Summary: Linux %module_name modules sources
License: GPL-2
URL: http://www.intel.com/network/connectivity/products/server_adapters.htm
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: rpm-build-kernel

%description
%module_name modules sources for ixgbe Linux kernel driver

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 %name-%version

%files
%_usrsrc/*

%changelog
* Tue Dec 20 2022 Alexei Takaseev <taf@altlinux.org> 5.18.6-alt1
- 5.18.6

* Mon Oct 17 2022 Alexei Takaseev <taf@altlinux.org> 5.17.1-alt1
- 5.17.1

* Fri Aug 05 2022 Alexei Takaseev <taf@altlinux.org> 5.16.5-alt1
- 5.16.5

* Mon May 23 2022 Alexei Takaseev <taf@altlinux.org> 5.15.2-alt1
- 5.15.2

* Mon Mar 14 2022 Alexei Takaseev <taf@altlinux.org> 5.14.6-alt1
- 5.14.6

* Wed Oct 20 2021 Alexei Takaseev <taf@altlinux.org> 5.13.4-alt1
- 5.13.4

* Mon Aug 23 2021 Alexei Takaseev <taf@altlinux.org> 5.12.5-alt2
- Change BR: kernel-build-tools -> rpm-build-kernel

* Wed Jul 14 2021 Alexei Takaseev <taf@altlinux.org> 5.12.5-alt1
- 5.12.5

* Tue Mar 09 2021 Alexei Takaseev <taf@altlinux.org> 5.11.3-alt1
- 5.11.3

* Mon Feb 08 2021 Alexei Takaseev <taf@altlinux.org> 5.10.2-alt1
- 5.10.2

* Thu Oct 01 2020 Alexei Takaseev <taf@altlinux.org> 5.9.4-alt1
- 5.9.4

* Wed Aug 19 2020 Alexei Takaseev <taf@altlinux.org> 5.8.1-alt1
- 5.8.1

* Thu May 21 2020 Alexei Takaseev <taf@altlinux.org> 5.7.1-alt1
- 5.7.1
- Added support for 5.6 kernel version

* Wed May 13 2020 Alexei Takaseev <taf@altlinux.org> 5.6.4-alt1
- 5.6.4
- Fix build with kernel >= 5.4

* Sat Nov 16 2019 Alexei Takaseev <taf@altlinux.org> 5.6.3-alt1
- initial build

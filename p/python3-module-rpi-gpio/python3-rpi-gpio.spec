%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var

%global __provides_exclude_from ^(%python3_sitelibdir/.*\\.so)$

Name:           python3-module-rpi-gpio
Version:        0.7.1
Release:        alt1
Group: Development/Python
Summary:        Class to control the GPIO on a Raspberry Pi

License:        MIT
URL:            https://sourceforge.net/projects/raspberry-gpio-python/
Source:        %name-%version.tar
Provides: python3-module-RPi.GPIO = %EVR
Obsoletes: python3-module-RPi.GPIO < %EVR

ExclusiveArch:  %{arm} aarch64

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Python library for GPIO access on a Raspberry Pi.

%prep
%setup

%build
CFLAGS="%optflags -fcommon"
%python3_build

%install
%python3_install

%files
%doc README.txt
%doc --no-dereference LICENCE.txt
%python3_sitelibdir/RPi*

%changelog
* Tue Apr 08 2025 Artem Semenov <savoptik@altlinux.org> 0.7.1-alt1
- Update to 0.7.1

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_3
- update to new release by fcimport

* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2
- update to new release by fcimport

* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.5-alt1_1
- new version

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1a-alt1_2
- update to new release by fcimport

* Tue Jan 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1a-alt1_1
- initial fc import


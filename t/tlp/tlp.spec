Name: tlp
Version: 1.5.0
Release: alt2

Summary: Optimize laptop battery life

License: GPLv2+
Group: System/Configuration/Hardware
Url: https://linrunner.de/tlp

# Source-url: https://github.com/linrunner/TLP/archive/%version.tar.gz#/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: rpm-build-perl
BuildRequires: libsystemd-devel libudev-devel
BuildRequires: systemd systemd-analyze systemd-homed systemd-networkd
#BuildRequires: udev-rules-portable udev-rules-sysvinit
BuildRequires: libappstream-glib libappstream-glib-gir

#The following requires are not detected:
Requires: ethtool
Requires: hdparm
Requires: iw
Requires: rfkill
Requires: systemd systemd-analyze systemd-homed systemd-networkd
#Requires: udev-rules-portable udev-rules-sysvinit
Requires: udev
Requires: usbutils
Requires: pciutils
Requires: cpupower linux-tools

#Note: Conflicts with laptop-mode-tools
#Makes sure laptop_mode isn't being used:
BuildArch: noarch

%description
TLP is a feature-rich command-line utility, saving laptop battery power
without the need to delve deeper into technical details.

TLPa.'s default settings are already optimized for battery life and implement
Powertopa.'s recommendations out of the box. Moreover TLP is highly
customizable to fulfil specific user requirements.

Settings are organized into two profiles, allowing to adjust between
savings and performance independently for battery (BAT) and AC operation.
In addition TLP can enable or disable Bluetooth, NFC, Wi-Fi and WWAN radio
devices on boot.

For ThinkPads and selected other laptops it provides a unified way
to configure charge thresholds and recalibrate the battery.

%package rdw
Group: System/Configuration/Hardware
Summary: Radio device wizard for TLP
Requires: NetworkManager-daemon >= 1.20
Requires: %name = %version-%release
BuildArch: noarch

%description rdw
Radio device wizard is an add-on to TLP. It provides event based
switching of bluetooth, NFC, Wi-Fi and WWAN radio devices on:
 - network connect/disconnect
 - dock/undock

%prep
%setup

%build
%make_build

%install
%makeinstall_std \
  TLP_SDSL=%_unitdir/../system-sleep \
  TLP_NMDSP=%_prefix/lib/NetworkManager/dispatcher.d \
  TLP_NO_INIT=1 \
  TLP_WITH_ELOGIND=0 \
  TLP_SYSD=%_unitdir \
  TLP_ULIB=%_udevrulesdir/..
#Install manpages:
%make_install install-man DESTDIR=%buildroot
%make_install install-man-rdw DESTDIR=%buildroot

%check
appstream-util validate-relax --nonet \
%buildroot/%_datadir/metainfo/*.xml

%files
%config(noreplace) %_sysconfdir/tlp.conf
%config(noreplace) %_sysconfdir/tlp.d
%doc --no-dereference LICENSE
%doc COPYING README.rst changelog
%_bindir/*
%exclude %_bindir/tlp-rdw
%_sbindir/*
%_mandir/man*/*
%exclude %_mandir/man*/tlp-rdw*
%_datadir/tlp
%_udevrulesdir/85-tlp.rules
%_udevrulesdir/../tlp-usb-udev
%_datadir/bash-completion/completions/*
%exclude %_datadir/bash-completion/completions/tlp-rdw
%_unitdir/*.service
%_unitdir/../system-sleep
%_datadir/metainfo/*.metainfo.xml
%_sharedstatedir/tlp

%files rdw
%doc COPYING README.rst changelog
%_bindir/tlp-rdw
%_mandir/man*/tlp-rdw*
%_prefix/lib/NetworkManager/dispatcher.d/99tlp-rdw-nm
%_udevrulesdir/85-tlp-rdw.rules
%_udevrulesdir/../tlp-rdw-udev
%_datadir/bash-completion/completions/tlp-rdw

%post
%post_service tlp
if [ $1 -eq 2 ] ; then
    systemctl unmask systemd-rfkill.service
    systemctl unmask power-profiles-daemon.service
fi

%preun
%preun_service tlp
%changelog
* Fri Apr 28 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- manual build for Sisyphus

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_5
- update to new release by fcimport

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_4
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_3
- update to new release by fcimport

* Thu Jan 20 2022 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_2
- update to new release by fcimport

* Wed Oct 13 2021 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt1_2
- update to new release by fcimport

* Mon Sep 20 2021 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt1_0.1.beta.1
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.3.1-alt2_5
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.3.1-alt2_4
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_2
- update to new release by fcimport

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_2
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- update to new release by fcimport

* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- update to new release by fcimport

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- update to new release by fcimport

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- update to new release by fcimport

* Wed Oct 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- new version


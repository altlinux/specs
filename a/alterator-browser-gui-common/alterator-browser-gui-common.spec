
%define alterator_cfg %_sysconfdir/alterator

Name: alterator-browser-gui-common
Version: 0.1
Release: alt2

Summary: Common files for alterator GUI browser
License: GPL
Group: System/Configuration/Other
Packager: Sergey V Turchin <zerg at altlinux dot org>

BuildArch: noarch

%description
Common files for alterator GUI browser

%install
mkdir -p %buildroot/%alterator_cfg
ln -s /dev/null %buildroot/%alterator_cfg/design-browser-qt
mkdir -p %buildroot/%_datadir/%name/design
ln -s %alterator_cfg/design-browser-qt %buildroot/%_datadir/%name/design/current

%files
%ghost %config %alterator_cfg/design-browser-qt
%_datadir/%name/

%changelog
* Fri Jun 14 2019 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt2
- don't use ubt macro

* Fri Apr 14 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build

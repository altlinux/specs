
%define alterator_cfg %_sysconfdir/alterator

Name: alterator-browser-gui-common
Version: 0.1
Release: alt1%ubt

Summary: Common files for alterator GUI browser
License: GPL
Group: System/Configuration/Other
Packager: Sergey V Turchin <zerg at altlinux dot org>

BuildArch: noarch

BuildRequires(pre): rpm-build-ubt

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
* Fri Apr 14 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1%ubt
- initial build

Name: theme-kworkstation
Version: 0.2.2
Release: alt3

Summary: Workstation K theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: %name-%version.tar

BuildArch: noarch

Requires(post,preun): alternatives >= 0.2
Requires: kde-theme-alt
Requires: icon-theme-altos

%description
Workstation K theme.

%prep
%setup

%install
mkdir -p %buildroot/%_datadir/plasma/desktoptheme/
cp -ar desktoptheme/altos-* %buildroot/%_datadir/plasma/desktoptheme/

# add icons alternatives
mkdir -p %buildroot/%_sysconfdir/alternatives/packages.d/
> %buildroot/%_sysconfdir/alternatives/packages.d/%name
for n in alt-distro-logo alterator alt-main-menu ; do
cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_iconsdir/altos/apps/16/${n}.svg      %_datadir/plasma/desktoptheme/altos-light/icons/${n}.svg 10
%_iconsdir/altos-dark/apps/16/${n}.svg %_datadir/plasma/desktoptheme/altos-dark/icons/${n}.svg  10
__EOF__
done

%files
%config %_sysconfdir/alternatives/packages.d/%name
%_datadir/plasma/desktoptheme/altos-*/icons/*alt*.*

%changelog
* Tue Mar 17 2026 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt3
- fix package description

* Thu Mar 12 2026 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt2
- fix package summary

* Wed Mar 11 2026 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt1
- update alt-main-menu icon

* Tue Mar 10 2026 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- update alt-main-menu icon

* Mon Sep 22 2025 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- update alterator and alt-main-menu icons

* Mon Dec 23 2024 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build

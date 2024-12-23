Name: theme-kworkstation
Version: 0.1
Release: alt1

Summary: Workstatio K theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: %name-%version.tar

BuildArch: noarch

Requires(post,preun): alternatives >= 0.2
Requires: kde-theme-alt
Requires: icon-theme-altos

%description
Workstatio K theme.

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
* Mon Dec 23 2024 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build

Name: icon-theme-alt-workstation
Version: 0.1
Release: alt1

Summary: ALT Workstation icon theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: icon-theme-alt-workstation-%version.tar

BuildArch: noarch

Requires(post,preun): alternatives >= 0.2
Obsoletes: alt-workstation-icon-theme <= %EVR

%description
ALT Workstation icon for Alterator and other ALT app icons.

%prep
%setup

%install
mkdir -p %buildroot/%_datadir/alt/desktoptheme/
cp -ar desktoptheme/altos-icons %buildroot/%_datadir/alt/desktoptheme/

# add icons alternatives
mkdir -p %buildroot/%_sysconfdir/alternatives/packages.d/
> %buildroot/%_sysconfdir/alternatives/packages.d/%name

# for scalable
for n in alt-distro-logo alterator alt-main-menu ; do
cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_iconsdir/hicolor/scalable/apps/${n}.svg	%_datadir/alt/desktoptheme/altos-icons/icons/${n}.svg 10
__EOF__
done
cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_iconsdir/hicolor/scalable/apps/altlinux.svg	%_datadir/alt/desktoptheme/altos-icons/icons/alt-distro-logo.svg 10
__EOF__

%files
%config %_sysconfdir/alternatives/packages.d/%name
%_datadir/alt/desktoptheme/altos-icons/icons/*.svg
%_datadir/alt/desktoptheme/altos-icons/icons/*.png

%changelog
* Mon Jan 27 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1-alt1
- Initial build

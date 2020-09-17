Name: system-logo
Version: 10.0
Release: alt1

Summary: Generic System Logo
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: http://altlinux.org/

Requires(post,preun): alternatives >= 0.2
Requires: menu-icons-default

Source: %name-%version.tar

BuildArch: noarch

%description
System logo generic provider to show how to package branding.

%prep

%install
# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_pixmapsdir/system-logo.png       %_iconsdir/hicolor/128x128/apps/basealt.png      0
__EOF__

mkdir -p %buildroot/%_pixmapsdir/
ln -s /dev/null %buildroot/%_pixmapsdir/system-logo.png

%files
%ghost %_pixmapsdir/system-logo.png
%_sysconfdir/alternatives/packages.d/%name

%changelog
* Wed Sep 16 2020 Sergey V Turchin <zerg@altlinux.org> 10.0-alt1
- initial build

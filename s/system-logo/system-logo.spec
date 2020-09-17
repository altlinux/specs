Name: system-logo
Version: 10.1
Release: alt1

Summary: Generic System Logo
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: http://altlinux.org/

Requires(post,preun): alternatives >= 0.2

Source: %name-%version.tar

BuildArch: noarch

%description
System logo generic provider to show how to package branding.

%prep

%install
# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_sysconfdir/system-logo.png       %_pixmapsdir/system-logo-sample.png      0
__EOF__

mkdir -p %buildroot/%_pixmapsdir/
ln -s `relative %_sysconfdir/system-logo.png %_pixmapsdir/system-logo.png` %buildroot/%_pixmapsdir/system-logo.png

mkdir -p %buildroot/%_sysconfdir/
ln -s /dev/null %buildroot/%_sysconfdir/system-logo.png

%files
%ghost %_sysconfdir/system-logo.png
%_pixmapsdir/system-logo.png
%_sysconfdir/alternatives/packages.d/%name

%changelog
* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 10.1-alt1
- move alternative symlink to /etc/
- provide logo sample

* Wed Sep 16 2020 Sergey V Turchin <zerg@altlinux.org> 10.0-alt1
- initial build

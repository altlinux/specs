
%define drvpre_dir /usr/libexec/X11/drvpre.d

Name: x11presetdrv
Version: 1.0.0
Release: alt1

Group: System/Configuration/Hardware
Summary: X Window System drivers preparing utility
License: GPL
URL: http://www.altlinux.ru

BuildArch: noarch

Source: %name-%version.tar.bz2

BuildRequires: gcc

%description
Utility for initial X Window System drivers preparing

%prep
%setup -q


%build


%install
mkdir -p -m 0755 %buildroot/%drvpre_dir

mkdir -p -m 0755 %buildroot/%_sbindir
install -m 0755 %name %buildroot/%_sbindir/%name
sed -i "s|@PRESET_DIR@|%drvpre_dir|g" %buildroot/%_sbindir/%name

mkdir -p -m 0755 %buildroot/%_sysconfdir/rc.d/init.d
install -m 0755 %name.init %buildroot/%_sysconfdir/rc.d/init.d/%name


%post
%post_service %name
%preun
%preun_service %name


%files
%doc AUTHORS
%dir %drvpre_dir
%_sbindir/%name
%_sysconfdir/rc.d/init.d/%name

%changelog
* Fri Apr 04 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- don't check for drvpre.d catalog twice

* Fri Jan 19 2007 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial release

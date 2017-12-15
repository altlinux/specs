%define drvpre_dir /usr/libexec/X11/drvpre.d

Name: x11presetdrv
Version: 2.1.2
Release: alt2%ubt

Group: System/Configuration/Hardware
Summary: X Window System drivers preparing utility
License: GPL
URL: http://www.altlinux.ru

BuildArch: noarch

BuildRequires(pre): rpm-build-ubt
Source: %name-%version.tar.bz2

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

mkdir -p -m 0755 %buildroot/%_sysconfdir/rc.d/init.d

mkdir -p -m 0755 %buildroot/%_unitdir
install -m 0644 %name.service %buildroot/%_unitdir/

mkdir -p -m 0755 %buildroot/%_unitdir/graphical.target.wants
ln -s `relative %_unitdir/%name.service %_unitdir/graphical.target.wants/%name.service` %buildroot/%_unitdir/graphical.target.wants/%name.service

mkdir -p -m 0755 %buildroot/%_presetdir
cat >%buildroot/%_presetdir/33-%name.preset <<__EOF__
# Need to be enabled by default
enable %name.service
__EOF__

%post
%post_service %name
%preun
%preun_service %name


%files
%doc AUTHORS
%dir %drvpre_dir
%_sbindir/%name
%_sysconfdir/rc.d/init.d/%name
%_unitdir/%name.service
%_unitdir/graphical.target.wants/%name.service
%_presetdir/??-%name.preset

%changelog
* Fri Dec 15 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.2-alt2%ubt
- turn on systemd service by default again

* Fri Feb 13 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- turn on systemd service by default

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- update systemd service conflicts

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- update service description

* Thu Apr 04 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- add systemd service file (ALT#28660)

* Fri Apr 04 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- don't check for drvpre.d catalog twice

* Fri Jan 19 2007 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial release

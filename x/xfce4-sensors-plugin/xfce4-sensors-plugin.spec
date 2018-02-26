Name: xfce4-sensors-plugin
Version: 1.2.5
Release: alt1

Summary: Sensors plugin for XFce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel
BuildRequires: hddtemp intltool libsensors3-devel libnotify-devel

Requires: xfce4-panel >= 4.8 hddtemp lm_sensors3

%description
%name

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-hddtemp=yes \
    --disable-netcat \
    --enable-libsensors=yes \
    --enable-procacpi \
    --enable-sysfsacpi \
    --enable-notification \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc NEWS AUTHORS
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_libexecdir/xfce4/panel-plugins/%name
%_libdir/xfce4/modules/libxfce4sensors.so*
%_liconsdir/*.png
%_datadir/xfce4/panel/plugins/*.desktop
%exclude %_pkgconfigdir/*.pc
%exclude %_libdir/xfce4/modules/libxfce4sensors.la

%changelog
* Thu May 31 2012 Mikhail Efremov <sem@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt2
- Rebuild with xfce4-panel-4.9.

* Fri Oct 14 2011 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1
- Drop obsoleted patches.
- Updated to 1.2.3.

* Tue Feb 08 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Drop xfce4-sensors-plugin-asneeded.patch.
- Port to xfce4-panel 4.7.
- Add xfce4-sensors-plugin-1.0.0-fedora-dso.patch.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 1.0.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.10.99.6-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.10.99.3-alt1
- new version
- add watch file

* Mon Dec 18 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.10.0-alt1
- new version

* Sun Sep 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.7.0-alt1
-  new version

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.1-alt1
- First build for Sisyphus.


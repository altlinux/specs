Name: xfce4-radio-plugin
Version: 0.5.1
Release: alt3

Summary: V4l radio plugin for XFce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel >= 4.8

%description
This is an Xfce panel plugin which allows you to control your V4l radio
device. You can turn your radio on/off, tune it to some frequency and
manage station presets.

%prep
%setup
%patch -p1

%build
touch ChangeLog
%xfce4reconf
%configure \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt2
- Rebuild with xfce4-panel-4.9.

* Mon Oct 17 2011 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Tue Feb 08 2011 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.gz -> tar.
- Drop watch file.
- Updated to 0.4.4.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.1-alt1
- new version
- add watch file

* Tue Jan 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- First build


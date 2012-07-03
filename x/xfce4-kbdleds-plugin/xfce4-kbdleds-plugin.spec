%define git_date .git20111014

Name: xfce4-kbdleds-plugin
Version: 0.0.6
Release: alt3%git_date

Summary: This plugin shows the state of your keyboard LEDs
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel

Requires: xfce4-panel >= 4.8

%description
This plugin shows the state of your keyboard LEDs: Caps, Scroll and
Num Lock in Xfce panel.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt3.git20111014
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt2.git20111014
- Rebuild with xfce4-panel-4.9.

* Fri Oct 14 2011 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt1.git20111014
- Initial build


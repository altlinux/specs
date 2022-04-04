Name: xfce4-kbdleds-plugin
Version: 0.2.5
Release: alt1

Summary: This plugin shows the state of your keyboard LEDs
License: GPLv2+
Group: Graphical desktop/XFce
Vcs: https://github.com/oco2000/xfce4-kbdleds-plugin.git
Url: https://github.com/oco2000/xfce4-kbdleds-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.12 libxfce4ui-gtk3-devel >= 4.12 libxfce4util-devel

Requires: xfce4-panel >= 4.12

%define _unpackaged_files_terminate_build 1

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
%doc README.md AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Apr 04 2022 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Use %%_unpackaged_files_terminate_build.
- Don't use rpm-build-licenses.
- Added Vcs tag.
- Updated Url tag.
- Updated to 0.2.5 (resurrected for Sisyphus).

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt4.git20111014
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt3.git20111014
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt2.git20111014
- Rebuild with xfce4-panel-4.9.

* Fri Oct 14 2011 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt1.git20111014
- Initial build


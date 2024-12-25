Name: xfce4-mpc-plugin
Version: 0.5.5
Release: alt1

Summary: MPD Client Plugin
License: ISC
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-mpc-plugin/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-mpc-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.16.0 libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libmpd-devel

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
This is a simple client plugin for Music Player Daemon.

Features :
- send Play/Stop/Next/Previous command to MPD.
- decrease/increase volume using the mouse wheel.
- show the current volume, status and title as a tooltip when passing
  the mouse over the plugin.
- show a simple playlist window upon middle-click, permitting to select
  a track to play
- configurable MPD host/port/password.
- toggles repeat/random features in the right-click menu.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS COPYING
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Thu Dec 26 2024 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt1
- Updated description.
- Updated to 0.5.5.

* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt2
- Fixed build: added intltool to BR.

* Tue May 02 2023 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1
- Enabled build on aarch64.
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated Url tag.
- Updated to 0.5.3.

* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Tue Sep 04 2018 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2
- Don't build the package on aarch64.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.5.0.

* Fri Feb 17 2012 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated translations from upstream git.
- Initial build.

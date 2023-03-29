%define _libexecdir /usr/libexec
%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d

Name: xorg-xwayland
Version: 23.1.1
Release: alt1
Epoch: 2
License: MIT
Summary: Wayland X server
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: xorg-server-common

BuildRequires: meson egl-wayland-devel libEGL-devel libGL-devel libXaw-devel libXdmcp-devel libXfont-devel libXfont2-devel libXpm-devel
BuildRequires: libXrender-devel libXres-devel libXtst-devel libXv-devel libaudit-devel libdbus-devel libdmx-devel libdrm-devel libepoxy-devel
BuildRequires: libgbm-devel libpciaccess-devel libpixman-devel libselinux-devel libssl-devel libtirpc-devel libudev-devel libwayland-client-devel
BuildRequires: libxcb-render-util-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxkbfile-devel
BuildRequires: libxcvt-devel libxshmfence-devel wayland-protocols xorg-xtrans-devel xorg-proto-devel libgcrypt-devel xkbcomp rendercheck 

%description
Xwayland is an X server for running X clients under Wayland

%package devel
Summary: Development package
Group: Development/C

%description devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland

%prep
%setup -q
%patch -p1

%build
%meson \
	-Dxwayland_eglstream=true \
	-Ddefault_font_path=%_deffontdir \
	-Dxkb_output_dir=%_localstatedir/xkb \
	-Dxcsecurity=true \
	-Dglamor=true \
	-Ddri3=true

%meson_build

%install
%meson_install

%files
%_bindir/Xwayland
%_desktopdir/org.freedesktop.Xwayland.desktop
%_man1dir/Xwayland.1*

%files devel
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 29 2023 Valery Inozemtsev <shrek@altlinux.ru> 2:23.1.1-alt1
- 23.1.1

* Thu Mar 23 2023 Valery Inozemtsev <shrek@altlinux.ru> 2:23.1.0-alt1
- 23.1.0

* Tue Feb 07 2023 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.8-alt1
- 22.1.8

* Fri Jan 20 2023 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.7-alt2
- glamor: Don't initialize on softpipe (closes: #44985)

* Mon Dec 19 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.7-alt1
- 22.1.7

* Wed Dec 14 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.6-alt1
- 22.1.6

* Wed Nov 02 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.5-alt1
- 22.1.5

* Thu Oct 20 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.4-alt1
- 22.1.4

* Wed Jul 13 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.3-alt1
- 22.1.3

* Thu May 26 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.2-alt1
- 22.1.2

* Thu Mar 31 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.1-alt1
- 22.1.1

* Thu Feb 17 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.1.0-alt1
- 22.1.0

* Fri Jan 21 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:22.0.99.901-alt1
- 22.1.0 RC1

* Tue Dec 14 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:21.1.4-alt1
- 21.1.4

* Tue Nov 09 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:21.1.3-alt1
- 21.1.3

* Fri Jul 09 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:21.1.2-alt1
- 21.1.2

* Wed Apr 14 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:21.1.1-alt1
- 21.1.1

* Fri Mar 19 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:21.1.0-alt1
- initial release


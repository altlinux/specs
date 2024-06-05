%define ver_major 13.0
%define api_ver_major 13
%define api_ver %api_ver_major
%define clientsdir %_libdir/%name/clients
%define soname 1
%define exec_soname 0

# Weston backend: DRM/KMS
%def_enable backend_drm

# DRM/KMS backend support for VA-API screencasting
%def_enable backend_drm_screencast_vaapi

# Weston backend: headless (testing)
%def_enable backend_headless

# Weston backend: RDP remote screensharing
%def_enable backend_rdp

# Compositor: RDP screen-sharing support
%def_enable screenshare

# Weston backend: Wayland (nested)
%def_enable backend_wayland

# Weston backend: X11 (nested)
%def_enable backend_x11

# VNC remote screensharing
%def_enable backend_vnc

# Weston backend: fbdev (deprecated)
%def_disable deprecated_backend_fbdev

# Default backend when no parent display server detected
# 'auto', 'drm', 'wayland', 'x11', 'fbdev', 'headless'
%define backend_default drm

# Weston renderer: EGL / OpenGL ES 2.x
%def_enable renderer_gl

# Weston launcher for systems without logind (removed since 11.0.0)
%def_disable deprecated_weston_launch

# Compositor: support systemd-logind D-Bus protocol (deprecated since 12.0.0)
%def_disable launcher_logind

# Compositor: support libseat (enabled by default)
%def_enable launcher_libseat

# Xwayland: support for X11 clients inside Weston
%def_enable xwayland

# systemd service plugin: state notify, watchdog, socket activation
%def_enable systemd

# Virtual remote output with GStreamer on DRM backend
%def_enable remoting

# Virtual remote output with Pipewire on DRM backend
%def_enable pipewire

# Weston shell UI: traditional desktop
%def_enable shell_desktop

# Weston shell UI: fullscreen/kiosk
%def_enable shell_fullscreen

# Weston shell UI: IVI (automotive)
%def_enable shell_ivi

# Weston shell UI: kiosk (desktop apps)
%def_enable shell_kiosk

# Weston desktop shell: default helper client selection
%define desktop_shell_client_default weston-desktop-shell

# Compositor color management: lcms
%def_enable color_management_lcms

# Compositor color management: static (deprecated)
%def_disable deprected_color_management_static

# Compositor color management: colord (deprecated since 11.0.0)
%def_disable deprecated_color_management_colord

# JPEG loading support
%def_enable image_jpeg

# WebP loading support
%def_enable image_webp

# List of accessory clients to build and install
# choices: [ 'calibrator', 'debug', 'info', 'terminal', 'touch-calibrator' ],
%define tools 'calibrator', 'debug', 'info', 'terminal', 'touch-calibrator'

# Sample clients: toytoolkit demo programs
%def_enable demo_clients

# Sample clients: simple test programs
%define simple_clients all
# choices: [ 'all', 'damage', 'im', 'egl', 'shm', 'touch', 'dmabuf-v4l', 'dmabuf-egl' ],

# Sample clients: optimize window resize performance
%def_enable resize_pool

# Tools: screen recording decoder tool
%def_enable wcap_decode

# Tests: output JUnit XML results
%def_enable test_junit_xml

# Tests: allow running with GL-renderer
%def_enable test_gl_renderer

# disabled by default
%def_disable doc

# running logind or seatd required
%def_disable check

Name: weston
Version: %ver_major.3
Release: alt1

Summary: Reference compositor for Wayland
Group: Graphical desktop/Other
License: MIT
Url: http://wayland.freedesktop.org/

Vcs: https://gitlab.freedesktop.org/wayland/weston.git
#Source: https://gitlab.freedesktop.org/wayland/weston/-/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
#Source1: %name.ini
Patch: %name-%version-%release.patch
#Patch2: weston-9.0.0-alt-launch-group.patch

Requires: lib%name = %EVR
Requires: xkeyboard-config
Requires: xorg-dri-swrast

%define pw_api_ver 0.3
%define pw_ver 0.3
%define gst_api_ver 1.0
%define mesa_ver 21.1.1

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-xdg
%{?_enable_systemd:BuildRequires(pre): rpm-build-systemd}
%{?_enable_launcher_libseat:BuildRequires: pkgconfig(libseat)}
BuildRequires: libGLES-devel libglvnd-devel
BuildRequires: libdrm-devel
BuildRequires: libgbm-devel >= %mesa_ver
BuildRequires: libdisplay-info-devel
BuildRequires: libva-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: wayland-protocols
BuildRequires: libpixman-devel
BuildRequires: libcairo-devel
BuildRequires: libpango-devel
BuildRequires: libevdev-devel
BuildRequires: libinput-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libdbus-devel
BuildRequires: libpam0-devel
%{?_enable_image_jpeg:BuildRequires: libjpeg-devel}
%{?_enable_image_webp:BuildRequires: libwebp-devel}
%{?_enable_deprecated_color_management_colord:BuildRequires: libcolord-devel}
%{?_enable_color_management_lcms:BuildRequires: liblcms2-devel}
%{?_enable_xwayland:
BuildRequires: xorg-xwayland-devel
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-shape) pkgconfig(xcb-xfixes) pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcursor) pkgconfig(cairo-xcb)}
%{?_enable_backend_rdp:BuildRequires: libfreerdp-devel}
%{?_enable_backend_x11:BuildRequires: pkgconfig(xcb) pkgconfig(xcb-xkb)}
%{?_enable_pipewire:BuildRequires: pkgconfig(libpipewire-%pw_api_ver) >= %pw_ver}
%{?_enable_remoting:
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) pkgconfig(gstreamer-allocators-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-app-%gst_api_ver) pkgconfig(gstreamer-video-%gst_api_ver)}
%{?_enable_test_junit_xml:BuildRequires: libxml2-devel}
%{?_enable_check:BuildRequires: xkeyboard-config /%_bindir/Xwayland}
%{?_enable_backend_vnc:BuildRequires: libaml-devel libneatvnc-devel >= 0.7}

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package -n lib%name
Summary: Weston compositor libraries
Group: System/Libraries

%description -n lib%name
This package contains Weston compositor libraries.

%package -n lib%name-devel
Summary: Development libraries for weston
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Header and Library files for doing development with the weston.

%package -n lib%name-protocols
Summary: Development libraries for weston
Group: Development/C
BuildArch: noarch
Requires: lib%name-devel = %EVR

%description -n lib%name-protocols
Header and Library files for doing development with the weston.

%package devel
Summary: Development files for weston
Group: Development/C
Requires: %name = %EVR
Requires: lib%name-devel = %EVR

%description devel
Header files for doing development with the weston.

%prep
%setup
%patch -p1
%{?_enable_deprecated_weston_launch:%patch2 -p1 -b .launch_group}

%build
%meson \
	%{?_enable_deprecated_weston_launch:-Ddeprecated-weston-launch=true \
	-Dweston-launch-group=xgrp} \
	--libexecdir=%clientsdir \
	%{?_disable_backend_x11:-Dbackend-x11=false} \
	%{?_disable_backend_rdp:-Dbackend-rdp=false} \
	%{?_disable_backend_vnc:-Dbackend-vnc=false} \
	%{?_disable_xwayland:-Dxwayland=false} \
	%{?_disable_remoting:-Dremoting=false} \
	%{?_disable_shell_ivi:-Dshell-ivi=false} \
	%{?_disable_pipewire:-Dpipewire=false} \
	%{?_disable_test_junit_xml:-Dtest-junit-xml=false} \
	%{?_enable_deprecated_backend_fbdev:-Ddeprecated-backend-fbdev=true} \
	%{?_enable_deprecated_color_management_static:-Ddeprecated-color-management-static=true}
%nil
%meson_build -v

%install
%meson_install
mkdir -p -- %buildroot/%_xdgconfigdir/%name
sed \
	-e 's,@clientsdir@,%clientsdir,g' \
	.gear/%name.ini > %buildroot/%_xdgconfigdir/%name/%name.ini

ln -sf %name/libexec_%{name}.so.%exec_soname \
%buildroot%_libdir/libexec_%{name}.so.%exec_soname

%check
%__meson_test

%files
%dir %_xdgconfigdir/%name
%{?_enable_backend_vnc:%_sysconfdir/pam.d/%name-remote-access}
%config(noreplace) %_xdgconfigdir/%name/%name.ini
%_bindir/*
%{?_enable_deprecated_weston_launch:%attr (4710,root,xgrp) %_bindir/weston-launch}
%dir %_libdir/%name
%{?_enable_color_management_colord:%_libdir/%name/cms-colord.so}
%{?_enable_deprecated_color_management_static:%_libdir/%name/cms-static.so}
%{?_enable_shell_desktop:%_libdir/%name/desktop-shell.so}
%{?_enable_shell_fullscreen:%_libdir/%name/fullscreen-shell.so}
%{?_enable_shell_ivi:
%_libdir/%name/hmi-controller.so
%_libdir/%name/ivi-shell.so}
%{?_enable_shell_kiosk:%_libdir/%name/kiosk-shell.so}
%{?_enable_screenshare:%_libdir/%name/screen-share.so}
%{?_enable_systemd:%_libdir/%name/systemd-notify.so}
# clients
%dir %_libdir/%name/clients
%{?_enable_shell_desktop:%_libdir/%name/clients/%name-desktop-shell}
%{?_enable_shell_ivi:%_libdir/%name/clients/%name-ivi-shell-user-interface}
%_libdir/%name/clients/%name-keyboard
%_libdir/%name/clients/%name-simple-im

%_datadir/%name/
%_datadir/wayland-sessions/%name.desktop
%_man1dir/%{name}*
%_man5dir/%{name}*
%_man7dir/%{name}*

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%files -n lib%name
%_libdir/lib%{name}*.so.*
%dir %_libdir/lib%name-%api_ver
%{?_enable_renderer_gl:%_libdir/lib%name-%api_ver/gl-renderer.so}
%{?_enable_remoting:%_libdir/lib%name-%api_ver/remoting-plugin.so}
%{?_enable_xwayland:%_libdir/lib%name-%api_ver/xwayland.so}
%{?_enable_pipewire:%_libdir/lib%name-%api_ver/pipewire-plugin.so}
%_libdir/%name/libexec_weston.so.*
#  symlink
%_libdir/libexec_%{name}.so.%exec_soname
# backends
%_libdir/lib%name-%api_ver/drm-backend.so
%{?_enable_deprecated_backend_fbdev:%_libdir/lib%name-%api_ver/fbdev-backend.so}
%{?_enable_backend_headless:%_libdir/lib%name-%api_ver/headless-backend.so}
%{?_enable_backend_rdp:%_libdir/lib%name-%api_ver/rdp-backend.so}
%{?_enable_backend_wayland:%_libdir/lib%name-%api_ver/wayland-backend.so}
%{?_enable_backend_x11:%_libdir/lib%name-%api_ver/x11-backend.so}
%{?_enable_color_management_lcms:%_libdir/lib%name-%api_ver/color-lcms.so}
%{?_enable_pipewire:%_libdir/lib%name-%api_ver/pipewire-backend.so}
%{?_enable_backend_vnc:%_libdir/lib%name-%api_ver/vnc-backend.so}

%files -n lib%name-devel
%_includedir/lib%name-%api_ver/
%_libdir/lib%{name}*.so
%_libdir/%name/libexec_weston.so
%_pkgconfigdir/lib%{name}*.pc

%files -n lib%name-protocols
%_datadir/lib%name-%api_ver/protocols/
%_datadir/pkgconfig/lib%name-%api_ver-protocols.pc

%changelog
* Wed Jun 05 2024 Yuri N. Sedunov <aris@altlinux.org> 13.0.3-alt1
- 13.0.3

* Tue Apr 23 2024 Yuri N. Sedunov <aris@altlinux.org> 13.0.1-alt1
- 13.0.1

* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 13.0.0-alt1
- 13.0.0

* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 12.0.3-alt1
- 12.0.3

* Sun Aug 06 2023 Yuri N. Sedunov <aris@altlinux.org> 12.0.2-alt1
- 12.0.2

* Fri May 26 2023 Yuri N. Sedunov <aris@altlinux.org> 12.0.1-alt1
- 12.0.1

* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 12.0.0-alt1
- 12.0.0

* Wed Dec 14 2022 Yuri N. Sedunov <aris@altlinux.org> 11.0.1-alt1
- 11.0.1

* Tue Jul 26 2022 Yuri N. Sedunov <aris@altlinux.org> 10.0.2-alt1
- 10.0.2

* Fri Jun 24 2022 Yuri N. Sedunov <aris@altlinux.org> 10.0.1-alt1
- 10.0.1

* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 10.0.0-alt2
- enabled deprecated weston launcher for systems without logind

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 10.0.0-alt1.1
- libexec_weston.so.* private libraries moved to libname package

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 10.0.0-alt1
- 10.0.0

* Sun Oct 31 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 9.0.0-alt1.2
- weston-launch: changed perms mode, subject of xgrp group (closes #41205)

* Sun Sep 12 2021 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1.1
- tests/ivi-layout-test-plugin.c: fixed for build with LTO

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1
- 9.0.0

* Sat Mar 02 2019 Alexey Gladkov <legion@altlinux.ru> 5.0.0-alt1
- Version (5.0.0).

* Thu Jul 05 2018 Alexey Gladkov <legion@altlinux.ru> 4.0.0-alt2
- Add rpm-build-xdg to buildrequires.

* Tue Jun 19 2018 Alexey Gladkov <legion@altlinux.ru> 4.0.0-alt1
- Version (4.0.0).

* Wed Feb 14 2018 Alexey Gladkov <legion@altlinux.ru> 3.0.0-alt1
- Version (3.0.0).

* Tue Feb 14 2017 Alexey Gladkov <legion@altlinux.ru> 1.99.92-alt0.5336153
- New upstream snapshot (1.99.92-6-g5336153).

* Thu Sep 29 2016 Alexey Gladkov <legion@altlinux.ru> 1.12.0-alt1
- Version (1.12.0).

* Thu Aug 25 2016 Alexey Gladkov <legion@altlinux.ru> 1.11.0-alt1
- Version (1.11.0).

* Mon Nov 18 2013 Alexey Gladkov <legion@altlinux.ru> 1.3.1-alt1
- Version (1.3.1).

* Wed Jul 17 2013 Alexey Gladkov <legion@altlinux.ru> 1.2.0-alt2
- Add missing directory.
- Remove unnecessary requires.

* Tue Jul 16 2013 Alexey Gladkov <legion@altlinux.ru> 1.2.0-alt1
- Version (1.2.0).

* Tue Apr 02 2013 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1
- Version (1.0.6).

* Wed Mar 06 2013 Alexey Gladkov <legion@altlinux.ru> 1.0.5-alt1
- Version (1.0.5).

* Sat Dec 29 2012 Alexey Gladkov <legion@altlinux.ru> 1.0.3-alt1
- Version (1.0.3).

* Mon Sep 24 2012 Alexey Gladkov <legion@altlinux.ru> 0.95.0-alt1
- First build for sisyphus.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Adam Jackson <ajax@redhat.com> 0.89-0.4
- Rebuild for new libudev
- Conditional buildreq for libudev-devel

* Wed Apr 25 2012 Richard Hughes <richard@hughsie.com> 0.89-0.3
- New package addressing Fedora package review concerns.

* Tue Apr 24 2012 Richard Hughes <richard@hughsie.com> 0.89-0.2
- Initial package for Fedora package review.


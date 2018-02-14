%global libweston_major 3

Name:           weston
Version:        3.0.0
Release:        alt1
Summary:        Reference compositor for Wayland
Group:          Graphical desktop/Other
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        %name-%version.tar

Packager: Alexey Gladkov <legion@altlinux.ru>

BuildRequires: autoconf gcc-c++ pkg-config doxygen
BuildRequires: glibc-devel-static
BuildRequires: libGLES-devel
BuildRequires: libXcursor-devel
BuildRequires: libcairo-devel
BuildRequires: libcolord-devel
BuildRequires: libdbus-devel
BuildRequires: libudev-devel
BuildRequires: libdrm-devel
BuildRequires: libgbm-devel
BuildRequires: libinput-devel
BuildRequires: libjpeg-devel
BuildRequires: liblcms2-devel
BuildRequires: libmtdev-devel
BuildRequires: libpam-devel
BuildRequires: libpixman-devel
BuildRequires: libsystemd-devel
BuildRequires: libva-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwebp-devel
BuildRequires: libxkbcommon-devel
BuildRequires: wayland-protocols

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package -n lib%name
Summary: Weston compositor libraries
Group:   System/Libraries

%description -n lib%name
This package contains Weston compositor libraries.

%package -n lib%name-devel
Summary:  Development libraries for weston
Group:    Development/C
Requires: %name = %version-%release

%description -n lib%name-devel
Header and Library files for doing development with the weston.

%package devel
Summary:  Development files for weston
Group:    Development/C
Requires: %name = %version-%release

%description devel
Header files for doing development with the weston.

%prep
%setup -q

%build
%autoreconf
%configure \
	--libexecdir=%_libdir/weston/clients \
	--disable-static \
	--disable-setuid-install \
	--disable-libunwind \
	--enable-xwayland \
	--enable-colord \
	--enable-clients \
	--enable-simple-clients \
	--enable-weston-launch \
	--enable-x11-compositor \
	--enable-drm-compositor \
	--enable-wayland-compositor \
	--enable-headless-compositor \
	--enable-fbdev-compositor \
	--enable-screen-sharing \
	--enable-vaapi-recorder \
	--enable-dbus \
	--enable-systemd-login \
	#

%make_build

%install
%make_install install DESTDIR=%buildroot

mkdir -p -- %buildroot/%_xdgconfigdir/weston
sed \
	-e 's,@clientsdir@,%_libdir/weston/clients,g' \
	.gear/weston.ini > %buildroot/%_xdgconfigdir/weston/weston.ini

chmod +s %buildroot/%_bindir/weston-launch

find %buildroot -name \*.la | xargs rm -f

#pre
#groupadd -r -f weston-launch
#useradd -r -g weston-launch -d /dev/null -s /dev/null -n weston-launch >/dev/null 2>&1 ||:

%files
%dir %_xdgconfigdir/weston
%config(noreplace) %_xdgconfigdir/weston/weston.ini
%_bindir/*
%_libdir/weston
%_datadir/weston
%_datadir/wayland-sessions/weston.desktop
%_man1dir/weston*
%_man5dir/weston*
%_man7dir/weston*
%doc README data/COPYING

%files devel
%_includedir/weston
%_pkgconfigdir/weston.pc

%files -n lib%name
%_libdir/libweston-%libweston_major
%_libdir/libweston*.so.*

%files -n lib%name-devel
%_includedir/libweston-%libweston_major
%_libdir/libweston*.so
%_pkgconfigdir/libweston*.pc

%changelog
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

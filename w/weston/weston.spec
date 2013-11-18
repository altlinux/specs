Name:           weston
Version:        1.3.1
Release:        alt1
Summary:        Reference compositor for Wayland
Group:          Graphical desktop/Other
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        %name-%version.tar

Packager: Alexey Gladkov <legion@altlinux.ru>

BuildRequires:  autoconf gcc-c++ pkg-config
BuildRequires:  libcairo-devel
BuildRequires:  libpango-devel
BuildRequires:  glib2-devel
BuildRequires:  libdrm-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libcolord-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg-devel librsvg-utils
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libwayland-cursor-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libEGL-devel >= 8.1
BuildRequires:  libgbm-devel
BuildRequires:  libGLES-devel
BuildRequires:  libGLU-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libmtdev-devel
BuildRequires:  libpam0-devel
BuildRequires:  libpixman-devel
BuildRequires:  libpoppler-devel
BuildRequires:  libpoppler-glib-devel
BuildRequires:  systemd-devel libwebp-devel

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package devel
Summary:          Development libraries for weston
Group:            Development/C
Requires:         %name = %version-%release

%description devel
Header and Library files for doing development with the weston.

%prep
%setup -q

%build
%autoreconf
%configure \
	--libexecdir=%_libdir/weston/clients \
	--disable-static \
	--disable-setuid-install \
	--disable-rpi-compositor \
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
	--without-cairo-glesv2

%make_build

%install
%make_install install DESTDIR=%buildroot

mkdir -p -- %buildroot/%_xdgconfigdir/weston
sed \
	-e 's,@clientsdir@,%_libdir/weston/clients,g' \
	rpm/weston.ini > %buildroot/%_xdgconfigdir/weston/weston.ini

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
%_man1dir/weston*
%_man5dir/weston*
%_man7dir/weston*
%doc README data/COPYING

%files devel
%_includedir/weston
%_pkgconfigdir/weston.pc

%changelog
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

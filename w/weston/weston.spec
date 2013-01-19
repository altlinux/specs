Name:           weston
Version:        1.0.3
Release:        alt1
Summary:        Reference compositor for Wayland
Group:          Graphical desktop/Other
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        %name-%version.tar

BuildRequires:  autoconf gcc-c++ pkg-config
BuildRequires:  libcairo-devel
BuildRequires:  glib2-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg-devel
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

%prep
%setup -q

%build
%autoreconf
%configure \
	--libexecdir=%_libexecdir/weston \
	--disable-static \
	--disable-setuid-install \
	--enable-xwayland \
	--enable-clients \
	--enable-simple-clients \
	--enable-weston-launch

%make_build

%install
%make_install install DESTDIR=%buildroot

find %buildroot -name \*.la | xargs rm -f

#pre
#groupadd -r -f weston-launch
#useradd -r -g weston-launch -d /dev/null -s /dev/null -n weston-launch >/dev/null 2>&1 ||:

%files
%_bindir/*
%_libdir/weston
%_libexecdir/weston
%_datadir/weston
%doc README data/COPYING

%changelog
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

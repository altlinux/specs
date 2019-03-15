Name: wayfire
Version: 0.1
Release: alt1

Summary: A wayland compositor based on wlroots

License: MIT
Group: Graphical desktop/Other
Url: https://github.com/WayfireWM/wayfire

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

BuildRequires(pre): meson
# Automatically added by buildreq on Sun Mar 17 2019
# optimized out: fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libX11-devel libXau-devel libXext-devel libXft-devel libXrender-devel libatk-devel libatkmm-devel libcairo-devel libcairo-gobject-devel libcairomm-devel libcrypt-devel libfreetype-devel libgdk-pixbuf-devel libgio-devel libglibmm-devel libglvnd-devel libgpg-error libgraphite2-devel libgtk+3-devel libharfbuzz-devel libicu-devel libp11-kit libpango-devel libpangomm-devel libpixman-devel libpng-devel libsigc++2-devel libstdc++-devel libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server libwayland-server-devel libwf-config libxcb-devel libxcbutil-icccm ninja-build perl pkg-config python-base python-modules python3 python3-base python3-module-pkg_resources sh4 wayland-devel xorg-proto-devel xz zlib-devel
BuildRequires: gcc-c++ libGLES-devel libdrm-devel libevdev-devel libglm-devel libgtkmm3-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwf-config-devel libwlroots-devel libxkbcommon-devel meson wayland-protocols

%package devel
Summary: Development files for Wayfire
Group: Development/C++

%description
Wayfire is a wayland compositor based on wlroots. It aims to create a
customizable, extendable and lightweight environment without sacrificing its
appearance.

It is also advisable to install wf-shell in order to get a background and a
panel.

%description devel
Wayfire is a wayland compositor based on wlroots. It aims to create a
customizable, extendable and lightweight environment without sacrificing its
appearance.

Development files for Wayfire.

%prep
%setup
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%config(noreplace) %_sysconfdir/%name/%name.ini
%_bindir/*
%_libexecdir/%name
%_datadir/%name

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Fri Mar 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.


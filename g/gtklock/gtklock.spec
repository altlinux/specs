Name: gtklock
Version: 3.0.0
Release: alt2.git.21.geff6868
Summary: GTK-based lockscreen for Wayland
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/jovanlanik/gtklock
Source: https://github.com/jovanlanik/gtklock/archive/refs/tags/v%version.tar.gz#/%name-%version.tar
Source1: %name.pam
Source44: %name.watch

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Mon Nov 20 2023
# optimized out: at-spi2-atk fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gobject-introspection-devel libX11-devel libXau-devel libXext-devel libXft-devel libXrender-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcap-ng libcrypt-devel libffi-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgraphite2-devel libgtk+3-devel libharfbuzz-devel libicu-devel libjson-glib libncurses-devel libp11-kit libpango-devel libpng-devel libtinfo-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libxcb-devel ninja-build perl pkg-config python3 python3-base python3-dev python3-module-setuptools sh5 wayland-devel xml-utils xz zlib-devel
BuildRequires: libgtk-session-lock-devel libpam-devel meson

%description
gtklock is a lockscreen based on gtkgreet.
It uses the ext-session-lock Wayland protocol.
Works on sway and other wlroots-based compositors.

For documentation, check out the man page and wiki.

%prep
%setup
cp -f %SOURCE1 pam/%name

%build
%meson \

%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%doc *.md
%_sysconfdir/pam.d/%name
%attr(102711,root,chkpwd) %_bindir/%name

%changelog
* Fri Sep 27 2024 Ildar Mulyukov <ildar@altlinux.ru> 3.0.0-alt2.git.21.geff6868
- new version (git head)
- fixes https://github.com/jovanlanik/gtklock/issues/104

* Tue Apr 30 2024 Ildar Mulyukov <ildar@altlinux.ru> 3.0.0-alt1
- change to the ext-session-lock Wayland protocol

* Tue Nov 21 2023 Ildar Mulyukov <ildar@altlinux.ru> 2.1.0-alt1.14.g6732a03
- Initial build for Sisyphus

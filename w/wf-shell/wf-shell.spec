Name: wf-shell
Version: 0.1
Release: alt1

Summary: A panel for the Wayfire compositor

License: MIT
Group: Graphical desktop/Other
Url: https://github.com/WayfireWM/wf-shell

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

# Automatically added by buildreq on Sun Mar 17 2019
# optimized out: at-spi2-atk fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libatkmm-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcairomm-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgpg-error libgtk+3-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwf-config ninja-build pkg-config python-base python-modules python3 python3-base python3-module-pkg_resources sh4 wayland-devel xz
BuildRequires: gcc-c++ libgtkmm3-devel libwf-config-devel meson wayland-protocols

%description
%summary.

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
%_datadir/wayfire

%changelog
* Fri Mar 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.



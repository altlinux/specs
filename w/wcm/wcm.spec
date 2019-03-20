Name: wcm
Version: 0.0.0.89.f481ea3
Release: alt1

Summary: Wayfire Config Manager

License: MIT
Group: Graphical desktop/Other
Url: https://github.com/WayfireWM/wcm

Source: %name-%version-%release.tar

Requires: wayfire

# Automatically added by buildreq on Wed Mar 20 2019
# optimized out: at-spi2-atk fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwf-config ninja-build pkg-config python-base python-modules python3 python3-base python3-module-pkg_resources sh4 xz
BuildRequires: gcc-c++ libgtk+3-devel libwf-config-devel libxml2-devel meson

%description
%summary.

%prep
%setup -n %name-%version-%release

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/*
%_datadir/wayfire

%changelog
* Wed Mar 20 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.89.f481ea3-alt1
- initial build for Sisyphus.


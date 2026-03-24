Name: fuzzel
Version: 1.14.1
Release: alt1

Summary: Application launcher for wlroots based Wayland compositors

License: MIT
Group: Other
Url: https://codeberg.org/dnkl/fuzzel
Vcs: https://codeberg.org/dnkl/fuzzel

# Source-url: https://codeberg.org/dnkl/fuzzel/releases/download/%version/fuzzel-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libtllist-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fcft)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(tllist)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(xkbcommon)

%description
Fuzzel is a Wayland-native application launcher, similar to rofi's drun mode.

Features:
  * Wayland native
  * Rofi drun-like mode of operation
  * dmenu mode where newline separated entries are read from stdin
  * Emacs key bindings
  * Icons!
  * Remembers frequently launched applications

%prep
%setup

%build
%meson -Denable-cairo=enabled \
       -Dpng-backend=libpng \
       -Dsvg-backend=nanosvg

%meson_build

%install
%meson_install

%check
%meson_test

%files
%_docdir/%name/
%_bindir/%name
%_datadir/fish/vendor_completions.d/*.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/%name.1*
%_man5dir/*.5*
%_sysconfdir/xdg/%name/

%changelog
* Tue Mar 10 2026 Aleksandr Dovydenkov <asd@altlinux.org> 1.14.1-alt1
- new version 1.14.1

* Fri Feb 06 2026 Aleksandr Dovydenkov <asd@altlinux.org> 1.14.0-alt1
- new version 1.14.0

* Mon Sep 22 2025 Aleksandr Dovydenkov <asd@altlinux.org> 1.13.1-alt1
- new version 1.13.1

* Tue May 06 2025 Egor Ignatov <egori@altlinux.org> 1.12.0-alt1
- new version 1.12.0

* Tue Sep 17 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.11.1-alt1
- new version 1.11.1 (with rpmrb script)

* Fri May 10 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.10.2-alt1
- initial build for ALT Sisyphus

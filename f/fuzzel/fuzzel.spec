Name: fuzzel
Version: 1.10.2
Release: alt1

Summary: Application launcher for wlroots based Wayland compositors

License: MIT
Group: Other
Url: https://codeberg.org/dnkl/fuzzel

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
* Fri May 10 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.10.2-alt1
- initial build for ALT Sisyphus


Name: wshowkeys
Version: 1.0
Release: alt1

Summary: Displays keypresses on screen on Wayland
License: GPL-3.0
Group: Graphical desktop/Other

Url: https://git.sr.ht/~sircmpwn/wshowkeys

# Source-url: https://git.sr.ht/~sircmpwn/wshowkeys/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xkbcommon)

%description
wshowkeys displays keypresses on screen on supported Wayland compositors.
Requires wlr_layer_shell_v1 support.

Note: This program must be configured as setuid during installation.
It requires root permissions to read input events, but drops these
permissions after startup.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%attr(4711,root,root) %_bindir/%name

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0
- switch to the maintained upstream URL (git.sr.ht/~sircmpwn, as in Debian)

* Tue Jan 13 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus

Name: wshowkeys
Version: 0.1
Release: alt1

Summary: Displays keypresses on screen on Wayland
License: GPL-3.0
Group: Graphical desktop/Other

Url: https://github.com/ammgws/wshowkeys

# Source-url: https://github.com/ammgws/wshowkeys/archive/refs/tags/%version.tar.gz
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
* Tue Jan 13 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus

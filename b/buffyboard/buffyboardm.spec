Name: buffyboard
Version: 0.2.0
Release: alt1
Summary: Touch-enabled framebuffer keyboard
License: GPLv3
Group: Accessibility
Url: https://gitlab.com/cherrypicker/buffyboard
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.xz

BuildRequires: meson pkgconfig(libinput) pkgconfig(xkbcommon)

%description
Buffyboard is a touch-enabled on-screen keyboard running on the Linux framebuffer

%prep
%setup -q

%build
meson _build
meson compile -C _build

%install
install -pD -m0755 _build/%name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Sep 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release


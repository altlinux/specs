Name: buffyboard
Version: 0.2.0
Release: alt2

Summary: Touch-enabled framebuffer keyboard
License: GPLv3
Group: Accessibility

Url: https://gitlab.com/cherrypicker/buffyboard
Packager: Valery Inozemtsev <shrek@altlinux.ru>
Source: %name-%version.tar.xz

BuildRequires: meson pkgconfig(libinput) pkgconfig(xkbcommon)

%description
Buffyboard is a touch-enabled on-screen keyboard running on Linux framebuffer

%prep
%setup
%ifarch %e2k
sed -i -E 's/static const char \* const (.*) = (".*");/#define \1 \2/' \
	sq2lv_layouts.c
%endif

%build
meson _build
meson compile -C _build

%install
install -pD -m0755 _build/%name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Sep 25 2023 Michael Shigorin <mike@altlinux.org> 0.2.0-alt2
- E2K: ftbfs workaround (mcst#8330; ilyakurdyukov@)
- minor spec cleanup

* Mon Sep 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release


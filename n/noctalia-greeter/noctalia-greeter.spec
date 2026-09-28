%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: noctalia-greeter
Version: 1.6.0
Release: alt1

Summary: Minimal login greeter for greetd matching the look and feel of Noctalia Shell
# Wuffs (third_party/wuffs) is Apache-2.0 OR MIT, the rest is MIT
License: MIT AND (Apache-2.0 OR MIT)
Group: Graphical desktop/Other

Url: https://github.com/noctalia-dev/noctalia-greeter
Vcs: https://github.com/noctalia-dev/noctalia-greeter

Source: %name-%version.tar
Source1: %name.toml
Patch0: %name-%version-alt.patch

Requires: greetd
# user list and avatars (docs/user/installation.md)
Requires: accountsservice
# noctalia-greeter-session starts the compositor under a session bus
Requires: /usr/bin/dbus-run-session

Provides: greetd-greeter

# startx is optional and needed only for X11 sessions
%filter_from_requires /^xinit$/d

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: libstb-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-ft)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(tomlplusplus)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots-0.20)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dm644 %SOURCE1 %buildroot%_sysconfdir/greetd/greeters/noctalia-greeter.toml
mkdir -p %buildroot%_altdir
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/noctalia-greeter.toml 45" \
	> %buildroot%_altdir/greetd-noctalia-greeter

# sourced by the other setup scripts, not executable on its own
chmod 644 %buildroot%_datadir/noctalia-greeter/greetd_setup_lib.sh

%check
%meson_test

%files
%doc LICENSE README.md docs/user examples/greeter.toml
%_bindir/noctalia-greeter
%_bindir/noctalia-greeter-apply-appearance
%_bindir/noctalia-greeter-compositor
%_bindir/noctalia-greeter-print-greetd-config
%_bindir/noctalia-greeter-session
%_bindir/noctalia-greeter-xsession
%_datadir/noctalia-greeter/
%_datadir/polkit-1/actions/org.noctalia.greeter.apply-appearance.policy
%_tmpfilesdir/noctalia-greeter.conf
%_altdir/greetd-noctalia-greeter
%config(noreplace) %_sysconfdir/greetd/greeters/noctalia-greeter.toml

%changelog
* Mon Sep 28 2026 Egor Ignatov <egori@altlinux.org> 1.6.0-alt1
- First build for ALT.

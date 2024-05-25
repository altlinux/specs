Name: swayfx
Version: 0.4
Release: alt1

Summary: A Beautiful Sway Fork
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/WillPower3309/swayfx
Source: %name-%version.tar

Conflicts: sway

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: asciidoc-a2x
BuildRequires: gcc-c++
BuildRequires: libpam-devel
BuildRequires: pkgconfig(basu)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots) >= 0.17.0
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(scenefx)
BuildRequires: scdoc

%description
Sway, but with eye candy!

%package data
Summary: %name - data files
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: sway-data

%description data
This package contains data files.

%prep
%setup

%build
%meson \
	-Dwerror=false
%meson_build

%install
%meson_install

mkdir -p %buildroot/%_sysconfdir/%name/config.d

%files
%doc README.md
%config(noreplace) %_sysconfdir/sway/config
%_bindir/sway
%_bindir/swaybar
%_bindir/swaymsg
%_bindir/swaynag
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_datadir/wayland-sessions/sway.desktop
%dir %_sysconfdir/sway

%_datadir/bash-completion/completions/sway*
%_datadir/fish/vendor_completions.d/sway*.fish
%_datadir/zsh/site-functions/_sway*

%files data
%dir %_datadir/backgrounds/sway
%_datadir/backgrounds/sway/*

%changelog
* Fri May 24 2024 Roman Alifanov <ximper@altlinux.org> 0.4-alt1
- new version 0.4 (with rpmrb script)

* Tue Aug 01 2023 Roman Alifanov <ximper@altlinux.org> 0.3.2-alt1
- new version 0.3.2 (with rpmrb script)
- add unowned /etc/sway dir to %files

* Tue Jun 27 2023 Roman Alifanov <ximper@altlinux.org> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Mon May 22 2023 Roman Alifanov <ximper@altlinux.org> 0.3-alt1
- Initial build for Sisyphus

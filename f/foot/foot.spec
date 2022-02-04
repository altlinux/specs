Name: foot
Version: 1.10.3
Release: alt1

Summary: A fast, lightweight and minimalistic Wayland terminal emulator
License: MIT
Group: Terminals
Url: https://codeberg.org/dnkl/foot

Source: %name-%version-%release.tar

BuildRequires: meson scdoc
BuildRequires: pkgconfig(tllist)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fcft)

%description
%summary

%prep
%setup

%build
%meson -Dterminfo=disabled
%meson_build

%install
%meson_install

%files
%doc LICENSE INSTALL.md README.md
%_bindir/foot
%_bindir/footclient
%_datadir/foot
%_desktopdir/*
%_datadir/bash-completion/*/*
%_datadir/fish/vendor_completions.d/*
%_datadir/zsh/site-functions/*
%_iconsdir/*/*/*/*
%_mandir/*/*

%changelog
* Fri Jan 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.3-alt1
- initial

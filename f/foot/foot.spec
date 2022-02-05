Name: foot
Version: 1.11.0
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
BuildRequires: pkgconfig(fcft) >= 3.0.0

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
%doc %_defaultdocdir/foot
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
* Sat Feb 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11.0-alt1
- 1.11.0 released

* Fri Jan 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.3-alt1
- initial

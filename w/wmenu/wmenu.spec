Name: wmenu
Version: 0.1.7
Release: alt1

Summary: Dynamic menu for Sway
License: MIT
Group: Graphical desktop/Other
Url: https://git.sr.ht/~adnano/wmenu

Source: %name-%version-%release.tar

BuildRequires: meson scdoc
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xkbcommon)

%description
wmenu is an efficient dynamic menu for Sway and wlroots based Wayland compositors.
It provides a Wayland-native dmenu replacement which maintains the look and feel of dmenu.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README*
%_bindir/wmenu
%_man1dir/wmenu.1*

%changelog
* Tue Mar  5 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.7-alt1
- initial

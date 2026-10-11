%define name libcosmic-gtk-appearance
%define libname libcosmic_gtk_appearance
%define giomoduledir %(pkg-config --variable giomoduledir gio-2.0)

%def_enable check

Name: %name
Version: 0.1.0
Release: alt0.1

Summary: GIO module that makes GTK3 and GTK4 windows follow the COSMIC desktop appearance settings
License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/marcelogomes90/libcosmic-gtk-appearance

Vcs: https://github.com/marcelogomes90/libcosmic-gtk-appearance.git

Source: %name-%version.tar

BuildRequires: just libgio-devel
BuildRequires: pkgconfig(wayland-client)
%{?_enable_check:BuildRequires: clippy rustfmt}

%description
This is a small shared library that loads into GTK3 and GTK4
applications. It reads your COSMIC appearance settings and applies them:
frosted glass when it is enabled, the palette of the live theme, and
COSMIC's own colours, corner radius and spacing on the window
decorations. Change the theme, the accent colour, the density or the
frosted setting and open windows follow along.

%prep
%setup

%build
just build

%install
install -pD -m644 target/release/%libname.so \
    %buildroot%giomoduledir/%libname.so

%check
just check

%files
%giomoduledir/%libname.so
%doc README*

%changelog
* Sat Oct 10 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.1
- first build for Sisyphus (1f397e2)



%define _libexecdir %_prefix/libexec

%define _name wayback
%define binary_name X%_name
%define ver_major 0.1
%define rdn_name io.github.fizzyizzy05.%_name

%def_enable man
%def_enable check

Name: %_name
Version: %ver_major
Release: alt0.2

Summary: A way to run X DE using Wayland components
License: MIT
Group: System/Servers
Url: https://gitlab.freedesktop.org/wayback/wayback

Vcs: https://gitlab.freedesktop.org/wayback/wayback.git

Source: %name-%version.tar

%define wl_proto_ver 1.14
%define wlr_api_ver 0.19
%define xw_ver 24.1

Provides: %binary_name = %EVR

Requires: xorg-xwayland >= %xw_ver
# for wayback-session
Requires: /etc/X11/xinit/xinitrc
Requires: seatd

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= %wl_proto_ver
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wlroots-%wlr_api_ver)
BuildRequires: pkgconfig(xwayland) >= %xw_ver
%{?_enable_man:BuildRequires: scdoc}

#%{?_enable_check:BuildRequires:}

%description
Wayback is an experimental X compatibility layer which allows for
running full X desktop environments using Wayland components. It is
essentially a stub compositor which provides just enough Wayland
capabilities to host a rootful Xwayland server.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_feature man generate_manpages}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%binary_name
%_bindir/%name-session
%_libexecdir/%name-compositor
%{?_enable_man:%_man1dir/%name-session.1*}
%doc README.*

%changelog
* Fri Jul 11 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt0.2
- updated to 5e821f9

* Mon Jun 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt0.1
- first build for Sisyphus (3507471)

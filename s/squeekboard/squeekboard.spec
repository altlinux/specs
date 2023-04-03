Name: squeekboard
Version: 1.22.0
Release: alt1

Summary: A Wayland on-screen keyboard
License: GPLv3
Group: Graphical desktop/Other
Url: https://gitlab.gnome.org/World/Phosh/squeekboard

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: meson rust-cargo /proc rpm-build-python3
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
%meson -Donline=false -Dnewer=true
%meson_build

%install
export CARGO_HOME=${PWD}/cargo
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop

%changelog
* Mon Apr 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22.0-alt1
- 1.22.0 released

* Thu Oct 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20.0-alt1
- 1.20.0 released

* Wed Apr 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17.1-alt1
- initial

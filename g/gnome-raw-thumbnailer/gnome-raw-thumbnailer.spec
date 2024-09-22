%define binary_name raw-thumbnailer
%define ver_major 47
%define _libexecdir %_prefix/libexec

Name: gnome-%binary_name
Version: %ver_major.0.1
Release: alt1

Summary: Camera raw thumbnailer for GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://www.gnome.org

Vcs: https://gitlab.gnome.org/World/gnome-raw-thumbnailer.git

Source: ftp://ftp.gnome.org/pub/gnome/sources/%binary_name/%ver_major/%binary_name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: shared-mime-info

%description
This package provides a thumbnailer for digital camera RAW files.

%prep
%setup -n %binary_name-%version

%build
%meson -Dprofile=release
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%binary_name
%_datadir/thumbnailers/raw.thumbnailer
%_datadir/mime/packages/%binary_name.xml
%doc README* ChangeLog

%changelog
* Sun Sep 22 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0.1-alt1
- first build for Sisyphus


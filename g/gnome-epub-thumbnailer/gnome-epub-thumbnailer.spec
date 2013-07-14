%define ver_major 1.0
%define _libexecdir %_prefix/libexec

Name: gnome-epub-thumbnailer
Version: %ver_major
Release: alt1

Summary: Thumbnailer for EPub books
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: libgio-devel libgdk-pixbuf-devel libxml2-devel libarchive-devel >= 3.1

%description
This package provides a thumbnailer for EPub books files.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/thumbnailers/*
%doc README AUTHORS NEWS

%changelog
* Sun Jul 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus


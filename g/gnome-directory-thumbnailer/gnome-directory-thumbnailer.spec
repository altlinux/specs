%define ver_major 0.1.2
%define _libexecdir %_prefix/libexec

Name: gnome-directory-thumbnailer
Version: %ver_major
Release: alt2

Summary: GNOME thumbnailer to generate thumbnails for directories
License: LGPLv2.1+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeDirectoryThumbnailer

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: intltool libgio-devel >= 2.36.0 libgtk+3-devel >= 3.0 libgnome-desktop3-devel

%description
This package provides a GNOME thumbnailer utility which will generate a
thumbnail for a directory.
It is intended to be called by gnome-desktops thumbnailer code, but
can be called manually as well.

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
%_datadir/thumbnailers/%name.thumbnailer
%doc README AUTHORS NEWS

%changelog
* Fri Mar 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- rebuilt against libgnome-desktop-3.so.10

* Mon Feb 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus




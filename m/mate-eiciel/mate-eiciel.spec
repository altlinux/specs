%define _unpackaged_files_terminate_build 1

Name: mate-eiciel
Version: 1.20.1
Release: alt1

Summary: Graphical editor for ACLs and xattr for MATE Desktop.
License: GPLv2
Group: Graphical desktop/MATE
Url: https://github.com/darkshram/mate-eiciel

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: mate-common
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtkmm-2.4)
BuildRequires: pkgconfig(libgnome-2.0)
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: libacl-devel

Requires: /usr/bin/caja

%description
Graphical editor for ACLs and xattr for MATE Desktop
MATE eiciel is a Graphical editor for access control lists (ACLs) and
extended attributes (xattr), either as an extension within Caja, or as a
standalone utility.

%prep
%setup
%patch -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %name --all-name

%files -f %name.lang
%doc TODO NEWS ChangeLog COPYING README README.md AUTHORS LICENSE ABOUT-NLS
%_bindir/*
%_libdir/caja/extensions-2.0/*.so
%dir %_datadir/help/C/%name/
%_datadir/applications/*%{name}.desktop
%_datadir/help/C/%name/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/metainfo/*%{name}.appdata.xml
%_man1dir/*

%changelog
* Fri Feb 07 2025 Nikolay Strelkov <snk@altlinux.org> 1.20.1-alt1
- Initial build for Sisyphus

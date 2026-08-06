%define _unpackaged_files_terminate_build 1
%define oname org.libvips.nip4

Name: nip4
Version: 9.1.5
Release: alt1

Summary: Image processing spreadsheet
License: GPL-2.0-only
Group: Graphics

Url: https://github.com/libvips/nip4
Vcs: https://github.com/libvips/nip4

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: flex
BuildRequires: cmake
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(vips)
BuildRequires: libgsl-devel
BuildRequires: pkgconfig(libxml-2.0)

%description
nip4 is a spreadsheet-like interface to the libvips image processing library.
You create a set of formula connecting your objects together, and on a change
nip4 will recalculate. Because nip4 uses libvips, it can process very large
images, it recalculates quickly, and it only needs a little memory. It scales
to fairly complex workflows: we have used it to develop systems with more than
10,000 cells, analyzing images totalling many hundreds of gigabytes.

nip4 can load all workspaces from nip2, the previous version of this program.
It has a batch mode, so you can run any image processing system you develop from
the command-line and without a GUI. It is purely functional, meaning there is no
assignment and there are no side effects, and it is fully lazy, meaning all
computation is driven by the user interface, down to the pixel level.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/*
%_desktopdir/%oname.desktop
%_datadir/glib-2.0/schemas/%oname.gschema.xml
%_iconsdir/hicolor/*/apps/*.png
%_mandir/man?/%{name}*.?.xz
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/%name

%changelog
* Thu Aug 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 9.1.5-alt1
- Initial build for ALT Linux.


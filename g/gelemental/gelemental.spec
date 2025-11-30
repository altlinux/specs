%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global optflags_lto %optflags_lto -ffat-lto-objects
%set_verify_elf_method strict,rpath=relaxed

Name: gelemental
Version: 2.0.2
Release: alt1

Summary: Periodic Table viewer
License: GPL-3.0 and MIT
Group: Sciences/Chemistry
Url: https://github.com/ginggs/gelemental

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(glibmm-2.4)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gtkmm-2.4)
BuildRequires: intltool

%description
gElemental is a GTK+ periodic table viewer that provides detailed information
about chemical elements.

It features a table view which allows the elements to be coloured thematically
by several properties, a sortable list view and an element properties
dialog, displaying a variety of information, including historical,
thermodynamic, electrochemical, and crystallographic properties.

%package devel
Summary: Periodic Table viewer (development files)
Requires: %name = %version-%release
Group: Development/C++

%description devel
gElemental is a GTK+ periodic table viewer that provides detailed information
about chemical elements.

It features a table view which allows the elements to be coloured thematically
by several properties, a sortable list view and an element properties
dialog, displaying a variety of information, including historical,
thermodynamic, electrochemical, and crystallographic properties.

This package contains the development libraries and headers.

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Science;Chemistry;|" data/gelemental.desktop.in

%build
%configure \
           --disable-static \
           --enable-debug
%make_build

%install
%makeinstall_std

%find_lang %name

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.DATA NEWS NEWS-GPeriodic README
%_bindir/gelemental
%_libdir/libelemental.so.0*
%_desktopdir/gelemental.desktop
%_iconsdir/hicolor/16x16/apps/gelemental.png
%_iconsdir/hicolor/22x22/apps/gelemental.png
%_iconsdir/hicolor/24x24/apps/gelemental.png
%_iconsdir/hicolor/32x32/apps/gelemental.png
%_iconsdir/hicolor/48x48/apps/gelemental.png
%_iconsdir/hicolor/scalable/apps/gelemental.svg
%_man1dir/gelemental.1.*

%files devel
%dir %_includedir/libelemental
%_includedir/libelemental/*
%_libdir/libelemental.so
%_pkgconfigdir/libelemental.pc

%changelog
* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus

%def_disable snapshot

%define ver_major 2.8
%define gst_api_ver 1.0
%def_enable debug
%def_enable exiv2
%def_enable libbrasero
%def_enable web_albums
%def_enable libchamplain
%def_disable libopenraw

Name: pix
Version: %ver_major.9
Release: alt1

Summary: An image viewer and browser utility.
License: GPLv2+
Group: Graphics
Url: https://github.com/linuxmint/pix

Source: %name-%version.tar

# From configure.in
%define glib_ver 2.38.0
%define gtk_ver 3.10.0
%define clutter_gtk_ver 1.0.0
%define gst_ver 1.0
%define exiv2_ver 0.20
%define openraw_ver 0.0.8
%define brasero_ver 3.2.0
%define soup_ver 2.36
%define gnome_common_ver 2.8.0
%define webp_ver 0.2.0
%define webkit_ver 1.10.0
%define champlain_ver 0.12.0
%define desktop_file_utils_ver 0.8

Requires: %name-data = %version-%release
Requires: xapps-icons

# From configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libclutter-devel libclutter-gtk3-devel >= %clutter_gtk_ver
BuildPreReq: gstreamer%gst_api_ver-devel >= %gst_ver gst-plugins%gst_api_ver-devel >= %gst_ver

BuildRequires: libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libsoup-gnome-devel >= %soup_ver libsecret-devel
BuildRequires: librsvg-devel intltool perl-XML-Parser gnome-common yelp-tools
BuildRequires: gsettings-desktop-schemas-devel libwebp-devel >= %webp_ver libjson-glib-devel
BuildRequires: libwebkit2gtk-devel >= %webkit_ver libchamplain-devel >= %champlain_ver
%{?_enable_libopenraw:BuildPreReq: libopenraw-gnome-devel >= %openraw_ver}
%{?_enable_libbrasero:BuildRequires: libbrasero-devel >= %brasero_ver}
%{?_enable_web_albums:BuildRequires: bison flex}
%{?_enabled_libchamplain:BuildRequires: libchamplain-devel >= %champlain_ver}

%if_enabled exiv2
BuildPreReq: libexiv2-devel >= %exiv2_ver gcc-c++
%endif

BuildPreReq: libjpeg-devel libtiff-devel libXrender-devel libXext-devel libX11-devel
BuildPreReq: libXtst-devel libXxf86vm-devel gnome-doc-utils libXi-devel
BuildRequires: libSM-devel libICE-devel

BuildRequires: desktop-file-utils >= %desktop_file_utils_ver
BuildRequires: gnome-common >= %gnome_common_ver

%description
Pix is an image browser, viewer, organizer and editor.
It features some advanced tools, too:

   * Import images from a digital camera.
   * Slide Shows.
   * Set an image as Desktop background.
   * Create index image.
   * Rename images in series.
   * Convert image format.
   * Change images date and time.
   * JPEG lossless transformations.
   * Find duplicated images.

%package data
Summary: Arch independent files for pix
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for pix to work.

%package devel
Summary: pix development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains headers needed to build extensions for pix.

%prep
%setup

%build
%autoreconf
%configure \
    --enable-jpeg \
    --enable-tiff \
    %{subst_enable exiv2} \
    %{subst_enable debug} \
    %{subst_enable libbrasero} \
    %{subst_enable libchamplain} \
    %{subst_enable libopenraw} \
    --disable-static \
    --disable-schemas-compile \
    --enable-libopenraw \
    --with-smclient=xsmp

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files
%_bindir/*
%dir %_libdir/pix/extensions
%_libdir/pix/extensions/*
%exclude %_libdir/%name/extensions/*.la

%files data  -f %name.lang
%_datadir/locale/sr@Latn/LC_MESSAGES/pix.mo
%_desktopdir/*
%_datadir/%name/
%_iconsdir/hicolor/*/*/*
%config %_datadir/glib-2.0/schemas/*.xml
%_man1dir/pix.1.*
%doc AUTHORS NEWS README.md

%files devel
%_includedir/pix-%ver_major/
%_datadir/aclocal/pix.m4
%_libdir/pkgconfig/*

%changelog
* Tue Jan 10 2023 Vladimir Didenko <cow@altlinux.org> 2.8.9-alt1
- 2.8.9

* Fri Dec 2 2022 Vladimir Didenko <cow@altlinux.org> 2.8.8-alt1
- 2.8.8

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 2.8.7-alt1
- 2.8.7

* Tue Jul 12 2022 Vladimir Didenko <cow@altlinux.org> 2.8.6-alt1
- 2.8.6

* Tue Jun 21 2022 Vladimir Didenko <cow@altlinux.org> 2.8.5-alt1
- 2.8.5

* Thu Jan 13 2022 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt1
- 2.8.4

* Wed Dec 15 2021 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- 2.8.1-1-g8e01c62

* Mon Nov 29 2021 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- New version

* Tue Jun 29 2021 Vladimir Didenko <cow@altlinux.org> 2.6.5-alt1
- New version

* Thu Jun 17 2021 Vladimir Didenko <cow@altlinux.org> 2.6.4-alt1
- New version

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- New version

* Tue Dec 22 2020 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- New version

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 2.6.1-alt1
- New version

* Thu Dec 3 2020 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- New version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 2.4.11-alt1
- New version

* Tue Jun 9 2020 Vladimir Didenko <cow@altlinux.org> 2.4.9-alt1
- New version

* Mon Jun 1 2020 Vladimir Didenko <cow@altlinux.org> 2.4.8-alt2
- add xapps-icons to dependencies

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 2.4.8-alt1
- New version

* Wed Jan 8 2020 Vladimir Didenko <cow@altlinux.org> 2.4.5-alt1
- New version

* Tue Dec 17 2019 Vladimir Didenko <cow@altlinux.org> 2.4.3-alt1
- New version

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- New version

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- New version

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- New version

* Wed Jun 26 2019 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- New version

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- New version

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- New version

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- New version

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- New version

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.2-alt1
- New version

* Fri Sep 8 2017 Vladimir Didenko <cow@altlinux.org> 1.4.5-alt1
- Initial build for Sisyphus

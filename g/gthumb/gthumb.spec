%define ver_base 3.0
%define ver_major 3.0
%def_enable debug
%def_enable exiv2
# brasero-3 not supported
%def_enable libbrasero
%def_enable web_albums

Name: gthumb
Version: %ver_major.1
Release: alt1

Summary: An image file viewer and browser for GNOME
Summary(ru_RU.UTF-8): Просмотрщик изображений и фотоальбом для GNOME

License: GPL
Group: Graphics
Url: http://gthumb.sourceforge.net/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Source1: %name.ru.po

# remove useless dump_exif_data() function (not compiled against exive2 < 0.21.1)
Patch: %name-2.13.91-remove_dump_exif_data.patch

# From configure.in
%define glib_ver 2.28.0
%define gtk_ver 3.2.0
%define clutter_gtk_ver 1.0.0
%define gst_ver 0.10
%define exiv2_ver 0.20
%define openraw_ver 0.0.8
%define brasero_ver 3.2.0
%define soup_ver 2.36
%define keyring_ver 3.2
%define gnome_common_ver 2.8.0
%define desktop_file_utils_ver 0.8

Requires: %name-data = %version-%release

# From configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libclutter-devel libclutter-gtk3-devel >= %clutter_gtk_ver
BuildPreReq: gstreamer-devel >= %gst_ver gst-plugins-devel >= %gst_ver
BuildPreReq: libopenraw-gnome-devel >= %openraw_ver
BuildRequires: libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libsoup-gnome-devel >= %soup_ver libgnome-keyring-devel >= %keyring_ver
BuildRequires: librsvg-devel intltool perl-XML-Parser gnome-common gnome-doc-utils
BuildRequires: gsettings-desktop-schemas-devel
%{?_enable_libbrasero:BuildRequires: libbrasero-devel >= %brasero_ver}
%{?_enable_web_albums:BuildRequires: bison flex}

%if_enabled exiv2
BuildPreReq: libexiv2-devel >= %exiv2_ver gcc-c++
%endif

BuildPreReq: libjpeg-devel libtiff-devel libXrender-devel libXext-devel libX11-devel
BuildPreReq: libXtst-devel libXxf86vm-devel gnome-doc-utils libXi-devel
BuildRequires: libSM-devel libICE-devel

BuildRequires: desktop-file-utils >= %desktop_file_utils_ver
BuildRequires: gnome-common >= %gnome_common_ver

%description
gThumb lets you browse your hard disk, showing thumbnails of image
files. It also lets view single files (including GIF animations),
add comments to images, organize images in catalogs, print images, view
slideshows, set desktop background, and more.

%description -l ru_RU.UTF-8
gThumb позволяет просматривать содержимое жёсткого диска, показывая
уменьшенные копии содержимого графических файлов. Также программа
позволяет просматривать отдельные изображения (включая мультфильмы в
формате GIF), добавлять комментарии к картинкам, раскладывать картинки
по каталогам, печатать, автоматически пролистывать серии картинок,
менять фон рабочего стола и многое другое.

%package data
Summary: Arch independent files for gThumb
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for gThumb to work.

%package devel
Summary: gThumb development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains headers needed to build extensions for gThumb.

%prep
%setup -q
#cp %SOURCE1 po/ru.po
#%%patch

%build
gnome-doc-prepare -f
%autoreconf
%configure \
    --enable-jpeg \
    --enable-tiff \
    %{subst_enable exiv2} \
    %{subst_enable debug} \
    %{subst_enable libbrasero} \
    --disable-static \
    --disable-scrollkeeper \
    --disable-schemas-compile \
    --enable-libopenraw \
    --with-smclient=auto

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%define schemas gthumb-comments gthumb_convert_format gthumb-gstreamer gthumb_image_print gthumb-image-viewer gthumb-importer gthumb_photo_importer gthumb-picasaweb gthumb-pixbuf-savers gthumb_resize_images gthumb gthumb-slideshow gthumb_crop_options gthumb_rename_series gthumb_resize_options gthumb_webalbums

%files
%_bindir/*
%dir %_libdir/gthumb/extensions
%_libdir/gthumb/extensions/*
%exclude %_libdir/%name/extensions/*.la

%files data  -f %name.lang
%_desktopdir/*
%_datadir/%name/
%_iconsdir/hicolor/*/*/*
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.change-date.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.comments.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.contact-sheet.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.convert-format.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.crop.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.enums.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.facebook.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.file-manager.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.gstreamer-tools.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.image-print.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.image-viewer.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.importer.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.photo-importer.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.picasaweb.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.pixbuf-savers.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.rename-series.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.resize.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.resize-images.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.rotate.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.slideshow.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.webalbums.gschema.xml
%_datadir/GConf/gsettings/%name.convert
%_man1dir/gthumb.1.*
%doc AUTHORS NEWS README

%files devel
%_includedir/gthumb-%ver_base/
%_datadir/aclocal/gthumb.m4
%_libdir/pkgconfig/*

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Apr 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.90.3-alt1
- 2.90.3

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 2.90.2-alt2
- updated from upstream git

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.90.2-alt1
- 2.90.2

* Tue Jan 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.14.2-alt1
- 2.14.2

* Sun Dec 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1
- split up noarch data in separate -data subpackage

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt2
- rebuilt against libexiv2.so.11

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.13.91-alt1
- 2.13.91

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.12.3-alt1
- 2.12.3

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt2
- updated buildreqs
- added some fixes from upstream

* Sat Jan 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt1
- 2.12.2

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.11.92-alt1
- 2.11.92

* Thu Jun 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.11.3-alt2
- rebuild against libexiv2-0.20

* Wed May 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.12-alt1
- 2.10.12

* Sun Sep 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.10.11-alt3
- updated russian translation (ALT #21639)

* Tue Jun 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.10.11-alt2
- rebuild

* Sun Mar 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.10.11-alt1
- new version

* Mon Dec 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt3
- removed obsolete %%post* macros
- updated buildreqs

* Thu Oct 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt2
- updated russian translation
  http://l10n.gnome.org/POT/gthumb.HEAD/gthumb.HEAD.ru.po

* Tue Sep 23 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt1
- 2.10.10

* Wed Aug 06 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.9-alt1
- new version
- updated buildreqs (versions, raw and IPTC support enabled)

* Mon Mar 24 2008 Vitaly Lipatov <lav@altlinux.ru> 2.10.8-alt1
- new version 2.10.8 (with rpmrb script)

* Thu Oct 18 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.7-alt1
- new version 2.10.7 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.6-alt1
- new version 2.10.6 (with rpmrb script)
- enable update/clean menus

* Sat Jun 23 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.4-alt1
- new version 2.10.4 (with rpmrb script)
- spec fixes

* Wed Mar 14 2007 Vitaly Lipatov <lav@altlinux.ru> 2.9.3-alt1
- new version 2.9.3 (with rpmrb script)
- bzip ChangeLog (fix bug #11084), thanks icesik@

* Sun Jan 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt0.1
- new version 2.9.1 (formally unstable)
- add gnome-doc-utils to buildreq

* Fri Dec 29 2006 Alexey Rusakov <ktirf@altlinux.org> 2.8.1-alt1
- new version (2.8.1)

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.7.8-alt1
- new version (2.7.8), switching to formally-unstable branch.
- renamed 'with libexif' switch to 'enable exif', to fit with configure script.
- likewise, renamed 'with gphoto' to 'enable gphoto2'.

* Tue Apr 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.9-alt1
- new version (2.6.9)
- spec cleanup, dependencies updated
- removed Debian menu support.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.6-alt1
- 2.6.6

* Sat Apr 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1.1
- rebuild against libexif.so.12.

* Fri Mar 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Sun Jan 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Dec 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Nov 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.1-alt1
- 2.6.0.1

* Mon Sep 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1.1
- rebuild with libtiff.so.4

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Wed Sep 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sat May 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu May 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1.1
- updated translations by slava@.

* Fri Apr 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt2
- build with gphoto2 support.
- new translation, i18n fix, summary and description in UTF-8 by slava.

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Fri Dec 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Thu Dec 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.9-alt1
- 2.1.9

* Mon Nov 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Mon Sep 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Wed Jul 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3
- ru.po by slava.

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- go to gnome2.
- Patch for building with libgnomeprint2-2.2 by AVL.

* Thu Jun 13 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.13-alt1
- ALTLinux build.

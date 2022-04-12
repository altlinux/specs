%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define rdn_name org.geeqie.Geeqie

%def_enable map
%def_enable ffmpegthumbnailer

Name: geeqie
Version: 1.7.3
Release: alt1

Summary: Graphics file browser utility
License: GPL-2.0-or-later
Group: Graphics
Url: https://www.%name.org

%if_disabled snapshot
Source: https://github.com/BestImageViewer/geeqie/archive/v%version/%name-%version.tar.gz
#Source: %url/%name-%version.tar.bz2
%else
Vcs: https://github.com/BestImageViewer/geeqie.git
Source: %name-%version.tar
%endif
# produced by gen_changelog.sh from git tree
Source1: ChangeLog
Source2: ChangeLog.html

Patch: %name-1.5-libdir-fix.patch

Provides: gqview = %version-%release
Obsoletes: gqview < %version

Requires: %_bindir/exiftool %_bindir/exiftran
Requires: %_bindir/convert %_bindir/gphoto2
Requires: %_bindir/zenity lcms2-utils >= 2.12-alt2

BuildRequires: gcc-c++ yelp-tools intltool libappstream-glib-devel
BuildRequires: python3-module-markdown
BuildRequires: libgtk+3-devel libjpeg-devel libtiff-devel libwebp-devel
BuildRequires: libopenjpeg2.0-devel libdjvu-devel liblcms2-devel
BuildRequires: libpoppler-glib-devel libheif-devel
BuildRequires: libraw-devel libgomp-devel
BuildRequires: libexiv2-devel liblirc-devel zlib-devel libarchive-devel
%{?_enable_map:BuildRequires: libgps-devel pkgconfig(clutter-gtk-1.0) libchamplain-gtk3-devel}
%{?_enable_ffmpegthumbnailer:BuildRequires: libffmpegthumbnailer-devel}

%description
Geeqie is a lightweight image viewer. It was forked from GQview. The development
is focused on features for photo collection maintenance: raw format, Exif/IPTC/XMP
metadata and integration with programs like UFraw, ImageMagick, Gimp, gPhoto or
ExifTool.

%prep
%setup
%patch -b .libdir
cp %SOURCE1 %SOURCE2 ./

sed -i 's/\-Werror//' configure.ac

%build
%add_optflags %(getconf LFS_CFLAGS)
%{?_enable_ffmpegthumbnailer:%add_optflags -Wno-error=unused-function}
%autoreconf
%configure --enable-lirc \
	--enable-largefile \
	--with-readmedir=%_datadir/%name \
	--disable-lua \
	%{subst_enable ffmpegthumbnailer}
%make_build

%install
%makeinstall_std
install -pD -m644 %name.png %buildroot%_liconsdir/%name.png

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_libdir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/%name.1.*
%_datadir/metainfo/%rdn_name.appdata.xml
%doc NEWS README.*

%changelog
* Tue Apr 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Wed Jan 26 2022 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2
- updated BRs and dependencies

* Mon Jan 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Aug 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt4
- applied upstream fixes for "Run time check on GDK display backend"
  and "Images fail to render on MacOS"

* Sat Aug 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt3
- applied upstream fixes for "segfault with clutter-gtk"
  https://github.com/BestImageViewer/geeqie/issues/829 (ALT #40734)

* Tue Apr 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt2
- fixed doc building with newer yelp by upstream

* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6 (GTK3 build)
- note: to run geeqie under wayland need to use following command
  "GDK_BACKEND=x11 geeqie --disable-clutter"

* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Fri Aug 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt2
- rebuilt against libexiv2.so.26

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3
- removed upstreamed patches

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2 (new url)
- removed upstreamed patches

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt5
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1-alt4.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt4
- applied some patches from geeqie bugtracker and mailing list
- built against liblcms2 (ALT #29943)

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt2
- rebuilt against libexiv2.so.13

* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1
- removed obsolete patches, more fixes for lfs

* Sat Jul 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt5
- rebuild

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt4
- rebuilt against libexiv2.so.11

* Thu Oct 21 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt3
- Patch to use arch-specific libdir instead of hardcoded /usr/lib.

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt2
- 1.0

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 1.0-alt1.beta2
- Rebuild with libexiv2.so.6.

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt0.beta2
- 1.0 beta2.

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt0.beta1
- 1.0 beta1.

* Thu Jul 31 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt0.alpha2
- Update to 1.0 alpha2 and build with LIRC support.

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt0.alpha1.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Thu May 15 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt0.alpha1
- Initial build.

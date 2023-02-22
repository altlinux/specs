%define _libexecdir %_prefix/libexec

%define ver_major 4.2
%define beta %nil
%define rdn_name org.darktable.darktable

%def_enable noise_tools
# o.21 required
%def_disable system_libraw
%def_enable system_lua
%def_enable libavif
%def_enable libheif
%def_enable jxl
# lensfun a mandatory dependency
#src/iop/lens.cc:
#error lensfun 0.3.95 is not supported since its API is not backward compatible with lensfun stable release.
%def_enable lensfun

Name: darktable
Version: %ver_major.1
Release: alt1

Summary: Darktable is a virtual lighttable and darkroom for photographer
License: GPL-3.0
Group: Graphics
Url: http://%name.org/

Vcs: https://github.com/darktable-org/darktable.git
Source: https://github.com/darktable-org/darktable/releases/download/release-%version/%name-%version.tar.xz
# required for llvm-7.0
Patch: darktable-3.0.0-is_supported_platform.patch
# See https://bugzilla.altlinux.org/38215
# based on https://bugzilla.altlinux.org/attachment.cgi?id=8682&action=edit
# by Pavel Nakonechnyi
Patch1: darktable-4.0.0-alt-disable-use-of-gcc-graphite.patch

ExcludeArch: %ix86 armh

%define cmake_ver 3.10
%define openmp_ver 4.0
%define glib_ver 2.40
%define gtk_ver 3.24.15
%define exiv2_ver 0.24
%define iso_codes_ver 3.66
%define pugixml_ver 1.8
%define lensfun_api_ver 1
%define lensfun_ver 0.3.3
%define libraw_ver 0.21.0
%define libavif_ver 0.9.1
%define libheif_ver 1.12.0
%define lua_ver_major 5.4

Requires: iso-codes >= %iso_codes_ver
Requires: icon-theme-adwaita
%{?_enable_noise_tools:Requires: %_bindir/gnuplot}

BuildRequires(pre):rpm-macros-cmake
BuildRequires: /proc cmake >= %cmake_ver ninja-build gcc-c++ libgomp-devel
BuildRequires: intltool desktop-file-utils /usr/bin/appstream-util po4a
BuildRequires: perl-Pod-Parser xsltproc exiftool
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libxml2-devel
BuildRequires: libSDL2-devel libX11-devel libXrandr-devel libcurl-devel
BuildRequires: libexiv2-devel >= %exiv2_ver libflickcurl-devel libsecret-devel
BuildRequires: libgphoto2-devel libjpeg-devel liblcms2-devel
BuildRequires: liblensfun%lensfun_api_ver-devel >= %lensfun_ver
BuildRequires: libpng-devel librsvg-devel libsqlite3-devel libtiff-devel
BuildRequires: openexr-devel libxkbcommon-x11-devel lsb-release
BuildRequires: libjson-glib-devel libsoup-devel libpixman-devel libexpat-devel
BuildRequires: libcolord-gtk-devel libudev-devel
BuildRequires: libGraphicsMagick-c++-devel libopenjpeg2.0-devel
BuildRequires: libharfbuzz-devel libwebp-devel libxshmfence-devel
# since 2.0
BuildRequires: libpugixml-devel >= %pugixml_ver libcups-devel
BuildRequires: libosm-gps-map1.0-devel
BuildRequires: /usr/bin/jsonschema
BuildRequires: iso-codes-devel >= %iso_codes_ver
BuildRequires: libgmic-devel libjasper-devel
%{?_enable_system_lua:BuildRequires(pre): rpm-build-lua
BuildRequires: liblua%lua_ver_major-devel
Provides: lua%lua_ver_major(darktable)}
%{?_enable_system_libraw:BuildRequires: libraw-devel >= %libraw_ver}
%{?_enable_libavif:BuildRequires: libavif-devel >= %libavif_ver}
%{?_enable_libheif:BuildRequires: libheif-devel}
%{?_enable_jxl:BuildRequires: libjxl-devel}
# for not recommended build from git tree
#BuildRequires: gnome-doc-utils fop saxon ...

%description
darktable is a virtual light table and darkroom for photographers. It manages
your digital negatives in a database and lets you view them through a zoomable
light table. It also enables you to develop raw images and enhance them.

%prep
%setup -n %name-%version
%patch1 -p1

%build
%ifarch ppc64le
%define optflags_lto %nil
%endif
%define _optlevel 3
%cmake \
-GNinja \
-DCMAKE_SKIP_RPATH:BOOL=OFF \
-DCMAKE_BUILD_TYPE=Release \
-DBINARY_PACKAGE_BUILD:BOOL=ON \
-DRAWSPEED_ENABLE_LTO=ON \
%{?_disable_lensfun:-DUSE_LENSFUN=OFF} \
%{?_enable_noise_tools:-DBUILD_NOISE_TOOLS=ON} \
%ifarch ppc64le
-DUSE_OPENCL=OFF \
%endif
%{?_enable_system_libraw:-DDONT_USE_INTERNAL_LIBRAW=ON} \
%{?_enable_system_lua:-DDONT_USE_INTERNAL_LUA=ON}
%nil
%cmake_build

%install
%cmake_install

ln -s %name/lib%name.so %buildroot%_libdir/lib%name.so

install -pD -m644 data/pixmaps/16x16/darktable.png %buildroot%_miconsdir/darktable.png
install -pD -m644 data/pixmaps/32x32/darktable.png %buildroot%_niconsdir/darktable.png
install -pD -m644 data/pixmaps/48x48/darktable.png %buildroot%_liconsdir/darktable.png

%find_lang --with-man --all-name --output=%name.lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_libdir/lib%name.so
%_libdir/%name/
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_datadir/metainfo/%rdn_name.appdata.xml
%{?_enable_noise_tools:
%_libexecdir/%name/tools/%name-gen-noiseprofile
%_libexecdir/%name/tools/%name-noiseprofile
%_libexecdir/%name/tools/profiling-shot.xmp
%_libexecdir/%name/tools/subr.sh}
%exclude /usr/share/doc/%name/
%doc README* RELEASE_NOTES*

%changelog
* Wed Feb 22 2023 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Thu Dec 22 2022 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Sun Jul 03 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sat Feb 26 2022 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1.1
- disabled LTO for ppc64le (ALT #40876)

* Sun Jul 04 2021 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Jun 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1.1
- fixed BR

* Sat Feb 06 2021 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Aug 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1
- ExcludeArch: +armh

* Sat Apr 18 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- 3.0.2

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt2
- rebuilt with gcc

* Fri Mar 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1
- ExcludeArch: %ix86 (not supported by upstream)
- built with clang/llvm-10.0
- enabled GMIC support

* Mon Oct 21 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt2
- fixed build against libexiv2-0.27.2
- ppc64le: disabled OpenCL

* Wed Mar 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Thu Mar 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Dec 25 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt2
- rebuilt against libexiv2.so.26

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1.1
- fixed buildreqs

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Sat Jan 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sun Dec 25 2016 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Oct 25 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Tue Sep 06 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Jul 05 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Fri May 06 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt2
- rebuilt against libosmgpsmap-1.0.so.1

* Tue Mar 29 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- rebuilt against liblensfun.so.1

* Thu Dec 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.9-alt1
- 1.6.9

* Tue Aug 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.8-alt1
- 1.6.8

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt2
- rebuilt against libexiv2.so.14

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.7-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7 using gcc-4.9

* Tue Apr 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Wed Mar 11 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt2
- rebuilt against libgphoto2_port.so.12

* Sun Feb 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sat Dec 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt2
- added -DBINARY_PACKAGE_BUILD:BOOL=ON  directive to cmake
  (suggested by upstream) to allow the program to run on
  various processors with sse3 and above

* Sat Dec 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Dec 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt2
- rebuilt against libcolord.so.2

* Thu May 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Feb 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Dec 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4 release

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt0.1.rc1
- 1.4-rc1
- built against libexiv2.so.13

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3, fixed (ALT #29371)

* Sun Aug 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2
- GraphicsMagick, libopenjpeg support

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.1
- Rebuilt with libpng15

* Sat Jun 16 2012 Victor Forsiuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Mar 15 2012 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt2
- rebuilt against libexiv2.so.11

* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 0.9.2-alt1
- 0.9.2

* Wed Jul 27 2011 Victor Forsiuk <force@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sun Jul 03 2011 Victor Forsiuk <force@altlinux.org> 0.9-alt1
- 0.9

* Wed Mar 09 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt3
- Refresh BuildRequires.

* Thu Feb 17 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt2
- Fix build mistake, now darktable will work correctly (closes: #25102).

* Wed Feb 16 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt1
- 0.8

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Dec 03 2010 Victor Forsiuk <force@altlinux.org> 0.7-alt1
- 0.7

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 0.6-alt1
- 0.6

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt2
- Rebuild with libexiv2.so.9.

* Wed Mar 31 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt1
- 0.5

* Wed Feb 10 2010 Victor Forsiuk <force@altlinux.org> 0.4-alt1.git20100210
- Git snapshot from 2010-02-10.

* Tue Aug 18 2009 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.

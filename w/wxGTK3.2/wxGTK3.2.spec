# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with webkitgtk
%def_with sdl

%define wxbranch 3.2

Name: wxGTK3.2
Version: 3.2.6
Release: alt1

Summary: The GTK+ port of the wxWidgets library
License: wxWidgets
Group: System/Libraries
Url: https://wxwidgets.org

# https://github.com/wxWidgets/wxWidgets.git
Source: %name-%version.tar
Source1: catch.tar
Source2: pcre.tar
Source3: nanosvg.tar
Source11: ld_shared_wrapper.pl
Patch1: wxGTK3.0-disable-ABI-checking.patch

BuildRequires: gcc-c++
BuildRequires: libGL-devel libGLU-devel libSM-devel
BuildRequires: libX11-devel libXinerama-devel libICE-devel libXmu-devel libXext-devel libXp-devel
BuildRequires: xorg-xextproto-devel xorg-inputproto-devel libXtst-devel
BuildRequires: libexpat-devel
BuildRequires: libjpeg-devel libtiff-devel libpng-devel libmspack-devel zlib-devel
BuildRequires: libgtk+3-devel libcairo-devel

BuildRequires: libXxf86vm-devel libbfd-devel
BuildRequires: libstdc++-devel
#BuildRequires: libGConf-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libnotify-devel
BuildRequires: libcurl-devel

%if_with webkitgtk
BuildRequires: libwebkit2gtk-devel
%endif

%if_with sdl
BuildRequires: libSDL2-devel
%endif

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This is a GTK+ port.

%package -n libwxBase%wxbranch
Summary: Non-GUI support classes from the wxWidgets library
Group: System/Libraries
Conflicts: lib%name < %EVR

%description -n libwxBase%wxbranch
Every wxWidgets application must link against this library. It contains
mandatory classes that any wxWidgets code depends on (like wxString) and
portability classes that abstract differences between platforms. wxBase can
be used to develop console mode applications -- it does not require any GUI
libraries or the X Window System.

%package -n libwxBase%wxbranch-devel
Group: Development/C++
Summary: Development files for the wxBase3 library
Requires: libwxBase%wxbranch = %EVR
Conflicts: lib%name-devel < %EVR
Conflicts: libwxGTK2.9-devel
Conflicts: libwxGTK3.0-devel
Conflicts: libwxGTK3.1-devel
Conflicts: libwxBase3.0-devel
Conflicts: libwxBase3.1-devel
Conflicts: wxGTK-devel
Conflicts: libwxGTK-devel

%description -n libwxBase%wxbranch-devel
This package include files needed to link with the wxBase3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n lib%name
Summary: The GTK+ port of the wxWidgets library
Group: System/Libraries
Requires: libwxBase%wxbranch = %EVR

%description -n lib%name
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%package -n lib%name-gl
Summary: OpenGL add-on for the wxWidgets library
Group: System/Libraries
Requires: lib%name = %EVR
Conflicts: lib%name < %EVR

%description -n lib%name-gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n lib%name-webview
Summary: WebView add-on for the wxWidgets library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-webview
WebView add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n lib%name-sound_sdlu
Summary: sound_sdlu add-on for the wxWidgets library
Group: System/Libraries
Requires: libwxBase%wxbranch = %EVR

%description -n lib%name-sound_sdlu
sound_sdlu add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n lib%name-media
Summary: Multimedia add-on for the wxWidgets library
Group: System/Libraries
Requires: lib%name = %EVR
Conflicts: lib%name < %EVR

%description -n lib%name-media
Multimedia add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n lib%name-devel
Summary: Development files for wxGTK library
Group: Development/C++
Requires: lib%name = %EVR
Requires: lib%name-gl = %EVR
Requires: lib%name-media = %EVR
Requires: libwxBase%wxbranch-devel = %EVR
%if_with webkitgtk
Requires: lib%name-webview = %EVR
%endif
%if_with sdl
Requires: lib%name-sound_sdlu = %EVR
%endif
%add_python_req_skip utils

%description -n lib%name-devel
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%package i18n
Summary: i18n message catalogs for the wxWidgets library
Group: Development/C++
BuildArch: noarch

%description i18n
i18n message catalogs for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package examples
Summary: wxGTK example programs
Group: Development/C++
BuildArch: noarch
Requires: lib%name-devel = %EVR

%description examples
wxGTK example programs.

%prep
%setup
tar -xf %SOURCE1 -C 3rdparty/
tar -xf %SOURCE2 -C 3rdparty/
tar -xf %SOURCE3 -C 3rdparty/

%autopatch -p1

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|bakefile/presets|bakefile/presets-\$(WX_RELEASE)|g' Makefile.in

rm -fR src/{expat,jpeg,tiff,zlib,png}

%build
CONF_FLAG=" \
	--enable-option-checking\
	--enable-shared \
	--with-zlib=sys \
	--with-expat=sys \
	--enable-display \
	--with-libjpeg=sys \
	--with-libpng=sys \
	--with-libtiff=sys \
	--with-opengl \
%if_with sdl
	--with-sdl \
%endif
	--enable-unicode \
	--enable-optimise \
	--with-regex=yes \
	--disable-rpath \
	--disable-joystick \
	--enable-webrequest \
	--enable-plugins \
	--enable-precomp-headers=yes \
	--enable-mediactrl \
	--enable-sound \
	--enable-stc \
	--enable-gui \
	--enable-graphics_ctx \
	--with-libmspack \
	--disable-stl \
	--enable-ipv6 \
	--with-subdirs"

./autogen.sh
export LIBS="-lX11"
DEFS="-DUNICODE=1 -DwxUSE_UNICODE=1"
%add_optflags -fno-strict-aliasing -std=gnu++11 $GST_CFLAGS $DEFS

%configure $CONF_FLAG \
	--with-gtk=3 \
%if_with webkitgtk
	--enable-webview
%endif
	%nil
%make_build

%make -C locale allmo

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/wx-%wxbranch/examples/src
cp -a demos samples %buildroot%_datadir/wx-%wxbranch/examples

cp -fR include/wx/private %buildroot%_includedir/wx-%wxbranch/wx/
cp -fR include/wx/unix/private %buildroot%_includedir/wx-%wxbranch/wx/unix/

%find_lang wxstd-3.2 wxmsw32 --output=wxstd.lang

# https://bugzilla.altlinux.org/47593
ln -s %_bindir/wx-config %buildroot%_bindir/wx-config-%wxbranch

%files -n libwxBase%wxbranch
%_libdir/libwx_baseu-*.so.*
%_libdir/libwx_baseu_net-*.so.*
%_libdir/libwx_baseu_xml-*.so.*
%dir %_libdir/wx

%files -n libwxBase%wxbranch-devel
%_bindir/wx-config
%_bindir/wxrc
%_bindir/wxrc-%wxbranch
%_bindir/wx-config-%wxbranch
%_includedir/wx-%wxbranch
%_libdir/libwx_baseu*.so
%dir %_libdir/wx
%dir %_libdir/wx/config
%dir %_libdir/wx/include
%_datadir/aclocal/wxwin.m4
%_datadir/bakefile/presets-%wxbranch
#_libexecdir/%name

%if_with sdl
%files -n lib%name-sound_sdlu
%dir %_libdir/wx/%wxbranch
%_libdir/wx/%wxbranch/sound_sdlu-*.so
%endif

%if_with webkitgtk
%files -n lib%name-webview
%dir %_libdir/wx/%wxbranch
%_libdir/libwx_gtk3u_webview-*.so.*
%_libdir/wx/%wxbranch/web-extensions
%endif

%files -n lib%name
%doc docs/changes.txt docs/gpl.txt docs/lgpl.txt docs/licence.txt
%doc docs/licendoc.txt docs/preamble.txt docs/readme.txt
%_libdir/libwx_gtk3u_adv-*.so.*
%_libdir/libwx_gtk3u_aui-*.so.*
%_libdir/libwx_gtk3u_core-*.so.*
%_libdir/libwx_gtk3u_html-*.so.*
%_libdir/libwx_gtk3u_propgrid-*.so.*
%_libdir/libwx_gtk3u_qa-*.so.*
%_libdir/libwx_gtk3u_ribbon-*.so.*
%_libdir/libwx_gtk3u_richtext-*.so.*
%_libdir/libwx_gtk3u_stc-*.so.*
%_libdir/libwx_gtk3u_xrc-*.so.*
%if_with webkitgtk
%exclude %_libdir/libwx_gtk3u_webview-*.so.*
%endif

%files -n lib%name-gl
%_libdir/libwx_gtk3u_gl-*.so.*

%files -n lib%name-media
%_libdir/libwx_gtk3u_media-*.so.*

%files -n lib%name-devel
%_libdir/libwx_gtk3u_*.so
%_libdir/wx/config/gtk3-unicode-%wxbranch
%_libdir/wx/include/gtk3-unicode-%wxbranch

%files i18n -f wxstd.lang

%files examples
%_datadir/wx-%wxbranch/examples

%changelog
* Mon Sep 09 2024 Anton Midyukov <antohami@altlinux.org> 3.2.6-alt1
- new stable release 3.2.6

* Tue May 14 2024 Anton Midyukov <antohami@altlinux.org> 3.2.5-alt1
- new stable release 3.2.5

* Sun Nov 12 2023 Anton Midyukov <antohami@altlinux.org> 3.2.4-alt1
- new stable release 3.2.4

* Tue Oct 10 2023 Anton Midyukov <antohami@altlinux.org> 3.2.3-alt1
- new stable release 3.2.3

* Fri Sep 15 2023 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt3
- add %%_bindir/wx-config-%%wxbranch for compatibilty with Fedora
  (Closes: 47593)

* Mon Feb 13 2023 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt2
- Add upstream commit: Fix drawing of icons for non-root wxTreeCtrl items

* Fri Feb 10 2023 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt1
- new stable release 3.2.2

* Sun Sep 25 2022 Fr. Br. George <george@altlinux.org> 3.2.1-alt3
- enable webrequest via libcurl
- fix License field

* Mon Sep 19 2022 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt2
- add missing conflict with libwxBase3.1-devel, libwxGTK3.1-devel
  (Closes: 43824)

* Thu Sep 08 2022 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1
- new stable release 3.2.1

* Mon Jul 11 2022 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt3
- cleanup spec

* Fri Jul 08 2022 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt2
- drop multilib wrapper

* Fri Jul 08 2022 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt1
- new stable release 3.2.0
- cleanup spec

* Fri Apr 22 2022 Anton Midyukov <antohami@altlinux.org> 3.1.6-alt1
- new version 3.1.6

* Thu Jul 01 2021 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt1
- new version 3.1.5 (Closes: 40344)

* Sat May 02 2020 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2
- Disable compat gtk2

* Sun Apr 19 2020 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- new version 3.1.3

* Thu Jun 06 2019 Anton Midyukov <antohami@altlinux.org> 3.1.2-alt1
- new version 3.1.2

* Fri Apr 26 2019 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt4
- switches for build with webkitgtk, SDL
- add compat with wxGTK3.0

* Wed Apr 24 2019 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt3.1
- enable_option_checking (only warnings) (Closes: 36662)

* Mon Apr 01 2019 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt3
- New subpackage libwxGTK3.1-webview
- New subpackage libwxGTK3.1-sound_sdlu
- Fix build without compat

* Wed Jan 02 2019 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt2.2
- Fix /usr/bin/wx-config (create symlink)

* Mon Dec 31 2018 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt2.1
- Drop update-alternatives

* Wed Oct 24 2018 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt2
- Disabled build options: stl, std_containers, std_string_conv_in_wxstring

* Sat Aug 04 2018 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt1
- New version 3.1.1 (build of a tag) (ALT#33929)
- New separate packages compatible gtk2
- Build with SDL2
- Build with libwebkit2gtk (ALT#34923)

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt9
- remove python-module-PyDSTool requires from -devel subpackage (ALT bug 33882)

* Fri Mar 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.1.0-alt8
- Built against GStreamer 1.0.
- clearly mark to build with GCC/G++ 5.

* Mon Feb 29 2016 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt7
- New release
- Rename wxGTK3.0.spec to wxGTK3.1.spec

* Tue Feb 02 2016 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt6.git20150312
- Disabled ABI checking.

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt5.git20150312
- Rebuilt for new gcc5 C++11 ABI.

* Sat Jun 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt4.git20150312
- Rebuilt with gcc5

* Fri Mar 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt3.git20150312
- New snapshot

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt3.git20141228
- New snapshot

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt2.svn20140708
- Enabled compatibility with 2.8 (ALT #30419)

* Wed Jul 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.svn20140708
- New snapshot

* Sat Jun 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.svn20140505
- Version 3.1.0 (with GTK 3)

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.svn20131118
- Added missing headers

* Tue Nov 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.svn20131118
- Version 3.0.0

* Fri Jul 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.5-alt3.svn20130718
- New snapshot

* Tue Mar 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.5-alt3.svn20120816
- Built without libgnomeprintui and with libgtk+2

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.5-alt2.svn20120816
- Rebuilt with libpng15

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.5-alt1.svn20120816
- Version 2.9.5

* Thu May 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.4-alt1.svn20120523
- Version 2.9.4

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.3-alt1.svn20110723
- Version 2.9.3

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20110322
- New snapshot
- Enabled wxUSE_UNICODE
- Disabled wxDEBUG_LEVEL

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20110312.1
- wxMBConv::ToWChar: avoid segfault when destination is empty

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20110312
- New snapshot
- Built with libXxf86vm and libpng

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20101203.1
- Rebuilt for debuginfo

* Sat Dec 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20101203
- Rebuilt for soname set-versions
- New snapshot

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20101119
- New snapshot

* Mon Sep 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20100926
- New snapshot
- Added libGConf-devel and gst-plugins-devel into build requirements

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.2-alt1.svn20100803
- Version 2.9.2

* Thu Jul 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.1-alt1.svn20100628
- New snapshot
- Enabled wxMediaCtrl and INFOBAR

* Tue Apr 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.1-alt1.svn20100312.3
- Fixed build

* Tue Mar 16 2010 Boris Savelev <boris@altlinux.org> 2:2.9.1-alt1.svn20100312.2
- drop debug packages

* Sun Mar 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.1-alt1.svn20100312.1
- Fixed link path to wx-config

* Sat Mar 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.1-alt1.svn20100312
- Version 2.9.1
- Set examples package as noarch

* Thu Mar 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.9.0-alt3.svn20100227
- New snapshot

* Mon Nov 16 2009 Boris Savelev <boris@altlinux.org> 2:2.9.0-alt2
- build 4 config (shared, static, shared-debug, static-debug)

* Thu Oct 29 2009 Boris Savelev <boris@altlinux.org> 2:2.9.0-alt1
- new version (closes #22027)
- rename packages
- drop contribs

* Mon Oct 26 2009 Alexey Rusakov <ktirf@altlinux.org> 2:2.8.10-alt4
- fix name clash with GSocket in Glib 2.21+

* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 2:2.8.10-alt3
- build with build-in regex (enable wxRE_ADVANCED)

* Mon Aug 24 2009 Boris Savelev <boris@altlinux.org> 2:2.8.10-alt2
- Add workaround for new version script handling in binutils:
  expand symbol patterns in version scripts manually instead of relying on
  unstable binutins behavior (Sergey Vlasov) (closes #20451).

* Fri Aug 21 2009 Boris Savelev <boris@altlinux.org> 2:2.8.10-alt1
-  2.8.10.

* Thu Jun 11 2009 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2:2.8.9-alt2
-  fix #20328.

* Wed Dec 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2:2.8.9-alt1
-  2.8.9.

* Fri Jun 27 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2:2.8.8-alt1
-  2.8.8;
-  #16156 fix.

* Tue Mar 18 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.6-alt2
-  rebuild without gnome-vfs (fix #14665).

* Wed Oct 03 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.6-alt1
-  2.8.6.

* Tue Jul 31 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.4-alt1
-  2.8.4.

* Mon Apr 16 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.3-alt1
-  2.8.3.

* Wed Jan 31 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.1.cvs31012007-alt1
-  build cvs version (10x for stupid wxPython afftars);
-  enable compatibility for wxGTK 2.6.x (10x for stupid wxPython afftars);
-  build with OpenGL.

* Tue Dec 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.0-alt1
-  change name.

* Wed Nov 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.0rc1-alt1
-  2.8.0rc1.

* Thu Aug 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.01-alt1
-  2.7.0 testing release.

* Mon May 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.3-alt1
-  2.6.3.

* Tue Dec 13 2005 Anton D. Kachalov <mouse@altlinux.org> 2.6.1-alt1.2
- multilib fix

* Thu Sep 15 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.1-alt1.1
-  rebuild with new libpango.

* Mon Jun 13 2005 Andrey Astafiev <andrei@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Sat May 07 2005 Andrey Astafiev <andrei@altlinux.ru> 2.6.0-alt2
- Added contrib-ogl.

* Tue May 03 2005 Andrey Astafiev <andrei@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Apr 11 2005 Andrey Astafiev <andrei@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Sun Mar 20 2005 Andrey Astafiev <andrei@altlinux.ru> 2.5.4-alt2
- Added contib-gizmos.
- Added patch for compatibility with wxPython 2.5.4.1.

* Sat Feb 26 2005 Andrey Astafiev <andrei@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Thu Oct 28 2004 Andrey Astafiev <andrei@altlinux.ru> 2.5.3-alt2
- XRC files moved to main package.

* Wed Sep 15 2004 Andrey Astafiev <andrei@altlinux.ru> 2.5.3-alt1
- 2.5.3
- With this version of spec wxGTK will be built with gtk2 support.
- It is possible to build and install four different types of wxGTK.
- Dynamic linked libraries of any build version can coexists in system.
- Fixed build of examples.

* Sun Mar 28 2004 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.2-alt2
- Added XRC and STC libraries from contribs.
- Changed name from wxWindows to wxWidgets.

* Sun Sep 28 2003 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.2-alt1
- 2.4.2

* Mon Aug 25 2003 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.1-alt2
- Patched wxTooltip and wxToolbar.

* Fri Jun 20 2003 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.1-alt1
- 2.4.1
- Some corrections taken from PLD spec:
  * Examples moved to separate package.
  * Added aclocal file.

* Wed Mar 05 2003 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.0-alt3
- Some spec corrections taken from Yuri Sedunov's unstable version.
- Fixed wxGTK-devel package group.
- Removed OpenGL support.

* Thu Jan 16 2003 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.0-alt2
- Some minor spec changes (thanks to Oleg Gints).

* Mon Jan 13 2003 Andrey Astafiev <andrei@altlinux.ru> 1:2.4.0-alt1
- 2.4.0.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 1:2.2.9-alt1
- Rollback to stable branch 2.2.x.
- 2.2.9.

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Jun 27 2001 AEN <aen@logic.ru> 2.3.1-alt1
- new version

* Wed Jun 27 2001 AEN <aen@logic.ru> 2.2.7-alt1
- new version

* Tue Apr 03 2001 Rider <rider@altlinux.ru> alt2
- bugfix

* Tue Apr 03 2001 Rider <rider@altlinux.ru> alt1
- 2.2.6

* Sun Dec 17 2000 AEN <aen@logic.ru>
- adopted for RE

* Tue Dec 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.2-2mdk
- build for gcc-2.96

* Sun Sep 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.2-1mdk
- update to 2.2.2
- clean spec
- BM

* Sat Aug 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.0-1mdk
- fix symlink that broke this lib
- update to 2.2.0
- macros

* Sat May 27 2000 Vincent Danen <vdanen@linux-mandrake.com> 2.1.15-2mdk
- add --with-gtk, --without-odbc, --without-shared, --without-debug_flag,
  and --without-debug_info to configure

* Fri May 26 2000 Vincent Danen <vdanen@linux-mandrake.com> 2.1.15-1mdk
- initial specfile
- bzip sources

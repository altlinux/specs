%define wxbranch 3.0

Name: wxGTK3.0
Version: %wxbranch.3
Release: alt8.git20160409

Summary: The GTK+ port of the wxWidgets library
License: wxWidgets License
Group: System/Libraries
Url: http://wxwidgets.org

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wxWidgets/wxWidgets.git
# branch: WX_3_0_BRANCH
Source: %name-%version.tar
Source2: ld_shared_wrapper.pl

Patch1: wxGTK3-3.0.2-abicheck.patch
Patch2: wxGTK3-3.0.2-gstreamer1.0.patch

BuildRequires: gcc-c++
BuildRequires: libGL-devel libGLU-devel libSDL-devel libSM-devel
BuildRequires: libX11-devel libXinerama-devel libICE-devel libXmu-devel libXext-devel libXp-devel
BuildRequires: xorg-xextproto-devel xorg-inputproto-devel libXtst-devel
BuildRequires: libexpat-devel
BuildRequires: libjpeg-devel libtiff-devel libpng-devel libmspack-devel zlib-devel
BuildRequires: libgtk+3-devel libcairo-devel

BuildRequires: libXxf86vm-devel libbfd-devel
BuildRequires: libstdc++-devel
BuildRequires: libGConf-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libnotify-devel libwebkitgtk3-devel

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
Requires: python-module-PyDSTool
%add_python_req_skip utils
Conflicts: libwxGTK2.9-devel
Conflicts: wxGTK-devel
Conflicts: libwxGTK-devel

%description -n lib%name-devel
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%package examples
Summary: wxGTK example programs
Group: Development/C++
BuildArch: noarch
Requires: lib%name-devel = %EVR

%description examples
wxGTK example programs.

%prep
%setup
%patch1 -p1
%patch2 -p1

# patch some installed files to avoid conflicts with 2.8.*
#sed -i -e 's|aclocal)|aclocal/wxwin3.m4)|' Makefile.in
sed -i -e 's|wxstd.mo|wxstd30.mo|' Makefile.in
sed -i -e 's|wxmsw.mo|wxmsw30.mo|' Makefile.in
sed -i -e 's|bakefile/presets|bakefile/presets-\$(WX_RELEASE)|g' Makefile.in

# fix plugin dir for 64-bit
sed -i -e 's|/usr/lib\b|%{_libdir}|' wx-config.in configure
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp

%build
CONF_FLAG="--enable-shared --without-debug_flag --without-debug_info"

./autogen.sh
export LIBS="-lX11"
DEFS="-DUNICODE=1 -DwxUSE_UNICODE=1"
%add_optflags -fno-strict-aliasing -std=gnu++11 $GST_CFLAGS $DEFS
%configure $CONF_FLAG \
	--with-zlib=sys \
	--with-expat=sys \
	--enable-display \
	--with-libjpeg=sys \
	--with-libpng=sys \
	--with-libtiff=sys \
	--with-opengl \
	--with-sdl \
	--enable-unicode \
	--enable-optimise \
	--with-regex=yes \
	--disable-rpath \
	--without-odbc \
	--disable-joystick \
	--enable-plugins \
	--enable-precomp-headers=yes \
	--enable-compat26 \
	--enable-compat28 \
	--with-gtk=3 \
	--enable-soname \
	--enable-mediactrl \
	--enable-sound \
	--enable-webview \
	--enable-stc \
	--enable-gui \
	--with-xresources \
	--without-gnomeprint \
	--enable-graphics_ctx \
	--enable-utf8=yes \
	--enable-utf8only=no \
	--with-libmspack \
	--enable-stl \
	--enable-std_containers \
	--enable-std_string_conv_in_wxstring \
	--enable-ipv6 \
	--enable-no_deps \
	--with-subdirs

#%make_build SHARED_LD_CXX='perl %SOURCE2 $(CXX) -shared -fPIC -g -o'
%make_build
%make -C locale allmo

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/wx-%wxbranch/examples/src
cp -a demos samples %buildroot%_datadir/wx-%wxbranch/examples

wx_config_filename=$(basename %buildroot%_libdir/wx/config/*-unicode-[0-9]*)
ln -sf ../..%_libdir/wx/config/$wx_config_filename %buildroot%_bindir/wx-config

cp -fR include/wx/private %buildroot%_includedir/wx-%wxbranch/wx/
cp -fR include/wx/unix/private %buildroot%_includedir/wx-%wxbranch/wx/unix/

%find_lang wxstd3
%find_lang wxmsw3
cat wxmsw3.lang >> wxstd3.lang

%files -f wxstd3.lang -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libwx_baseu*.so.*
%exclude %_libdir/libwx_gtk3u_gl-*.so.*
%exclude %_libdir/libwx_gtk3u_media-*.so.*

%files -n libwxBase%wxbranch
%_libdir/libwx_baseu*.so.*

%files -n lib%name-gl
%_libdir/libwx_gtk3u_gl-*.so.*

%files -n lib%name-media
%_libdir/libwx_gtk3u_media-*.so.*

%files -n lib%name-devel
%_libdir/wx/config/gtk3-unicode-%wxbranch
%dir %_libdir/wx/include/gtk3-unicode-%wxbranch
%_libdir/wx/include/gtk3-unicode-%wxbranch/wx
%doc docs/*
%dir %_datadir/bakefile
%_datadir/bakefile/*
%_bindir/*
%_libdir/wx/*
%_datadir/aclocal/*.m4
%_includedir/wx-%wxbranch
%_libdir/*.so

%files examples
%_datadir/wx-%wxbranch/examples

%changelog
* Fri Mar 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.3-alt8.git20160409
- Built against GStreamer 1.0.
- removed old gst1.0 patch.

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 3.0.3-alt7.git20160409
- git snapshot 59078ab5456c8383257a226ae88a446b60800af9
- revert aclocal/wxwin.m4 name

* Tue Apr 05 2016 Alexey Shabalin <shaba@altlinux.ru> 3.0.3-alt6.git20160401
- git snapshot of WX_3_0_BRANCH with fixes for wayland
- update BR:
- split package to libwxBase3.1,libwxGTK3.0,libwxGTK3.0-gl,libwxGTK3.0-media

* Thu Oct 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.3-alt5.git20150312
- Disabled ABI checking.

* Thu Oct 29 2015 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt4.git20150312
- Rebuilt for new gcc5 C++11 ABI.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt3.git20150312
- Added %_bindir/wxrc-3.0 (ALT #31197)

* Fri Jul 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt2.git20150312
- Rebuilt with gcc5

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.git20150312
- Version 3.0.3
- Built with gtk3 instead of gtk2

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

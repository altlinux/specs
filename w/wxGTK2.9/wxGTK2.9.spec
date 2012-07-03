%define wxbranch 2.9
%define ucode u
%def_disable debug
%def_enable unicode

%if_disabled unicode
%define ucode %{-E}
%endif

Name: wxGTK2.9
Version: %wxbranch.4
Release: alt1.svn20120523
Epoch: 2

Summary: The GTK+ port of the wxWidgets library
License: wxWidgets License
Group: System/Libraries
Url: http://wxwidgets.org

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source2: ld_shared_wrapper.pl

# Automatically added by buildreq on Wed Dec 10 2008
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSM-devel
BuildRequires: libXinerama-devel libesd-devel libexpat-devel
BuildRequires: libgnomeprintui-devel libjpeg-devel libtiff-devel

BuildPreReq: xorg-xextproto-devel xorg-inputproto-devel libXtst-devel
BuildPreReq: rpm-build-java libXxf86vm-devel
BuildPreReq: libstdc++-devel gstreamer-devel gst-plugins-devel
BuildPreReq: libGConf-devel gst-plugins-devel libpng-devel

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This is a GTK+ port.

%package -n lib%name
Summary: The GTK+ port of the wxWidgets library
Group: System/Libraries

%description -n lib%name
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%package -n lib%name-devel
Summary: Development files for wxGTK library
Group: Development/C++
Requires: lib%name = %epoch:%version-%release
Requires: python-module-PyDSTool
%add_python_req_skip utils
Conflicts: wxGTK2-devel
Conflicts: wxGTK-devel
Conflicts: libwxGTK-devel
Conflicts: wxGTK2u-devel

%description -n lib%name-devel
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%package -n lib%name-devel-static
Summary: The GTK+ port of the wxWidgets library
Group: Development/C++
Requires: lib%name-devel = %epoch:%version-%release

%description -n lib%name-devel-static
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%if_enabled debug
%package -n lib%name-debug
Summary: The GTK+ port of the wxWidgets library build with debug
Group: System/Libraries

%description -n lib%name-debug
Debug library for wxGTK, the GTK+ port of the wxWidgets library.

%package -n lib%name-debug-devel
Summary: Development files for wxGTK library
Group: Development/C++
Requires: lib%name-debug = %epoch:%version-%release
Requires: lib%name = %epoch:%version-%release

%description -n lib%name-debug-devel
Development files for wxGTK, the GTK+ port of the wxWidgets library.

%package -n lib%name-debug-devel-static
Summary: The GTK+ port of the wxWidgets library
Group: Development/C++
Requires: lib%name-debug-devel = %epoch:%version-%release

%description -n lib%name-debug-devel-static
Static library for wxGTK, the GTK+ port of the wxWidgets library.
%endif

%package examples
Summary: wxGTK example programs
Group: Development/C++
BuildArch: noarch
Requires: lib%name-devel = %epoch:%version-%release

%description examples
wxGTK example programs.

%prep
%setup
subst "s,bakefile/presets,bakefile/presets-\$(WX_RELEASE),g" Makefile.in

%build
%if_enabled debug
DIRS="shared_release shared_debug static_release static_debug"
%else
DIRS="shared_release static_release"
%endif
for dist in $DIRS ; do
    case $dist in
	shared_release)
	    CONF_FLAG="--enable-shared --without-debug_flag --without-debug_info"
	;;
	shared_debug)
	    CONF_FLAG="--enable-shared --enable-debug"
	;;
	static_release)
	    CONF_FLAG="--disable-shared --without-debug_flag --without-debug_info"
	;;
	static_debug)
	    CONF_FLAG="--disable-shared --enable-debug"
	;;
    esac

./autogen.sh
mkdir $dist && cd $dist
%define _configure_script ../configure
GST_CFLAGS="$(pkg-config --cflags gstreamer-0.10)"
export LIBS="-lX11"
DEFS="-DUNICODE=1 -DwxUSE_UNICODE=1 -DwxUSE_UNICODE_UTF8=1"
%add_optflags -fno-strict-aliasing $GST_CFLAGS $DEFS
%configure $CONF_FLAG \
	--with-sdl \
	--enable-unicode \
	--enable-optimise \
	--with-regex=yes \
	--disable-rpath \
	--without-subdirs \
	--without-odbc \
	--with-opengl \
	--disable-joystick \
	--enable-plugins \
	--enable-precomp-headers=yes \
	--enable-compat26 \
	--enable-gtk2=yes \
	--enable-sound \
	--enable-soname \
	--enable-mediactrl \
	--enable-stc \
	--enable-gui \
	--with-xresources \
	--without-gnomeprint \
	--enable-graphics_ctx

%make_build SHARED_LD_CXX='perl %SOURCE2 $(CXX) -shared -fPIC -g -o'
cd ..
done

%install
%if_enabled debug
DIRS="shared_debug static_release static_debug shared_release"
%else
DIRS="static_release shared_release"
%endif
for dist in $DIRS ; do
  %makeinstall_std -C $dist
done
mkdir -p %buildroot%_datadir/wx/examples/src
cp -a demos samples %buildroot%_datadir/wx/examples

wx_config_filename=$(basename %buildroot%_libdir/wx/config/*-unicode-[0-9]*)
ln -sf ../..%_libdir/wx/config/$wx_config_filename %buildroot%_bindir/wx-config

%files -n lib%name
%_libdir/libwx_base%ucode-%wxbranch.so.*
%_libdir/libwx_base%{ucode}_net-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_adv-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_aui-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_richtext-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_core-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_html-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_xrc-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_qa-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_gl-%wxbranch.so.*
%_libdir/libwx_base%{ucode}_xml-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_stc-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_propgrid-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_ribbon-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_media-%wxbranch.so.*

%files -n lib%name-devel
%_libdir/wx/config/gtk2-unicode-%wxbranch
%dir %_libdir/wx/include/gtk2-unicode-%wxbranch
%_libdir/wx/include/gtk2-unicode-%wxbranch/wx
%doc docs/*
%dir %_datadir/bakefile
%_datadir/bakefile/*
%_bindir/*
%_libdir/wx/%version/sound_sdl%ucode-%version.so
%_datadir/aclocal/*.m4
%dir %_includedir/wx-%wxbranch
%dir %_includedir/wx-%wxbranch/wx
%_includedir/wx-%wxbranch/wx/generic
%_includedir/wx-%wxbranch/wx/gtk
%_includedir/wx-%wxbranch/wx/html
%_includedir/wx-%wxbranch/wx/protocol
%_includedir/wx-%wxbranch/wx/unix
%_includedir/wx-%wxbranch/wx/xrc
%_includedir/wx-%wxbranch/wx/propgrid
%_includedir/wx-%wxbranch/wx/persist
%_includedir/wx-%wxbranch/wx/meta
%_includedir/wx-%wxbranch/wx/*.h
%_includedir/wx-%wxbranch/wx/*.cpp
%_includedir/wx-%wxbranch/wx/aui
%_includedir/wx-%wxbranch/wx/richtext
%_includedir/wx-%wxbranch/wx/xml
%_includedir/wx-%wxbranch/wx/stc
%_includedir/wx-%wxbranch/wx/ribbon
%_libdir/libwx_base%{ucode}-%wxbranch.so
%_libdir/libwx_base%{ucode}_net-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_adv-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_core-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_html-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_aui-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_richtext-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_gl-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_xrc-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_qa-%wxbranch.so
%_libdir/libwx_base%{ucode}_xml-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_stc-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_propgrid-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_ribbon-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_media-%wxbranch.so

%files -n lib%name-devel-static
%_libdir/wx/config/gtk2-unicode-static-%wxbranch
%dir %_libdir/wx/include/gtk2-unicode-static-%wxbranch
%_libdir/wx/include/gtk2-unicode-static-%wxbranch/wx
%_libdir/libwx_base%{ucode}-%wxbranch.a
%_libdir/libwx_base%{ucode}_net-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_adv-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_core-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_html-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_aui-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_richtext-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_gl-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_xrc-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_qa-%wxbranch.a
%_libdir/libwx_base%{ucode}_xml-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_stc-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_propgrid-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_ribbon-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}_media-%wxbranch.a
%_libdir/libwxregex%{ucode}-%wxbranch.a
%_libdir/libwxscintilla-%wxbranch.a

%if_enabled debug
%files -n lib%name-debug
%_libdir/libwx_base%{ucode}d-%wxbranch.so.*
%_libdir/libwx_base%{ucode}d_net-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_adv-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_aui-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_richtext-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_core-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_html-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_xrc-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_qa-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_gl-%wxbranch.so.*
%_libdir/libwx_base%{ucode}d_xml-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_stc-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_propgrid-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}d_ribbon-%wxbranch.so.*

%files -n lib%name-debug-devel
%_libdir/wx/%version/sound_sdl%{ucode}d-%version.so
%_libdir/libwx_base%{ucode}d-%wxbranch.so
%_libdir/libwx_base%{ucode}d_net-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_adv-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_core-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_html-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_aui-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_richtext-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_gl-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_xrc-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_qa-%wxbranch.so
%_libdir/libwx_base%{ucode}d_xml-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_stc-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_propgrid-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}d_ribbon-%wxbranch.so

%files -n lib%name-debug-devel-static
%_libdir/libwx_base%{ucode}d-%wxbranch.a
%_libdir/libwx_base%{ucode}d_net-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_adv-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_core-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_html-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_aui-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_richtext-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_gl-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_xrc-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_qa-%wxbranch.a
%_libdir/libwx_base%{ucode}d_xml-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_stc-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_ribbon-%wxbranch.a
%_libdir/libwx_gtk2%{ucode}d_propgrid-%wxbranch.a
%_libdir/libwxregex%{ucode}d-%wxbranch.a
#_libdir/libwxscintillad-%wxbranch.a
%endif

%files examples
%_datadir/wx/examples

%changelog
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

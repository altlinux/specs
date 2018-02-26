%define wxbranch 2.8
%define ucode u
%def_enable unicode

%if_disabled unicode
%define ucode %{-E}
%endif

Name: wxGTK
Version: %wxbranch.11.0
Release: alt1.svn20100628.5
Serial:	2

Summary: The GTK+ port of the wxWidgets library
License: wxWidgets License
Group: System/Libraries
Url: http://wxwidgets.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
Source2: ld_shared_wrapper.pl

BuildPreReq: gcc-c++ libGL-devel libSDL-devel libSM-devel
BuildPreReq: libXinerama-devel libesd-devel libexpat-devel
BuildPreReq: libgnomeprintui-devel libjpeg-devel libtiff-devel
BuildPreReq: rpm-build-java libXt-devel gstreamer-devel
BuildPreReq: libGConf-devel gst-plugins-devel

BuildPreReq: libstdc++-devel

Requires: lib%name = %version-%release

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This is a GTK+ port.

%package -n lib%name
Summary: Shared libraries of the GTK+ port of the wxWidgets
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains shared libraries of a GTK+ port.

%package -n lib%name-doc
Summary: Documentation for wxGTK library
Group: Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description -n lib%name-doc
Documentation for wxGTK, the GTK+ port of the wxWidgets library.

%package -n lib%name-devel
Summary: Development files for wxGTK library
Group: Development/C++
Provides: %name-devel = %version-%release
Conflicts: %name-devel < %version-%release
Obsoletes: %name-devel < %version-%release
Requires: %name = %version-%release
Conflicts: wxGTK2-devel
Conflicts: wxGTK2u-devel

%description -n lib%name-devel
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%package examples
Summary: wxGTK example programs
Group: Development/C++
BuildArch: noarch
Requires: %name-devel = %version
COnflicts: wxGTK2.9-examples
Conflicts: wxGTK2u-examples

%description examples
wxGTK example programs.

%package -n lib%name-contrib-stc
Summary: wxWidgets styled text control library
Group: System/Libraries
Provides: %name-contrib-stc = %version-%release
Conflicts: %name-contrib-stc < %version-%release
Obsoletes: %name-contrib-stc < %version-%release
Requires: %name = %version-%release

%description -n lib%name-contrib-stc
wxWidgets styled text control library.

%package -n lib%name-contrib-stc-devel
Summary: Development files for wxWidgets styled text control library
Group: Development/C++
Provides: %name-contrib-stc-devel = %version-%release
Conflicts: %name-contrib-stc-devel < %version-%release
Obsoletes: %name-contrib-stc-devel < %version-%release
Requires: %name-contrib-stc = %version-%release

%description -n lib%name-contrib-stc-devel
Header files for wxWidgets styled text control library.

%package -n lib%name-contrib-gizmos
Summary: wxWidgets cell and canvas layout objects
Group: System/Libraries
Provides: %name-contrib-gizmos = %version-%release
Conflicts: %name-contrib-gizmos < %version-%release
Obsoletes: %name-contrib-gizmos < %version-%release
Requires: %name = %version-%release

%description -n lib%name-contrib-gizmos
wxWidgets cell and canvas layout objects.

%package -n lib%name-contrib-gizmos-devel
Summary: Development files for wxWidgets cell and canvas layout objects
Group: Development/C++
Provides: %name-contrib-gizmos-devel = %version-%release
Conflicts: %name-contrib-gizmos-devel < %version-%release
Obsoletes: %name-contrib-gizmos-devel < %version-%release
Requires: %name-contrib-gizmos = %version-%release

%description -n lib%name-contrib-gizmos-devel
Header files for wxWidgets cell and canvas layout objects.

%package -n lib%name-contrib-ogl
Summary: wxWidgets object graphics library
Group: System/Libraries
Provides: %name-contrib-ogl = %version-%release
Conflicts: %name-contrib-ogl < %version-%release
Obsoletes: %name-contrib-ogl < %version-%release
Requires: %name = %version-%release

%description -n lib%name-contrib-ogl
wxWidgets' Object Graphics Library (OGL) is a C++ library supporting the
creation and manipulation of simple and complex graphic images on a canvas.

%package -n lib%name-contrib-ogl-devel
Summary: Development files for wxWidgets object graphics library
Group: Development/C++
Provides: %name-contrib-ogl-devel = %version-%release
Conflicts: %name-contrib-ogl-devel < %version-%release
Obsoletes: %name-contrib-ogl-devel < %version-%release
Requires: %name-contrib-ogl = %version-%release

%description -n lib%name-contrib-ogl-devel
Header files for wxWidgets object graphics library.

%prep
%setup
subst "s,bakefile/presets,bakefile/presets-\$(WX_RELEASE),g" Makefile.in

%build
./autogen.sh
%configure --without-odbc \
	 --without-debug_flag \
	 --without-debug_info \
	 --with-opengl \
	 --disable-joystick \
	 --enable-plugins \
	 --enable-precomp-headers=yes \
	 --enable-compat26 \
	 --with-xresources \
	 --enable-optimise \
	 --enable-shared \
	 --enable-unicode \
	 --enable-gtk2=yes \
	 --enable-soname \
	 --enable-mediactrl \
	 --with-gnomeprint \
	 --with-sdl \
	 --with-regex=yes

%make_build SHARED_LD_CXX='perl %SOURCE2 $(CXX) -shared -fPIC -g -o'

pushd contrib
%make_build SHARED_LD_CXX='perl %SOURCE2 $(CXX) -shared -fPIC -g -o'
popd

%install

%makeinstall_std

ln -s %_libdir/wx/include/gtk2-unicode-release-%wxbranch/wx/setup.h \
	%buildroot%_includedir/wx-%wxbranch/wx
install -m644 version-script \
	%buildroot%_libdir/wx/config

pushd contrib
%makeinstall_std
#ln -s %_libdir/libwx_gtk2%{ucode}_mmedia-%wxbranch.so \
#	%buildroot%_libdir/libwx_gtk2%{ucode}_media-%wxbranch.so
popd

install -d %buildroot%_datadir/wx/examples/src
cp -a demos samples %buildroot%_datadir/wx/examples
for i in $(find %buildroot%_datadir/wx/examples -name Makefile)
do
	sed -i 's|^\(wx_top_builddir\).*|\1 =|' $i
	sed -i 's|^\(SAMPLES_RPATH_FLAG\).*|\1 =|' $i
	sed -i 's|^\(COND_wxUSE_REGEX_builtin___LIB_REGEX_p.*\)|#\1|' $i
	sed -i 's|^\(LIBDIRNAME\).*|\1 = %_libdir|' $i
	sed -i 's|^\(CXXFLAGS.*\)|\1 -I%_includedir/wx-%wxbranch|' $i
	sed -i 's|^\(CPPFLAGS.*\)|\1 -I%_includedir/wx-%wxbranch|' $i
	sed -i 's|\(/version\-script\)|%_libdir/wx/config\1|' $i
done

install -d %buildroot%_docdir/%name-%version
cp -fR docs/* %buildroot%_docdir/%name-%version/

%find_lang wxstd2%ucode

%files -f wxstd2%ucode.lang
%_datadir/bakefile/

%files -n lib%name
%_libdir/libwx_base%{ucode}-%wxbranch.so.*
%_libdir/libwx_base%{ucode}_net-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_adv-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_aui-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_richtext-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_core-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_html-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_mmedia-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_media-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_xrc-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_qa-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_fl-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_plot-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_svg-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_gl-%wxbranch.so.*
%if "%wxbranch" >= "2.5"
%_libdir/libwx_base%{ucode}_xml-%wxbranch.so.*
%endif

%files -n lib%name-doc
%doc %_docdir/%name-%version/

%files -n lib%name-devel
%_bindir/*
%_libdir/libwx_base%{ucode}-%wxbranch.so
%_libdir/libwx_base%{ucode}_net-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_adv-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_core-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_html-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_aui-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_richtext-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_fl-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_plot-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_svg-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_gl-%wxbranch.so
%_libdir/wx/%{wxbranch}/sound_sdl-%{wxbranch}.so
%_libdir/libwx_gtk2%{ucode}_mmedia-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_media-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_xrc-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_qa-%wxbranch.so
%if_enabled unicode
%_libdir/wx/config/gtk2-unicode-release-%wxbranch
%dir %_libdir/wx/include/gtk2-unicode-release-%wxbranch
%_libdir/wx/include/gtk2-unicode-release-%wxbranch/wx
%else
%_libdir/wx/config/gtk2-ansi-release-%wxbranch
%dir %_libdir/wx/include/gtk2-ansi-release-%wxbranch
%_libdir/wx/include/gtk2-ansi-release-%wxbranch/wx
%endif
%_libdir/wx/config/version-script
%_datadir/aclocal/*.m4
%dir %_includedir/wx-%wxbranch
%dir %_includedir/wx-%wxbranch/wx
%_includedir/wx-%wxbranch/wx/generic
%_includedir/wx-%wxbranch/wx/gtk
%_includedir/wx-%wxbranch/wx/html
%_includedir/wx-%wxbranch/wx/protocol
%_includedir/wx-%wxbranch/wx/unix
%_includedir/wx-%wxbranch/wx/xrc
%_includedir/wx-%wxbranch/wx/*.h
%_includedir/wx-%wxbranch/wx/*.cpp
%_includedir/wx-%wxbranch/wx/aui
%_includedir/wx-%wxbranch/wx/richtext
%_includedir/wx-%wxbranch/wx/fl
%_includedir/wx-%wxbranch/wx/plot
%_includedir/wx-%wxbranch/wx/svg
%_includedir/wx-%wxbranch/wx/mmedia
%if "%wxbranch" >= "2.5"
%_includedir/wx-%wxbranch/wx/xml
%_libdir/libwx_base%{ucode}_xml-%wxbranch.so
%endif

%files -n lib%name-contrib-stc
%_libdir/libwx_gtk2%{ucode}_stc-%wxbranch.so.*

%files -n lib%name-contrib-stc-devel
%_libdir/libwx_gtk2%{ucode}_stc-%wxbranch.so
%_includedir/wx-%wxbranch/wx/stc

%files -n lib%name-contrib-gizmos
%_libdir/libwx_gtk2%{ucode}_gizmos-%wxbranch.so.*
%_libdir/libwx_gtk2%{ucode}_gizmos_xrc-%wxbranch.so.*

%files -n lib%name-contrib-gizmos-devel
%_libdir/libwx_gtk2%{ucode}_gizmos-%wxbranch.so
%_libdir/libwx_gtk2%{ucode}_gizmos_xrc-%wxbranch.so
%_includedir/wx-%wxbranch/wx/gizmos

%files -n lib%name-contrib-ogl
%_libdir/libwx_gtk2%{ucode}_ogl-%wxbranch.so.*

%files -n lib%name-contrib-ogl-devel
%_libdir/libwx_gtk2%{ucode}_ogl-%wxbranch.so
%_includedir/wx-%wxbranch/wx/ogl

%files examples
%_datadir/wx/examples

%changelog
* Tue Mar 15 2011 Michael Shigorin <mike@altlinux.org> 2:2.8.11.0-alt1.svn20100628.5
- NMU: rebuilt with rpm-4.0.4-alt100.23 to fix broken requires

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100628.4
- Rebuilt for debuginfo

* Sat Dec 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100628.3
- Rebuilt for soname set-versions

* Wed Oct 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100628.2
- Fixed underlinking with libX11

* Mon Sep 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100628.1
- Added libGConf-devel and gst-plugins-devel into build requirements
  (ALT #24158)

* Sun Jul 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100628
- New snapshot

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100227.1
- Enabled wxMediaCtrl

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.11.0-alt1.svn20100227
- Version 2.8.11.0

* Thu Jan 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.10.1-alt1.svn20100111.1
- Fixed build of media library
- Added missing development files
- Extracted docs into separate package
- Fixed examples' makefiles
- Deleted unused upstream files from branch `master'
- Avoided repocop's warnings

* Tue Jan 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.8.10.1-alt1.svn20100111
- Version 2.8.10.1

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

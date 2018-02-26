%global __strip %_mingw32_strip
%global __objdump %_mingw32_objdump

%define wxbranch 2.8
%define ucode u
%define oname wxGTK
%def_enable unicode

%if_disabled unicode
%define ucode %{-E}
%endif

Name: mingw32-wxGTK
Version: 2.8.10
Release: alt5

Summary: The GTK+ port of the wxWidgets library
License: wxWidgets License
Group: System/Libraries
Url: http://wxwidgets.org

Packager: Boris Savelev <boris@altlinux.org>

Source: %oname-%version.tar.gz
Source2: ld_shared_wrapper.pl
Patch: changeset_r60875.diff
Patch1: changeset_r60876.diff
#Source: %name-2007-01-31.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Sat Sep 19 2009
BuildRequires: mingw32-dlfcn mingw32-gcc-c++ mingw32-libjpeg mingw32-libpng mingw32-pthreads mingw32-SDL
BuildRequires: rpm-build-mingw32 mingw32-libtiff mingw32-expat

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This is a GTK+ port.

%package static
Summary: wxWidgets static library
Group: System/Libraries
Requires: %name = %version-%release

%description static
wxWidgets static librarary

%package debug
Summary: wxWidgets debug library
Group: System/Libraries
Requires: %name = %version-%release

%description debug
wxWidgets debug librarary

%package static-debug
Summary: wxWidgets static static library
Group: System/Libraries
Requires: %name = %version-%release

%description static-debug
wxWidgets static debug librarary

%prep
%setup -q -n %oname-%version
%__subst "s,bakefile/presets,bakefile/presets-\$(WX_RELEASE),g" Makefile.in
%patch0 -p0
%patch1 -p0

%build
#========= Shared Libraries ==========
for dist in shared_release shared_debug static_release static_debug ; do
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

mkdir $dist && cd $dist
%_mingw32_configure $CONF_FLAG \
	--with-msw \
	--with-sdl \
	--enable-unicode \
	--enable-optimise \
	--with-regex=yes \
	--disable-rpath \
	--without-subdirs \
	--without-odbc \
	--without-opengl \
	--disable-joystick \
	--enable-plugins \
	--enable-precomp-headers=yes \
	--enable-compat26 \
	--enable-gtk2=yes \
	--enable-soname \
	--without-gnomeprint

%make_build SHARED_LD_CXX='perl %SOURCE2 $(CXX) -shared -fPIC -o'
cd ..
done

%install
for dist in shared_release shared_debug static_release static_debug ; do
%makeinstall_std -C $dist
done
if ls %buildroot%_mingw32_libdir/*.dll ; then
  mv %buildroot%_mingw32_libdir/*.dll %buildroot%_mingw32_bindir
else
  echo "No shared libraries found."
fi

# we need to modify the absolute wx-config link to be relative or rpm complains
# (and our package wouldn't be relocatable)
wx_config_filename=$(basename %buildroot%_mingw32_libdir/wx/config/%_mingw32_target-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename %buildroot%_mingw32_bindir/wx-config

rm -rf %buildroot%_mingw32_datadir/bakefile

%files
%doc docs/*
%_mingw32_bindir/wx-config
%_mingw32_bindir/wx*28u_*.dll
%_mingw32_libdir/wx
%exclude %_mingw32_libdir/wx/config/%_mingw32_target-*-static-*
%exclude %_mingw32_libdir/wx/config/%_mingw32_target-*-debug-*
%_mingw32_includedir/wx-%wxbranch
%_mingw32_datadir/aclocal/*.m4

%files static
%_mingw32_libdir/libwx*u_*.dll.a
%_mingw32_libdir/libwx*u-*.a
%_mingw32_libdir/libwx*u_*.a
%_mingw32_libdir/wx/config/%_mingw32_target-*-static-*
%exclude %_mingw32_libdir/wx/config/%_mingw32_target-*-debug-*

%files debug
%_mingw32_bindir/wx*28ud_*.dll
%_mingw32_libdir/wx/config/%_mingw32_target-*-debug-*
%exclude %_mingw32_libdir/wx/config/%_mingw32_target-*-static-*

%files static-debug
%_mingw32_libdir/libwx*ud_*.dll.a
%_mingw32_libdir/libwx*ud-*.a
%_mingw32_libdir/libwx*ud_*.a
%_mingw32_libdir/wx/config/%_mingw32_target-*-static-*
%exclude %_mingw32_libdir/wx/config/%_mingw32_target-*-release-*

%changelog
* Wed Sep 23 2009 Boris Savelev <boris@altlinux.org> 2.8.10-alt5
- drop contribs
- build 4 config (shared, static, shared-debug, static-debug)
- build with system libtiff
- build with system expat

* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 2.8.10-alt4
- version up

* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 2.8.10-alt1
- build for mingw32

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


Name:          awesome
Version:       4.3.1753
Release:       alt0.1
Group:         Graphical desktop/Other
License:       GPLv2

Url:           https://awesomewm.org/
Vcs:           https://github.com/awesomeWM/awesome.git
Source:        %name-%version.tar
Source1:       %name.wmsession
Source2:       %name.menu-method
Source3:       awesome.rockspec.in
Patch:         rpm-install.patch
Summary:       A window manager initialy based on a dwm code rewriting

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-rocks
BuildRequires(pre): rpm-build-xdg
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: asciidoctor
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: ImageMagick-tools
BuildRequires: lua >= 5.5
BuildRequires: xmlto
BuildRequires: libcairo-gobject
BuildRequires: libgdk-pixbuf-gir
BuildRequires: libpango-gir
BuildRequires: cmake(lua) >= 5.5
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.79.2
BuildRequires: pkgconfig(imlib2)
BuildRequires: pkgconfig(libev)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libxdg-basedir) >= 1.0.0
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-icccm) >= 0.3.8
BuildRequires: pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires: pkgconfig(xcb-util) >= 0.3.8
BuildRequires: pkgconfig(xcb-xrm)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: rocks(lgi) >= 0.8.0
BuildRequires: rocks(luarocks)

Requires:      libstartup-notification >= 0.10-alt1
Requires:      rocks(awesome) = 4.3.1753

%description
awesome is a window manager initialy based on a dwm code rewriting. It's
extremely fast, small, dynamic and awesome.


%package       -n rock-awesome
Summary:       Lua library for the Awesome window manager
Group:         System/Libraries
BuildArch:     noarch
Requires:      libcairo-gobject
Requires:      libgdk-pixbuf-gir
Requires:      libpango-gir
Requires:      typelib(GioUnix) = 2.0

%description   -n rock-awesome
Lua modules that run inside the Awesome window manager.


%prep
%setup
%autopatch -p1

%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DLUA_EXECUTABLE=%_bindir/lua5.5 \
   -DLUA_INCLUDE_DIR=%_includedir/lua5.5 \
   -DLUA_LIBRARY=%_libdir/liblua-5.5.so \
   -DCOMPRESS_MANPAGES=OFF \
   -DSYSCONFDIR=%_sysconfdir \
   -DXDG_CONFIG_DIR=%_xdgconfigdir \
   -DROCK_VERSION=%version-%rock_revision \
   -DROCK_LIBEXECDIR=%rock_libexecdir \
   -DROCK_SPECDIR=%rock_specdir \
   -DROCK_SPEC_TEMPLATE=%SOURCE3 \
   -DROCK_LUAROCKS=%_bindir/luarocks-%rock_lua_version \
   -DALT_DESKTOP_DIR=%_desktopdir \
   -DALT_WMSESSION=%SOURCE1 \
   -DALT_MENU_METHOD=%SOURCE2
%cmake_build

%install
%cmake_install
%find_lang %name

%check
%ctest


%files         -f %name.lang
%_bindir/*
%_sysconfdir/menu-methods/%name
%dir %_xdgconfigdir/%name
%config(noreplace) %_xdgconfigdir/%name/rc.lua
%config(noreplace) %_xdgconfigdir/%name/menu.lua
%_sysconfdir/X11/wmsession.d/*
%_man1dir/aw*
%_man5dir/aw*
%_mandir/*/man1/aw*
%_mandir/*/man5/aw*
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/xsessions/%name.desktop
%_defaultdocdir/%name
%doc LICENSE README.md

%files         -n rock-awesome
%doc LICENSE
%rock_libexecdir/*
%exclude %dir %rock_specdir


%changelog
* Wed Nov 18 2026 Pavel Skrylev <majioa@altlinux.org> 4.3.1753-alt0.1
- ^ 4.3 -> 4.3p1753
- + added the rock-awesome Lua library package, including ruled.
- * built with Lua 5.5 and enabled LGI.
- * configured the rockspec and installed ALT integration files with CMake.
- * checked the staged files and rock metadata with CTest.
- * generated the LGI requirement from the rockspec.
- ! fixed startup with the default configuration and current GLib (ALT#56677).

* Wed May 13 2026 Pavel Skrylev <majioa@altlinux.org> 4.3-alt6.1
- * moved build to lua5.4
- - disabled LGI to fix FTBFS

* Sat Jul 19 2025 Pavel Skrylev <majioa@altlinux.org> 4.3-alt6
- ! fixed FTBFS
- * cleanup spec
- * rewritten cmake build proc

* Wed Mar 08 2023 L.A. Kostis <lakostis@altlinux.ru> 4.3-alt5
- NMU update:
  + cmake: use full lua binary path (and fix FTBFS).
  + use rpm-build-licenses and fix License.
  + filter out self provides for lua modules.

* Fri Mar 12 2021 Slava Aseev <ptrnine@altlinux.org> 4.3-alt4
- Fix build with gcc-10

* Sat Jun  1 2019 Terechkov Evgenii <evg@altlinux.org> 4.3-alt3
- Add /usr/share/xsessions/awesome.desktop (ALT#36830)

* Thu Apr  4 2019 Terechkov Evgenii <evg@altlinux.org> 4.3-alt2
- Add libgdk-pixbuf-gir to Requires (ALT#36499)

* Fri Feb 22 2019 Terechkov Evgenii <evg@altlinux.org> 4.3-alt1
- 4.3 (Too Long)

* Thu Aug 24 2017 Terechkov Evgenii <evg@altlinux.org> 4.2-alt1
- 4.2 (Human after all)

* Mon Mar 20 2017 Terechkov Evgenii <evg@altlinux.org> 4.1-alt1
- 4.1 (Technologic)

* Fri Feb 24 2017 Terechkov Evgenii <evg@altlinux.org> 4.0-alt1
- 4.0 (Harder, Better, Faster, Stronger)

* Sat Jan 28 2017 Terechkov Evgenii <evg@altlinux.org> 3.5.9-alt3
- Fix build

* Mon Oct 17 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.9-alt2
- Rebuild with lua5.3

* Mon Mar 21 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.9-alt1
- 3.5.9 (Mighty Ravendark)

* Sun Jan 31 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.8-alt1
- 3.5.8 (Major Tom)

* Mon Jan 18 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.7-alt1
- 3.5.7 (Space Oddity)

* Mon Jan 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.5.6-alt1
- 3.5.6 (For Those About To Rock)

* Tue Apr 22 2014 Terechkov Evgenii <evg@altlinux.org> 3.5.5-alt1
- 3.5.5 (Kansas City Shuffle)

* Fri Apr  4 2014 Terechkov Evgenii <evg@altlinux.org> 3.5.4-alt1
- 3.5.4

* Sun Mar 30 2014 Terechkov Evgenii <evg@altlinux.org> 3.5.3-alt1
- 3.5.3 (Crazy)

* Fri Nov 15 2013 Terechkov Evgenii <evg@altlinux.org> 3.5.2-alt1
- 3.5.2 (The Fox)

* Wed Apr 10 2013 Terechkov Evgenii <evg@altlinux.org> 3.5.1-alt1
- 3.5.1 (Ruby Tuesday)

* Mon Jan 21 2013 Terechkov Evgenii <evg@altlinux.org> 3.5-alt4
- We need libcairo-gobject

* Mon Dec 24 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt3
- Oops. Adding missing requires

* Sat Dec 22 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt2
- 3.5 (Last Christmas)

* Tue Dec 18 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt1.rc2
- 3.5-rc2 (I'll Kill Her)

* Tue Dec  4 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt1.rc1
- 3.5-rc1 (Dirty Magic)

* Wed Oct  3 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.13-alt2
- Set default background according to WM Policy 1.1

* Sun Sep  9 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.13-alt1
- 3.4.13 (Octopus)

* Sun Sep  2 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.12-alt1
- 3.4.12 (Starlight)

* Fri Apr  6 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.10-alt2
- Fix FTBFS with new glib

* Wed May 25 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.10-alt1
- 3.4.10 (Exploder)

* Sat May 14 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.9-alt3
- Manpages fixed in spec (thanks to legion@)
- git-20110508

* Sat Apr  9 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.9-alt2
- Fix build with new cmake (Dirty hack)

* Thu Jan 20 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.9-alt1
- 3.49 (Smack)

* Thu Dec  2 2010 Terechkov Evgenii <evg@altlinux.org> 3.4.8-alt1
- 3.4.8 (Never Know)

* Thu Sep 16 2010 Terechkov Evgenii <evg@altlinux.org> 3.4.7-alt1
- 3.4.7 (Left Of Center)

* Mon Jul 19 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.6-alt1
- 3.4.6 (Hooch)

* Wed May 19 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.5-alt1
- 3.4.5 (Close To You)

* Wed Mar 10 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.4-alt1
- 3.4.4 (Jet Sex)

* Tue Feb 23 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.3-alt2
- Lets conform to ALT Linux IconPathPolicy: http://www.altlinux.org/IconPathsPolicy

* Wed Jan  6 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.3-alt1
- 3.4.3 (Engines)

* Sun Dec 27 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4.2-alt1
- 3.4.2 (For The Restless)

* Wed Oct 21 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt4
- 3.4 (Closing In)

* Mon Oct 19 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt3.rc3
- Set minimal required libstartup-notification (ALT#21983, thanks to wrar@, barabashka@)

* Sat Oct 10 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt2.rc3
- 3.4-rc3 (Black Star)

* Mon Sep 28 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt2.rc2
- 3.4-rc2 (Piku)

* Sun Sep 27 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt2.rc1
- Default config fixed

* Sat Sep 26 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt1.rc1
- 3.4-rc1 (Uprising)

* Sat Sep 19 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.4-alt2
- Sources cleanup (thanks to kas@)

* Wed Sep  9 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.4-alt1
- 3.3.4 (Mercury)

* Sun Aug 30 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.3-alt1
- 3.3.3 (Firelight)

* Wed Aug  5 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.2-alt1
- 3.3.2 (Half Moon)

* Fri Jul 17 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.1-alt2
- Generic X error format message fixed

* Thu Jul 16 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Tue Jun 16 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3-alt2
- Ignore size hints by default, @kas
- git-20090616

* Thu Jun  4 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3-alt1
- 3.3

* Fri May 29 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt4
- Rebuild with libxcb-1.3

* Sun Apr 26 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt3
- ALT-specific patch extracted
- Buildrequires updated
- git-20090426 from upstream (to work with libxcbutil-0.3.4)
- Version stamp now updated correctly
- Dependency to gxmessage suppressed

* Sat Apr 25 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt2
- Rebuild with libxcbutil-0.3.4

* Tue Apr 21 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Sat Mar 14 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2-alt2
- 3.2

* Mon Feb 23 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2-alt1.rc3
- 3.2-rc3

* Thu Jan 22 2009 Terechkov Evgenii <evg@altlinux.ru> 3.1.1-alt3
- srpm->git migration (thanks, kas@)
- Substitute "+" to "_" in section name (kas@, c78693654a5639759decb3c606a3adb98311ed57)

* Fri Jan 16 2009 Terechkov Evgenii <evg@altlinux.ru> 3.1.1-alt2
- Patch0 added to set default background image loader to xsetroot (see #18514)

* Tue Jan 13 2009 Terechkov Evgenii <evg@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sun Dec 21 2008 Terechkov Evgenii <evg@altlinux.ru> 3.1-alt2
- Debian-menu generation added

* Tue Dec 16 2008 Terechkov Evgenii <evg@altlinux.ru> 3.1-alt1
- 3.1

* Sun Nov 16 2008 Terechkov Evgenii <evg@altlinux.ru> 3.0-alt2
- Update spec to new filetriggers system

* Sun Oct 12 2008 Terechkov Evgenii <evg@altlinux.ru> 3.0-alt1
- Initial build for ALT Linux Sisyphus (Thanks OpenSuSE for spec)

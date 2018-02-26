%define svnrev 269

%def_enable nls
%def_enable gpm
%def_enable mp3
%def_enable audiocd
%def_enable ogg
%def_enable alsa
%def_enable disk_writer
%def_enable oss
%def_enable threads

%define Name MPFC
Name: mpfc
%define lname lib%name
Version: 1.3.8
Release: alt0.5.qa2
Summary: %Name is music player for console
License: %gpl2plus
Group: Sound
URL: http://%name.sourceforge.net
%ifdef svnrev
Source: %name-svn-r%svnrev.tar
%else
Source: %name-%version.tar
%endif
Patch: %name-svn-r269-alt.patch
Patch1: %name-1.3.8-alt-DSO.patch
Requires: %lname = %version-%release
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Wed Sep 24 2008
#BuildRequires: libalsa-devel libgpm-devel libmad-devel libncursesw-devel libvorbis-devel

BuildRequires: cvs libncursesw-devel gettext-tools
%{?_enable_gpm:BuildRequires: libgpm-devel}
%{?_enable_mp3:BuildRequires: libmad-devel}
%{?_enable_ogg:BuildRequires: libvorbis-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}

%description
%Name is an abbrevation for Music Player For Console.
It is a full-featured curses-based playlist-oriented player.
%Name has vi-style key bindings.


%package -n %lname
Summary: Shared libraries of %Name
Group: System/Libraries

%description -n %lname
%Name is an abbrevation for Music Player For Console.
It is a full-featured curses-based playlist-oriented player.
This package contains shared libraries of %Name.


%package -n %lname-devel
Summary: %Name is music player for console (development files)
Group: Development/C
Requires: %lname = %version-%release
Requires: libncursesw-devel
Obsoletes: %name-devel < %version-%release
Provides: %name-devel = %version-%release

%description -n %lname-devel
%Name is an abbrevation for Music Player For Console.
It is a full-featured curses-based playlist-oriented player.
This package contains files for development with %lname.


%prep
%setup %{?svnrev:-n %name-svn-r%svnrev}
%patch -p1
%patch1 -p2


%build
%set_automake_version 1.10
#set_autoconf_version 2.5

%define _optlevel 3
sh ./autogen.sh
%configure \
    --disable-static \
    --enable-shared \
    %{subst_enable nls} \
%if_enabled threads
    --enable-threads=posix \
%else
    --disable-threads \
%endif
    %{subst_enable gpm} \
    %{subst_enable mp3} \
    %{subst_enable audiocd} \
    %{subst_enable ogg} \
    %{subst_enable alsa} \
    %{subst_enable disk_writer} \
    %{subst_enable oss} \
    --with-pic \
    --with-gnu-ld
%make_build
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot%_libdir/%name/general
%find_lang %name




%files -f %name.lang
%doc AUTHORS ChangeLog.* NEWS README
%_bindir/*
%config(noreplace) %_sysconfdir/*
%dir %_libdir/%name/general
%dir %_libdir/%name/input
%dir %_libdir/%name/output
%_libdir/%name/input/*.so
%_libdir/%name/output/*.so
%_man1dir/*
%_infodir/*


%files -n %lname
%_libdir/*.so.*


%files -n %lname-devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*


%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.8-alt0.5.qa2
- Fixed build

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.8-alt0.5.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 28 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.8-alt0.5
- update requires

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.8-alt0.4
- Rebuild 
- remove old macros

* Wed Nov 12 2008 Led <led@altlinux.ru> 1.3.8-alt0.3
- new SVN snapshot (revision 269)

* Thu Oct 16 2008 Led <led@altlinux.ru> 1.3.8-alt0.2
- cleaned up spec
- added dir for 'general' plugins

* Wed Sep 24 2008 Led <led@altlinux.ru> 1.3.8-alt0.1
- new SVN snapshot (revision 268)
- fixed License
- removed %name-1.3.7-alt-gcc41.patch (fixed in upstrem)
- updated %name-svn-r268-makefile.patch
- added mpfc-svn-r268-alt.patch

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 1.3.7-alt3
- fixed %%_libdir/mpfc stuff for x86_64
- use "-release %%version" libtool flags for libmpfc/libmpfcwnd
  and "-avoid-version" for plugins

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 1.3.7-alt2
- fixed gcc-4.1 issues
- linked input/output plugins with libmpfc and libmpfcwnd
- intoduced mpfc-devel subpackage
- using ALSA output plugin by default

* Wed Apr 19 2006 Alexey Tourbin <at@altlinux.ru> 1.3.7-alt1
- 1.3.6 -> 1.3.7
- fixed linkage
- alsa output is possibly broken, using oss by default

* Fri Sep 23 2005 Alexey Tourbin <at@altlinux.ru> 1.3.6-alt1
- 1.3.5 -> 1.3.6

* Fri Jan 07 2005 Alexey Tourbin <at@altlinux.ru> 1.3.5-alt1
- 1.3.3 -> 1.3.5

* Sat Oct 16 2004 Alexey Tourbin <at@altlinux.ru> 1.3.3-alt1
- 1.2-8 -> 1.3.3
- applied a patch from the author that fixes mouse initialization
- built with esd output plugin

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 1.2.8-alt1
- 1.2-4 -> 1.2-8
- util_strncpy.patch merged upstream

* Fri Mar 05 2004 Alexey Tourbin <at@altlinux.ru> 1.2.4-alt1
- 1.2-4
- alt-set-m_tail.patch merged upstream
- alt-util_strncpy.patch: fixed strcpy(3) inside util_strncpy()

* Sat Feb 28 2004 Alexey Tourbin <at@altlinux.ru> 1.2.2-alt1
- 1.2-2
- alt-set-m_tail.patch: fixed a bug in linked list processing

* Sun Feb 15 2004 Alexey Tourbin <at@altlinux.ru> 1.2-alt1
- 1.2
- non-pic code stuff fixed upstream
- use `libtool -release' to set SONAMEs according to package version

* Wed Feb 04 2004 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt1.1
- added dependencies on install/uninstall-info
- better fix for non-pic code (convenience libtool libraries)

* Tue Feb 03 2004 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt1
- updated to 1.1.1
- fixed non-pic code in plugins
- static libraries and .la files not packaged
- info page packaged
- description updated
- cleanup_spec applied

* Mon Oct 27 2003 Alexey Voinov <voins@altlinux.ru> 1.0-alt1
- new version (1.0)

* Wed Oct 15 2003 Alexey Voinov <voins@altlinux.ru> 0.3-alt1
- initial build

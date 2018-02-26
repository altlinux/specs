%undefine __libtoolize
%define _keep_libtool_files 1
%define _optlevel s

%define qtdir %_qt3dir
%define kdedir %_K3prefix

%def_with gstreamer

Name: kaffeine
Version: 0.8.8
%define beta %nil
Release: alt7

Group: Video
Summary: A Xine-based Media Player for KDE
License: GPL
Url: http://kaffeine.sourceforge.net/

Requires: kdelibs >= %{get_version kdelibs}
Requires: lib%{name} = %version-%release
Requires: %name-engine >= %version-%release

Source: %name-%version%beta.tar.bz2
# FC
Patch1: acinclude.patch
# ALT
Patch2: kaffeine-0.8.4-alt-ru.patch
Patch3: kaffeine-0.8.4-alt-without-xcb.patch
Patch4: kaffeine-0.8.7-alt-desktop.patch
Patch5: kaffeine-0.8.7-alt-i18n-ru-servicemenus.patch
Patch6: kaffeine-0.8.7-alt-dont-replace-percent.patch
Patch7: kaffeine-0.8.8-alt-fix-compile.patch
Patch8: kaffeine-0.8.8-alt-automake.patch
Patch9: tde-3.5.13-build-defdir-autotool.patch
Patch10: kaffeine-0.8.8-mp3InputPlugBuild.patch

# Automatically added by buildreq on Tue Jun 23 2009 (-bi)
#BuildRequires: doxygen gcc-c++ gcc-fortran graphviz gst-plugins-devel imake kdepim-devel libXt-devel libXtst-devel libcdio-devel libjpeg-devel liblame-devel libxine-devel qt3-designer qt3-doc-html rpm-build-ruby xml-utils xorg-cf-files xorg-inputproto-devel
BuildRequires(pre): kdelibs-devel
BuildRequires: doxygen gcc-c++ graphviz kdepim-devel libpng-devel
BuildRequires: libcdio-devel libjpeg-devel liblame-devel libxine-devel xml-utils
%if_with gstreamer
BuildRequires: gst-plugins-devel
%endif

%description
Kaffeine is a Xine-based Media Player for QT/KDE

%package -n lib%{name}
Group: System/Libraries
Summary: Base libraries for %name
Requires: kdelibs >= %{get_version kdelibs}
Conflicts: kaffeine < 0.8
%description -n lib%{name}
Base libraries for %name

%package -n lib%{name}-devel
Group: Development/KDE and QT
Summary: Headers and development files for lib%{name}
Requires: lib%{name} = %version-%release
%description -n lib%{name}-devel
Headers and development files for lib%{name}

%package engine-xine
Group: Video
Summary: Kaffeine Xine player part
Provides: %name-engine = %version-%release
Requires: lib%{name} = %version-%release
Conflicts: kaffeine <= 0.8.5-alt3
%description engine-xine
A Kaffeine engine based on xine.

%package engine-gstreamer
Group: Video
Summary: Kaffeine GStreamer player part
Provides: %name-engine = %version-%release
Requires: lib%{name} = %version-%release
Requires: gst-ffmpeg gst-plugins-alsa gst-plugins-base-audio-filters gst-plugins-base-video-filters
Requires: gst-plugins-good-audio-formats gst-plugins-good-container-formats gst-plugins-good-tags
Requires: gst-plugins-good-video-filters gst-plugins-lame gst-plugins-mad gst-plugins-ogg
Requires: gst-plugins-theora gst-plugins-vorbis gst-plugins-xvideo
%description engine-gstreamer
A Kaffeine engine based on GStreamer.

%prep
%setup -q -n %name-%version%beta
#%patch1 -p0
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch9
%patch10 -p1

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%prefix
export PATH=%qtdir/bin:%kdedir/bin:$PATH
%K3configure \
    --disable-debug \
    %{subst_with gstreamer} \
    --disable-gcc-hidden-visibility \
    --with-xinerama
#    --without-xcb \
#    --with-xinit-workaround \

%make_build

%install
%K3install PACKAGE=%name

%K3find_lang --with-man --with-kde %name

%files -n lib%{name}
%_K3libdir/lib*%{name}*.so*

%files -n lib%{name}-devel
%_K3libdir/lib*%{name}*.la
%_K3lib/libxinepart.la
%_K3lib/lib*%{name}*.la
%_K3includedir/%{name}*

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO kaffeine/README.* kaffeine/CREDITS kaffeine/BUGS
#%_man1dir/*
#
%_K3bindir/%name
%_K3lib/lib*%{name}*.so*
#
%_K3xdg_apps/%name.desktop
%_K3mimelnk/application/*%{name}*.desktop
%_K3srv/*%{name}*.desktop
%_K3srvtyp/*%{name}*.desktop
#
%_K3apps/%name
%exclude %_K3apps/%name/xine_part.rc
%_K3apps/profiles/*
%_K3apps/konqueror/servicemenus/*.desktop
#
%_kde3_iconsdir/hicolor/*/apps/*.png
%_kde3_iconsdir/*/*/actions/*.png
%_kde3_iconsdir/*/*/mimetypes/*%{name}*.png

%files engine-xine
%_K3lib/libxinepart.so*
%_K3apps/%name/xine_part.rc
%_K3srv/xine_part.desktop

%if_with gstreamer
%files engine-gstreamer
%_K3lib/libgstreamerpart.so*
%_K3apps/gstreamerpart
%_K3srv/gstreamer_part.desktop
%endif

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.8.8-alt7
- Build for TDE 3.5.13 release

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt6
- fix build requires

* Fri Mar 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt5
- move to alternate place

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt4
- fix to build

* Wed Mar 10 2010 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt3
- fix compile with new autotools

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt2
- rebuilt with new libcdio

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt1
- new version
- built with xcb

* Wed Nov 12 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt3
- fix to play URLs with non-latin path

* Wed Oct 01 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt2
- translate service menus to russian

* Wed Aug 06 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt1
- new version

* Tue Jan 22 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.6-alt1
- new version
- fix gstreamer requires; thanks shrek@alt

* Fri Sep 28 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.5-alt4
- built with gstreamer; thanks shrek@alt

* Wed Aug 29 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.5-alt3
- fix desktop categories

* Tue Aug 28 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.5-alt2
- add upstream fix against CD encoding crash

* Wed Aug 01 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.5-alt1
- new version
- built with libxine-devel mimetype list support

* Wed May 23 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.4-alt4
- force build without xcb

* Tue May 15 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.4-alt3
- rebuilt for xcb support

* Fri May 04 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.4-alt2
- small i18n-ru fix

* Mon Apr 16 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.4-alt1
- new version

* Fri Jan 12 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt1
- new version

* Mon Sep 11 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.2-alt1
- new version
- built without xinit workaround

* Fri Jul 14 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.2-alt0.1.beta1
- 0.8.2-beta1

* Tue Jul 11 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt2
- rebuilt

* Wed Apr 19 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- new version

* Mon Mar 27 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt1
- new version

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt1
- fix compile with new binutils

* Thu Sep 08 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt0.1
- new version

* Wed Aug 24 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7-alt0.1
- new version

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.3b-alt3.1
- Rebuilt with libstdc++.so.6.

* Sat Jun 5 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3b-alt3
- remove kaffeineplugin.so requires from package

* Fri May 28 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3b-alt2
- fixed kaffeineplugin.so file bug

* Fri May 14 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3b-alt1
- moved mozilla-plugin in CVS module kaffeine-mozilla
- removed superkaramba example
- font encoding fix (xine-lib uses now utf8 by default)
- fixed broken icons for KDE 3.2

* Tue May 11 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3-alt2
- rebuild with gcc-3.3

* Tue May 4 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3-alt1
- 0.4.3
- finally fixed the crash after closing with xfree 4.4/X.org 6.7
- kaffeine uses now the tvtime plugin for deinterlacing
- fixed compiler errors with gcc 3.3.3
- playlist window shortcuts are now also configurable

* Thu Mar 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.2-alt1
- 0.4.2
- control panel layout improved (fixed jerking time button)
- playlist track info dialog improved + click on info icon opens it
- playlist status bar shows total entries + total play time
- fixed conflicts with installation files of KDE 3.2

* Sun Jan 18 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.4.1-alt1
- 0.4.1
- new command line switch --verbose to output xine debug messages
- support for xine messages added (popup)
- support for mouse wheel added
- support for network broadcasting

* Sat Dec 13 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4-alt3
- cleanup spec file

* Fri Nov 21 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4-alt2
- improve .spec by Sergey V Turchin
- fix requires
- fix menu to be with mimetypes
- add patch to don't ask about link mozilla plugin

* Mon Nov 17 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4-alt1
- 0.4 release
- add cmd line option --enqueue to append files to current playlist
- handbook updated
- bookmark-entrys may now be playlists
- new titles (maybe from internet broadcast) now OS displayed
- add equalizer

* Sun Oct 12 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4-alt0.1.beta1
- 0.4beta1
- plays now local *.wma files
- add a right-click context menu for minimal- and fullscreen-mode
- add a minimal mode (hides control-panel and menu)
- add small context menu for playlist entries
- resolved startup problems
- bugs fixed

* Sun Jun 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt1
- First version of RPM package.


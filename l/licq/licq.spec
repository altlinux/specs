%define lIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define lIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define lIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define lIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

# define names and paths of QT/KDE packages
%define glibc_core_ver %{get_version glibc-core}

%define _optlevel s
%define socks 0
%define cvs 0
%define no_some_docs 1

%define with_email 1
%define with_console 0
%define with_auto_reply 1
%define with_rms 1
%define with_qt4 1
%define with_kde4 1
%define with_gtk 0
%define with_osd 1
%define with_aosd 1
%define with_gpg 1
%define with_msn 1
%define with_jabber 1

# name-version-release
%define rname licq
%define ver 1.6.0
%define rlz alt3

Name: %rname
Version: %ver
Release: %rlz

BuildRequires(pre): kde4libs-devel
BuildRequires: freetype2-devel gcc-c++ chrpath
BuildRequires: libart_lgpl-devel libexpat-devel libjpeg-devel
BuildRequires: liblcms-devel libmng-devel kde-common-devel
BuildRequires: libncurses-devel libssl-devel libstdc++-devel libtinfo-devel
BuildRequires: rpm-utils boost-devel doxygen libgloox-devel
%if %with_console
BuildRequires: libcdk-devel
%endif
%if %with_qt4
BuildRequires: libqt4-devel
%endif
%if %with_kde4
BuildRequires: kde4libs-devel
%endif
%if %socks
BuildRequires: libdante-devel
%endif
%if %with_gtk
BuildRequires: libgtk+2-devel
%endif
%if %with_osd
BuildRequires: libxosd-devel cvs
%endif
%if %with_aosd
BuildRequires: libaosd-devel glib2-devel
%endif
%if %with_gpg
BuildRequires: libgpgme-devel libgpg-error-devel
%endif

########################
Source: %name.tar
%if %with_auto_reply
#Source1: ftp://ftp.licq.org/pub/licq/plugins/%name-auto-reply-%%cvsdate.tar
%endif
%if %with_gtk
Source5: ftp://ftp.licq.org/pub/licq/plugins/icqnd-0.1.9.6.tar
%endif

########################

Source9: licq-tracepath.utility
Source10: licq-viewurl.sh
Source21: %name.16.xpm.bz2
Source22: %name.32.xpm.bz2
Source23: %name.48.xpm.bz2

Patch2: licq-1.5.0-alt-xvt.patch
Patch3: licq-1.5.0-alt-qt4-def-encoding.patch
#
Patch17: licq_osd_plugin-1.3.2.1-defaults.patch
#
Patch22: licq-1.3.6-alt-qt4-yes-stl.patch

Patch200: licq-1.2.7-remove-pidfile.patch


#package licq
Group: Networking/Instant messaging
Summary: ICQ clone written in C++
License: GPL
Url: http://www.licq.org/
Requires: %name-jabber = %version-%release
%if %with_osd
Requires: %name-osd = %version-%release
%endif
%if %with_kde4
Requires: %name-kde4 = %version-%release
%else
Requires: %name-ui
%endif


%package maxi
Group: Networking/Instant messaging
Summary: ICQ clone written in C++
%if %with_msn
Requires: %name-msn = %version-%release
%endif
%if %with_jabber
Requires: %name-jabber = %version-%release
%endif
%if %with_email
Requires: %name-email = %version-%release
%endif
%if %with_auto_reply
Requires: %name-autoreply = %version-%release
%endif
%if %with_rms
Requires: %name-rms = %version-%release
%endif
%if %with_osd
Requires: %name-osd = %version-%release
%endif
%if %with_aosd
Requires: %name-aosd = %version-%release
%endif
%if %with_qt4
Requires: %name-qt4 = %version-%release
%else
Requires: %name-ui
%endif
%if %with_kde4
Requires: %name-kde4 = %version-%release
%else
Requires: %name-ui
%endif
%if %with_gtk
Requires: %name-gtk = %version-%release
%else
Requires: %name-ui
%endif
%if %with_console
Requires: %name-console = %version-%release
%else
Requires: %name-ui
%endif

%package mini
Group: Networking/Instant messaging
Summary: ICQ clone written in C++
%if %with_qt4
Requires: %name-qt4 = %version-%release
%else
Requires: %name-ui
%endif

%package common
Summary: Common binaries and data files  for Licq
Group: Networking/Instant messaging
Obsoletes: %name-ssl < %version-release
Obsoletes: %name-data < %version-release
Obsoletes: %name-update-hosts < %version-release
Provides: %name-base = %version-release
Obsoletes: %name-base < %version-release
Requires: sound_handler

%package kde4
Group: Networking/Instant messaging
Summary: ICQ clone written in C++, and the default plugin for KDE4
Provides: %name-plugin %name-ui
Provides: licq-kde = %version-%release
Obsoletes: licq-kde < %version-%release
Requires: %name-common = %version-%release
Requires: kde4libs >= %{get_version kde4libs}
Requires: %name-qt4

%package qt4
Summary: Qt4 based GUI plugin  for %name
Group: Networking/Instant messaging
Provides: %name-plugin %name-ui
Provides: licq-qt = %version-%release
Obsoletes: licq-qt < %version-%release
Requires: %name-common = %version-%release
Requires: libqt4-core >= %{get_version libqt4-core}

%package gtk
Summary: GTK+ based GUI plugin  for %name
Group: Networking/Instant messaging
Provides: %name-plugin %name-ui
Requires: %name-common = %version-%release

%package console
Summary: Console based plugin for %name that uses ncurses
Group: Networking/Instant messaging
Provides: %name-plugin %name-ui
Requires: %name-common = %version-%release

%package email
Summary: Email forwarder plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin, %name-forwarder = %version-%release
Obsoletes: %name-forwarder < %version-%release
Requires: %name-common = %version-%release

%package autoreply
Summary: Autoreply Licq plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package rms
Summary: Remote management service plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package osd
Summary: OSD (On Screen Dysplay) plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package aosd
Summary: OSD (On Screen Dysplay) plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package icq
Summary: ICQ protocol plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package msn
Summary: MSN protocol plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package jabber
Summary: XMPP(Jabber) protocol plugin for %name
Group: Networking/Instant messaging
Provides: %name-plugin
Requires: %name-common = %version-%release

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name-common = %version-%release

%description maxi
Licq supports different interfaces and functions via plugins. Currently there are
plugins for both the X Windowing System and the console.

This package contains the base files for Licq (the Licq daemon) and the QT
plugin, which is written using the Qt widget set. Currently this GUI plugin has
most of the ICQ functions implemented.

This starts the QT plugin by default, so to run other plugins, you will have to
issue the command "licq -p <plugin>" once. To get back the Qt plugin, you will
have to run once "licq -p qt-gui". Alternatively you may be able to do it in a
plugin dialog box if your plugin supports this feature.

This version of licq has SSL support for those plugins that support it.
%description mini
Licq supports different interfaces and functions via plugins. Currently there are
plugins for both the X Windowing System and the console.

This package contains the base files for Licq (the Licq daemon) and the QT
plugin, which is written using the Qt widget set. Currently this GUI plugin has
most of the ICQ functions implemented.

This starts the QT plugin by default, so to run other plugins, you will have to
issue the command "licq -p <plugin>" once. To get back the Qt plugin, you will
have to run once "licq -p qt-gui". Alternatively you may be able to do it in a
plugin dialog box if your plugin supports this feature.

This version of licq has SSL support for those plugins that support it.
%description
Licq supports different interfaces and functions via plugins. Currently there are
plugins for both the X Windowing System and the console.

This package contains the base files for Licq (the Licq daemon) and the QT
plugin, which is written using the Qt widget set. Currently this GUI plugin has
most of the ICQ functions implemented.

This starts the QT plugin by default, so to run other plugins, you will have to
issue the command "licq -p <plugin>" once. To get back the Qt plugin, you will
have to run once "licq -p qt-gui". Alternatively you may be able to do it in a
plugin dialog box if your plugin supports this feature.

This version of licq has SSL support for those plugins that support it.

%description kde4
This is the KDE4 based GUI plugin for Licq.
Install this if you want a KDE4-based GUI for Licq.

%description common
Common binaries and data files  for Licq

%description devel
This is the header files that you will need in order to compile Licq plugins.

%description rms
RMS stands for the Remote Management Service. It is a plugin for Licq which
enables you to "telnet" to your Licq box to perform various tasks. Security is
implemented through basic username and password authentication.

%description qt4
This is the Qt4 based GUI for Licq.
Install this and if you want a Qt4-based GUI for Licq.

%description gtk
This is the GTK+ based GUI plugin for Licq.
Install this if you want a GTK+ based GUI for Licq.

%description console
This is a console based plugin for Licq that uses ncurses that came in the
standard Licq source package. It is extremely usable and functional, but it
does not currently have support for gpm.

Install this if you want to run Licq on the console.

%description email
This plugin for Licq lets you forward messages to your email account. This is a
plugin that came with the standard Licq source package. It can be run
concurrently with a UI plugin.

Install this if you want to add this function to Licq.

%description autoreply
This plugin for Licq enables Licq to auto reply to messages. This is a plugin
standard Licq source package. It can be run concurrently with a UI plugin.

Install this if you want to add this function to Licq.

%description osd
This is a small plugin, which uses libxosd2 to
display new arriving messages as OSD (On Screen Display)
text on your desktop.

Install this if you want to add this function to Licq.

%description aosd
This is a small plugin, which uses libaosd to
display new arriving messages as OSD (On Screen Display)
text on your desktop.

Install this if you want to add this function to Licq.

%description icq
ICQ Protocol Plugin.

Install this if you want to add this function to Licq.

%description msn
MSN Protocol Plugin.

Install this if you want to add this function to Licq.

%description jabber
Jabber(XMPP) Protocol Plugin.

Install this if you want to add this function to Licq.

%description maxi
Licq supports different interfaces and functions via plugins. Currently there are
plugins for both the X Windowing System and the console.

This package contains the base files for Licq (the Licq daemon) and the QT
plugin, which is written using the Qt widget set. Currently this GUI plugin has
most of the ICQ functions implemented.

This starts the QT plugin by default, so to run other plugins, you will have to
issue the command "licq -p <plugin>" once. To get back the Qt plugin, you will
have to run once "licq -p qt-gui". Alternatively you may be able to do it in a
plugin dialog box if your plugin supports this feature.

This version of licq has SSL support for those plugins that support it.
%description mini
Licq supports different interfaces and functions via plugins. Currently there are
plugins for both the X Windowing System and the console.

This package contains the base files for Licq (the Licq daemon) and the QT
plugin, which is written using the Qt widget set. Currently this GUI plugin has
most of the ICQ functions implemented.

This starts the QT plugin by default, so to run other plugins, you will have to
issue the command "licq -p <plugin>" once. To get back the Qt plugin, you will
have to run once "licq -p qt-gui". Alternatively you may be able to do it in a
plugin dialog box if your plugin supports this feature.

This version of licq has SSL support for those plugins that support it.
%description
Licq supports different interfaces and functions via plugins. Currently there are
plugins for both the X Windowing System and the console.

This package contains the base files for Licq (the Licq daemon) and the QT
plugin, which is written using the Qt widget set. Currently this GUI plugin has
most of the ICQ functions implemented.

This starts the QT plugin by default, so to run other plugins, you will have to
issue the command "licq -p <plugin>" once. To get back the Qt plugin, you will
have to run once "licq -p qt-gui". Alternatively you may be able to do it in a
plugin dialog box if your plugin supports this feature.

This version of licq has SSL support for those plugins that support it.


### PREP ##########################################
%prep
%ifdef autoreconf
%undefine autoreconf
%define autoreconf aclocal --force; autoconf; automake
%endif

%setup -q -n %name

pushd plugins
%if %with_gtk
    tar xfj %SOURCE5
    mv icqnd-* icqnd
%endif
popd

install -m 644 %SOURCE9 share/utilities/tracepath.utility

%patch2 -p1

%if %with_osd
pushd plugins/osd*
%patch17 -p1
popd
%endif

# with_qt4 || with_kde4
pushd plugins/qt4-gui*
%patch3 -p0
%patch22 -p1
popd

%if %with_aosd
%else
    rm -rf plugins/aosd
%endif
%if %with_console
%else
    rm -rf plugins/console
%endif

cd plugins/qt4-gui*

%if %with_qt4
cd ../qt4-gui*
sed -i "s|\s*Name\s*=.*|Name=Licq [Qt4]|" share/misc/licq.desktop
sed -i "s|\s*Exec\s*=.*|Exec=licq -p qt4-gui|" share/misc/licq.desktop
sed -i 's|/applications)|/applications RENAME licq-qt4.desktop)|' share/misc/CMakeLists.txt
#sed -i 's|set(USE_KDE.*|set(USE_KDE FALSE)|' CMakeLists.txt
#sed -i 's|option(WITH_KDE.*|set(WITH_KDE FALSE)|' CMakeLists.txt
find -type f -name CMakeLists.txt | \
while read f; do sed -i 's|WITH_KDE|QT_WITH_KDE|' $f; done
%endif

%if %with_kde4
cd ..; cp -r qt4-gui* kde4-gui
cd kde4-gui; rm -rf qt4-gui*
sed -i "s|\s*Name\s*=.*|Name=Licq [KDE4]|" share/misc/licq.desktop
sed -i "s|\s*Exec\s*=.*|Exec=licq -p kde4-gui|" share/misc/licq.desktop
sed -i 's|Qt4-GUI|KDE4-GUI|' CMakeLists.txt
sed -i 's|add_subdirectory(doc)||' CMakeLists.txt
#sed -i 's|set(USE_KDE.*|set(USE_KDE TRUE)|' CMakeLists.txt
#sed -i 's|option(WITH_KDE.*|set(WITH_KDE TRUE)|' CMakeLists.txt
find -type f -name CMakeLists.txt | \
while read f; do sed -i 's|QT_WITH_KDE|WITH_KDE|' $f; done
%endif

cd ../..

### BUILD ##########################################
%build
#add_optflags -D_FILE_OFFSET_BITS=64
#export CFLAGS="%optflags" CXXFLAGS="%optflags" CPPFLAGS="%optflags"

%K4cmake \
    -DINCLUDE_INSTALL_DIR=%_includedir \
    -DWITH_KDE:BOOL=ON \
    -DQT_WITH_KDE:BOOL=OFF \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_PLUGINS:BOOL=ON
%K4make

### INSTALL ##########################################
%install
%K4install

rm -rf %buildroot/%_datadir/licq/translations

#mkdir -p %buildroot/%_bindir
ln -fs licq %buildroot/%_bindir/licq-ssl
install -m755 %SOURCE10 %buildroot/%_bindir/licq-viewurl.sh

mkdir -p %buildroot/%_miconsdir
mkdir -p %buildroot/%_niconsdir
mkdir -p %buildroot/%_liconsdir
bzip2 -dc %SOURCE21 > %buildroot/%_miconsdir/licq.xpm
bzip2 -dc %SOURCE22 > %buildroot/%_niconsdir/licq.xpm
bzip2 -dc %SOURCE23 > %buildroot/%_liconsdir/licq.xpm

# menu stuff GTK
%if %with_gtk
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name-gtk <<EOF
    ?package(licq-gtk):\
    command="licq -p gtk-gui"\
    icon="licq.xpm"\
    title="Licq [GTK]"\
    longtitle="ICQ client"\
    needs="x11"\
    section="Networking/Instant messaging"
EOF
%endif

# menu stuff console
%if %with_console
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name-console <<EOF
    ?package(licq-console):\
    command="licq -p console"\
    icon="licq.xpm"\
    title="Licq [console]"\
    longtitle="Text based ICQ client"\
    needs="text"\
    section="Networking/Instant messaging"
EOF
%endif


%if %with_gtk
pushd plugins/icqnd
%make install DESTDIR=%buildroot libdir=%_libdir/%name
ln -s licq_icqnd.so %buildroot/%_libdir/licq/licq_gtk-gui.so
popd
%endif

# remove rpath from plugins
#find %buildroot -type f -name \*.so | while read f; do chrpath -d $f; done

%find_lang %name
%find_lang licq_osd_plugin


### FILES ##########################################
#
%files
%files maxi
%files mini

%if %with_kde4
## kde4 plugin
%files kde4
%_libdir/licq/licq*kde4-gui*
%_desktopdir/kde4/licq.desktop
%endif

%if %with_qt4
## licq qt4 plugin
%files qt4
%_libdir/licq/licq*qt4-gui*
%_datadir/licq/qt4-gui/
%_desktopdir/licq-qt4.desktop
%endif

## licq base
%files common -f %name.lang
%_bindir/licq
%_bindir/licq-ssl
%dir %_libdir/licq/
%dir %_datadir/licq/
%_datadir/licq/utilities/
%_datadir/licq/sounds/
%_miconsdir/licq.xpm
%_niconsdir/licq.xpm
%_liconsdir/licq.xpm
%attr(0755,root,root) %_bindir/licq-viewurl.sh
%doc doc/ upgrade/ README*
%if !%no_some_docs
%doc ChangeLog
%endif
%if %with_gpg
%doc licq_gpg.conf
%endif

%if %with_gtk
## gtk plugin
%files gtk
%_menudir/licq-gtk
%_libdir/licq/licq*icqnd*
%_libdir/licq/licq*gtk-gui*
%_datadir/licq/icqnd
%endif

%if %with_osd
## osd plugin
%files osd -f licq_osd_plugin.lang
%_libdir/licq/licq_osd.*
%doc plugins/osd*/%{name}_osd.conf
%doc plugins/osd*/{AUTHORS,TODO,README}
%endif

%if %with_osd
## aosd plugin
%files aosd
%_libdir/licq/licq_aosd.*
#%doc plugins/aosd*/%{name}_osd.conf
%doc plugins/aosd*/README
%endif

%if %with_msn
## msn plugin
%files msn
%_libdir/licq/protocol_msn.*
%doc plugins/msn*/owner.MSN_
%doc plugins/msn*/README
%endif

%if %with_jabber
## jabber plugin
%files jabber
%_libdir/licq/protocol_jabber.*
%doc plugins/jabber*/README
%endif

## devel
%files devel
%_includedir/licq
%_datadir/licq/cmake

%if %with_console
## console plugin
%files console
%_menudir/licq-console
%_libdir/licq/licq_console.*
%doc plugins/console*/README
%doc plugins/console*/%{name}_console.conf
%endif


%if %with_email
## email plugin
%files email
%_libdir/licq/licq_forwarder.*
%doc plugins/forwarder*/README
%doc plugins/forwarder*/%{name}_forwarder.conf
%endif

%if %with_auto_reply
## auto reply plugin
%files autoreply
%_libdir/licq/licq_autoreply.*
%doc plugins/auto-reply*/README
%doc plugins/auto-reply*/%{name}_autoreply.conf
%endif

%if %with_rms
## remote management svcx
%files rms
%_libdir/licq/licq_rms.*
%doc plugins/rms*/README
%doc plugins/rms*/%{name}_rms.conf
%endif

########################################################
%changelog
* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt3
- rebuild with new boost

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt2
- rebuilt with new boost

* Mon Nov 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt0.M60P.1
- built for M60P

* Tue Nov 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt1
- new version

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 1.5.1-alt3
- removed set_strip_method macro

* Thu Aug 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1.M60P.1
- built for M60P

* Fri Jul 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt2
- fix kde4 desktop-file

* Thu Jul 14 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt2
- fix build requires

* Mon Oct 04 2010 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.9-alt0.M51.1
- built for M51

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.9-alt1
- new version (ALT#23547)
- require qt4/kde4 ui by default

* Wed Jan 13 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.8-alt1.M51.1
- built for M51

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.8-alt2
- fix icon placement

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.8-alt1
- new version

* Tue Oct 20 2009 Sergey V Turchin <zerg@altlinux.org> 1.3.7-alt0.1
- 1.3.7-rc1

* Mon Jul 13 2009 Sergey V Turchin <zerg@altlinux.org> 1.3.6-alt4
- fix compile with new gpgme

* Mon Jun 29 2009 Sergey V Turchin <zerg@altlinux.org> 1.3.6-alt3
- fix compile with gcc-4.4

* Tue Jan 27 2009 Sergey V Turchin <zerg at altlinux dot org> 1.3.6-alt2
- add patch to fix logon
- remove deprecated macroses

* Thu Oct 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.3.6-alt1
- new version

* Wed Jul 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.3.5-alt4
- add unpackaged dirs

* Mon Jul 07 2008 Sergey V Turchin <zerg at altlinux dot org> 1.3.5-alt3
- add patch to fix login connection

* Wed Nov 07 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3.5-alt2
- fix requires

* Tue Oct 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3.5-alt1
- new version

* Fri Nov 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.4-alt2
- remove "-p qt-gui" from licq.desktop:Exec

* Mon Oct 30 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.4-alt1
- release 1.3.4

* Wed Sep 20 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.4-alt0.1.RC1
- 1.3.4-RC1
- update gtk plugin to icqnd-0.1.9.6

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt6
- use original Russian translation

* Tue Jul 18 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt5
- fix build on x86_64
- disable gtk plugin on x86_64 until not fixed

* Fri Jul 14 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt4
- rebuilt without console plugin (#9684)
- update gtk plugin to icqnd-0.1.9.5

* Fri Oct 28 2005 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt3
- fix russian translation

* Thu Oct 27 2005 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt2
- fix build requires
- update russian translation

* Tue Oct 25 2005 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt1
- new version

* Tue Oct 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1.3.0-alt3
- disable docking by default because crash

* Tue Oct 12 2004 Sergey V Turchin <zerg at altlinux dot org> 1.3.0-alt2
- add upgrade-1.3.0.sh to documentation of %name-common package
- force linking qt-gui and kde-gui with libpthread

* Tue Oct 12 2004 Sergey V Turchin <zerg at altlinux dot org> 1.3.0-alt1
- new version

* Mon Jul 12 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt7
- check /proc/PID/cmdline (#3924)
- osd plugin 1.2.7.5
- add translations of osd plugin into package
- fix dock size in gnome

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.7-alt6.1
- Rebuilt with openssl-0.9.7d.

* Sat Mar 20 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt6
- rebuild with new qt

* Thu Dec 11 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt5
- add patch to wrap qt malloc

* Fri Nov 14 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt4
- restructurisation
- improve charset changing icon visibility in kde-ui
- new version of osd plugin and default settings
- gpg support
- hiding userlist by click on warf in qt-gui
- add patch for default url viewver
- fix menu

* Mon Jun 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt3
- patch to encode alias in tabbed dialog by Alexey Morozov <alex at hop-go.com>
- add hack for default encoding CP1251 when *.KOI8* locale

* Thu Jun 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt2
- build without socks for Sisyphus

* Thu Jun 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt1.sox
- new version
- build with socks for Daedalus

* Tue Jun 24 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.7-alt0.1.20030624
- update from cvs
- new version of osd plugin

* Fri Apr 04 2003 Sergey V Turchin < zerg at altlinux dot ru > 1.2.6-alt3
- build with new osd (On Screen Dysplay) plugin

* Wed Apr 02 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.6-alt2
- build without socks for Sisyphus

* Wed Apr 02 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.6-alt1.sox
- new version
- build with socks for Daedalus

* Thu Jan 30 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.4-alt2
- build without socks

* Thu Jan 30 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.4-alt1.sox
- new version
- build with socks

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt2
- fix build with socks

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt1.sox
- build with socks for Daedalus

* Wed Jan 08 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Wed Dec 25 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021225
- update from cvs

* Thu Dec 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021219
- update from cvs

* Wed Nov 27 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021127
- update from cvs

* Mon Nov 18 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021118
- update from cvs

* Thu Nov 14 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021114
- update from cvs

* Tue Nov 12 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021112
- update from cvs

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.2.20021105
- update from cvs
- disable Patch8

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.1.20021104
- update from cvs

* Tue Oct 29 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt0.1.20021029
- new devel version
- update from cvs

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt0.4.20021015
- update from cvs

* Tue Oct 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt0.3.20021015
- update code from cvs
- move %name to %name-qt, %name-kde to %name

* Thu Sep 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt0.3.20020828
- build with gcc 3.2

* Wed Aug 28 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt0.2.20020828
- update code from cvs

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt0.2.20020819
- add patch8 for translation tables
  from Sergey A. Sukiyazov <corwin@micom.net.ru>

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt0.1.20020819
- update code from cvs

* Thu Aug 01 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.0-alt1.a
- new version

* Wed Jul 17 2002 ZerG <zerg@altlinux.ru> 1.1.0-alt0.15.cvs20020717
- update code from cvs

* Sun Jul 14 2002 ZerG <zerg@altlinux.ru> 1.1.0-alt0.15.cvs20020711
- update code from cvs

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.15.cvs20020611
- fix requires

* Tue Jun 11 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.14.cvs20020611
- update from cvs
- build without email plugin

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.12.cvs20020425
- build with KDE3/Qt3 but without KDE2/Qt2
- update from cvs

* Fri Apr 12 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.11.cvs20020411
- fix build GUI pluguins with right QT-KDE
- fix launch KDE3 plugin

* Thu Apr 11 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.10.cvs20020411
- update cvs
- build plugin for KDE3
- cleanup spec

* Thu Mar 28 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.9.cvs20020328
- cvs updated

* Thu Mar 21 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.8.cvs20020321
- cvs updated

* Wed Feb 21 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.7.cvs20020220
- cvs updated

* Thu Feb 12 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.6.cvs20020212
- cvs updated

* Fri Feb 01 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.5.cvs20020201
- cvs updated

* Wed Jan 16 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.4.cvs20020112
- cvs updated

* Thu Jan 03 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.0-alt0.3.cvs20020103
- cvs updated
- cleanup spec

* Fri Dec 21 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.4-alt2
- cvs updated
- drop Source1, Source7

* Fri Dec 07 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.4-alt1
- add Source7 to compile 1.0.4 with qt2

* Thu Dec 06 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.4-alt0.4
- 1.0.4
- cleanup && fix && improve spec
- cvs tag V8_BRANCH added to Source1
- remove jons-gtk-gui plugin

* Tue Oct 30 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.4-alt0.3
- fix Requires

* Mon Oct 29 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.4-alt0.2
- move base binaries and data to external package %name-base
- cleanup spec
- remove update-hosts plugin

* Mon Oct 22 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.4-alt0.1
- cvs snapshoot
- build jons-gtk-gui plugin
- change version because 1.0.4 is near

* Tue Oct 02 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.3-ipl7mdk
- cvs snapshoot
- cleanup spec
- add patch6 from Alexey Morozov <aam@altlinux.ru>

* Thu May 17 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.3-ipl6mdk
- fix wrong build

* Mon May 14 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.3-ipl5mdk
- fix build version

* Fri May 11 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.3-alt1
- rebuild with KDE and QT plugins

* Fri Mar 16 2001 AEN <aen@logic.ru> 1.0.3-ipl3mdk
- rebuild w/o KDE :-(

* Fri Mar 16 2001 AEN <aen@logic.ru> 1.0.3-ipl2mdk
- rebuild in release environment

* Sat Mar 10 2001 AEN <aen@logic.ru> 1.0.3-ipl1mdk
- 1.0.3

* Fri Jan 05 2001 AEN <aen@logic.ru>
- default translation directory fixed

* Wed Dec 20 2000 AEN <aen@logic.ru>
- 1.0.2
- small spec changes

* Sun Dec 17 2000 AEN <aen@logic.ru>
- 1.0.1

* Sat Dec 09 2000 AEN <aen@logic.ru>
- build for RE
- translations added
* Wed Nov 15 2000 Geoffrey Lee <snailtlak@mandrakesoft.com> 1.0-4mdk
- patched source to generate to use soundwrapper by default.

* Sun Nov 05 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-3mdk
- recompile with new gcc.

* Sun Oct 22 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-2mdk
- add a missing iostream include.

* Fri Oct 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-1mdk
- a very nice and new shiny version.

* Sun Oct 08 2000 Geoffrey Lee <snailtalk@mandrakeoft.com> 0.85-23mdk
- fix the segv problems (Jason, Alex.)
- remove qt-devel (Why was it ever there ??)

* Wed Sep 20 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-22mdk
- remove the wrapper script. It is a bad idea, really ... Qt has pretty
  crappy support for i18n anyway.
- replace the wrapper script with a symbolic link.

* Tue Sep 19 2000 David BAUDENS <baudens@mandrakesoft.com> 0.85-21mdk
- Fix section in Menu entry$
- Fux Summary

* Sat Sep 09 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-20mdk
- rebuild against the latest Qt library.
- a fix for the shell script wrapper.

* Tue Sep 05 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-19mdk
- for each (@group) s/ICQ/Instant messaging/;

* Sun Sep 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-18mdk
- really obsolete licq-ssl ..

* Sun Sep 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-17mdk
- requires licq, not licq-base. OK this really should be the last problem..:-(

* Sun Sep 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-16mdk
- obsolete licq-ssl as well. This should be the last of licq problems ..

* Sun Sep 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-15mdk
- obsoletes the licq-base package, as it is no longer needed (vdanen.)
- add a script for i18n (me).

* Thu Aug 31 2000 Geoffrey Lee <snailtalk@mandakesoft.com> 0.85-14mdk
- merge the licq-ssl and licq-base package to licq.

* Sun Aug 20 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-13mdk
- apply patch from Jan Niehusmann <jan@gondor.com> to fix an annoying bug.

* Thu Aug 17 2000 Geoffrey Lee <snailtalk@mandrakesoft.com>  0.85-12mdk
- rebuild to fix a typo.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.85-11mdk
- automatically added BuildRequires

* Sat Jul 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-10mdk
- fix silly typo in the licq-ssl package (andre)

* Thu Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-9mdk
- add post and postun for ssl package

* Thu Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-8mdk
- re-enable the ssl binary support since we can include it now

* Mon Jul 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-7mdk
- fix some wrong requires
- fix the duplicate menu entries
- remove the ssl binary (maybe one should go to crypto ...)

* Fri Jul 22 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.85-6mdk
- problem with licq-ssl menu entry: command is licq-ssl not licq or else you
  don't get the secure licq to licq implementation!!
- update menus and clean the menus for the licq-ssl pcakage
- fix the requires
- fix some awfully wrong permissions ...

* Wed Jul 19 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.85-5mdk
- re-del the individual versionning. either we use individual release
  tags or we do nothing, in order to not make the upgrades impossible.
- BM

* Tue Jul 18 2000 Geoffrey lee <snailtalk@linux-mandrake.com> 0.85-4mdk
- re-add the individual versioning: it is not silly, because every plugin
  has its own version, it is best not to re-define the version ourselves
- add official rms plugin
- gtk+licq has been moved to separate spec file
- add devel package

* Mon Jul 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.85-3mdk
- fix silly hardcoding of i586-mandrake-linux instead of %% {_target_platform}

* Mon Jul 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.85-2mdk
- disable silly separate versionning of each plugin

* Mon Jul 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.85-1mdk
- 0.85
- gtk plugin does not compile anymore (API change)
- patch4: fix update-host plugin
- patch5: fix ltconfig problem for main

* Wed May 19 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.81-11mdk
- _tmppath
- better perl fix for gtk+licq install hack
- buildrequires qt2-devel >= 2.1, and not just in requires:
- use QTDIR
- remove some patches
- new mailchecker plugin (not compiled yet, doesn't work with release)
- add password patch for qt-gui and gtk+ gui, please test !!
- oops, require ncurses for console plugin
- removed duplicate summary
- remove -c from %%setup (ugly hack by me) and use mv

* Wed May 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.81-10mdk
- libtoolizification fix (aka shoot'party of configure).

* Wed Apr 26 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.81-9mdk
- licq-update-hosts-0.0.5-8mdk.i586.rpm has been lost in space

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.81-8mdk
- added dependency to qt2 >= 2.1

* Wed Apr 19 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.81-7mdk
- fixed missing icon in filelist
- added 32x32 icon
- cleanup of specfile, install section mostly [still a lot to do]
- path of qt2 with the help of Christopher Molnar

* Sun Apr 16 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.81-6mdk
- changed path of qt2 includes

* Sat Apr 15 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.81-5mdk
- Added menu icon

* Fri Apr 14 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.81-4mdk
- updated to use qt-2.1

* Fri Apr 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.81-3mdk
- fix menu entry
- merge menu file with spec

* Thu Apr 06 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.81-2mdk
- installation hacks for gtk+licq  :-/
- add URL for gtk+licq @ http://gtk.licq.org
- update hosts 0.0.5
- greatly improve description
- use prefix: _prefix and then prefix in files section
- fixed files section
- apologize for the stupid changelog mistakes that i made last time

* Fri Mar 31 2000 Lenny Cartier <lenny@mandrakesoft.com>
- add menu entry
- used srpm from Geoffrey Lee <snailtalk@linux-mandrake.com>

* Thu Mar 29 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- licq 0.81
- qt+licq 0.38.1
- compile qt-gui --with-spoofing ;-) ;-)

* Thu Mar 23 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- licq 0.80
- add gtk+licq 0.38
- include more docs
- hacked the spec file a lot
- add update-hosts 0.0.4 (hacked slightly to get it to work)
- use autoconf for qt plugin + update-hosts because original configure script
  was f*cked

* Tue Mar 23 2000 Lenny Cartier <lenny@mandrakesoft.com>
- clean spec
- fix group
- fix files section

* Sun Feb 06 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- Fix docs
- Strip binaries

* Thu Jan 27 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- Updated to 0.75.3a
- Fixed upgrade scripts.

* Sun Dec 19 1999 John Buswell <johnb@mandrakesoft.com>
- Added docs

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.70.1.
- {Build,}Requires: qt2{-,devel}.
- Correct download locations.
- Improve Summary.
- Fix build with qt2.

* Sun Sep 19 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 0.70 final

* Thu Aug 12 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- initial RPM


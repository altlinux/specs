%define mysql_ver %{get_version libmysqlclient-devel}
%if "%mysql_ver" == "%nil"
%define mysql_ver %{get_version libMySQL-devel}
%endif
%if "%mysql_ver" == "%nil"
%define mysql_ver 5.0
%endif

%define rname amarok
Name: kde4-%rname
Version: 2.5.0
Release: alt2
#define beta 20090812

Summary: Amarok is a music player for KDE.
License: GPLv2
Group: Sound
Url: http://amarok.kde.org/

Requires: qtscriptbindings libqt4-sql-sqlite
Requires: kde4multimedia-audiocd
Conflicts: amarok <= 1.4.10-alt10

Source0: ftp://ftp.kde.org/pub/kde/stable/amarok/%version/src/%rname-%version%{?beta:.%beta}.tar
Source1: mysql.tar
Patch1: amarok-2.3.2-alt-mysql.patch
# RH
Patch50: amarok-2.4.3-qtscript_not_required.patch


# Automatically added by buildreq on Thu Nov 19 2009 (-bi)
#BuildRequires: dbus-tools-gui doxygen gcc-c++ git-core glibc-devel-static groff-ps kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libcurl-devel libgcrypt-devel libgio-devel libgpod-devel libgtk+2-common-devel liblastfm-devel libloudmouth-devel libmtp-devel libncursesw-devel libqca2-devel libqt3-devel libtag-devel libtag-extras-devel libxkbfile-devel libxml2-devel qtscriptbindings rpm-build-ruby tetex-latex time xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4libs-devel kde4base-runtime-devel libMySQL-devel
BuildRequires: dbus-tools-gui doxygen gcc-c++ glibc-devel groff-ps
BuildRequires: libtag-devel >= 1.6 libtag-extras-devel >= 1.0
BuildRequires: libcurl-devel libgcrypt-devel libgio-devel libgpod-devel libgtk+2-common-devel liblastfm-devel
BuildRequires: libloudmouth-devel libmtp-devel libncursesw-devel libqca2-devel libxml2-devel
BuildRequires: qtscriptbindings rpm-build-ruby tetex-latex libofa-devel libgdk-pixbuf-devel glib2-devel
BuildRequires: libtunepimp-devel libusb-devel libvisual0.4-devel libSDL-devel
BuildRequires: qjson-devel libavformat-devel libavcodec-devel libmygpo-qt-devel
BuildRequires: /proc


%description
amaroK is an advanced audio player.
Excellent streaming support, audio effects, visualisations and smooth 
crossfading separate this player from existing KDE solutions. 
At the same time amaroK provides a very intuitive and quick user interface, 
with unparalleled playlist handling, optimized for very large playlists.
The built-in StreamBrowser makes finding web streams as easy as using a radio: 
you can pick your favorite program right inside of amaroK.
%description -l ru_RU.UTF-8
amaroK - передовой аудио плеер. Превосходная поддержка потокового воспроизведения, 
звуковые эффекты, визуализации. В то же самое время amaroK обеспечивает очень интуитивный
и быстрый пользовательский интерфейс. Плейлист оптимизирован для очень больших плейлистов.
Встроенный StreamBrowser делает обнаружение потоков в сети столь же легкими как и использование
радио: Вы можете выбрать и настроить их прямо в amaroK.

%package engine-phonon
Summary: Phonon engine for amaroK player
Group: Sound
Requires: %name = %version-%release
Provides: %name-engine
%description engine-phonon
amarok-engine-phonon is an engine for amaroK player.
It uses Phonon for output sound stream.

%package mediadevice-ipod
Summary: iPod plugin for amaroK player
Group: Sound
Requires: %name = %version-%release
%description mediadevice-ipod
amarok-mediadevice-ipod is a plugin for Apple iPod
player

%package mediadevice-generic
Summary: VFAT plugin for amaroK player
Group: Sound
Requires: %name = %version-%release
Provides: %name-mediadevice-vfat
%description mediadevice-generic
amarok-mediadevice-generic is a generic plugin for
various devices that uses VFAT filesystem

%package mediadevice-daap
Summary: DAAP (Digital Audio Access Protocol) plugin for amaroK player
Group: Sound
Requires: %name = %version-%release
%description mediadevice-daap
amarok-mediadevice-daap is a plugin for interoperability
with various devices that uses Digital Audio Access
Protocol (DAAP)

%package mediadevice-mtp
Summary: MTP (Media Transfer Protocol) plugin for amaroK player
Group: Sound
Requires: %name = %version-%release
%description mediadevice-mtp
amarok-mediadevice-daap is a plugin for interoperability
with various devices that uses Media Transfer Protocol (MTP)

%prep
%setup -q -n %rname-%version%{?beta:.%beta} -a 1
%patch1 -p1
%patch50 -p1
pushd mysql
%autoreconf
popd

%build
%if 1
if ! [ -f %_builddir/%rname-%version%{?beta:.%beta}/mysql-installed/exclude/lib/mysql/libmysqld.a \
    -a -f %_builddir/%rname-%version%{?beta:.%beta}/mysql-installed/exclude/lib/mysql/libmysqlclient.a ]
then
pushd mysql
CFLAGS="%optflags %optflags_shared" CXXFLAGS="%optflags %optflags_shared" LDFLAGS="-L%_libdir" \
%configure \
    --prefix=/exclude \
    --bindir=/exclude/bin \
    --libdir=/exclude/lib \
    --datadir=%_K4apps/amarok \
    --without-server \
    --with-embedded-server \
    --without-docs \
    --without-man \
    --without-bench \
    --without-ssl \
    --without-extra-tools \
    --without-libwrap \
    --disable-shared \
    --enable-static \
    --with-plugins=none \
    --with-plugin-myisam
#    --with-charset=utf8 \
#    --with-collation=utf8_general_ci \

%make_build
%make install DESTDIR=%_builddir/%rname-%version%{?beta:.%beta}/mysql-installed
popd
fi
%endif
%K4cmake \
    -DLIBVISUAL_FOUND:BOOL=TRUE \
    -DMYSQL_FOUND:BOOL=TRUE \
    -DMYSQL_EMBEDDED_FOUND:BOOL=TRUE \
    -DMYSQL_INCLUDE_DIR:PATH=%_builddir/%rname-%version%{?beta:.%beta}/mysql-installed/%_includedir/mysql \
    -DMYSQL_EMBEDDED_LIBRARIES:FILEPATH=%_builddir/%rname-%version%{?beta:.%beta}/mysql-installed/exclude/lib/mysql/libmysqld.a \
    -DMYSQL_LIBRARIES:FILEPATH=%_builddir/%rname-%version%{?beta:.%beta}/mysql-installed/exclude/lib/mysql/libmysqlclient.a
%K4make

%install
pushd mysql
%make install DESTDIR=%buildroot
popd
%K4install
if [ -d %buildroot/%_K4datadir/bin ]; then
    mkdir -p %buildroot/%_kde4_bindir/
    pushd %buildroot/%_K4datadir/bin/
    ls -1 | \
    while read b; do
	mv $b %buildroot/%_kde4_bindir/
    done
    popd
fi
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang amarokcollectionscanner_qt
%K4find_lang --with-kde --append --output=%rname.lang amarok_scriptengine_qscript
%K4find_lang --with-kde --append --output=%rname.lang amarokpkg



%files -f %rname.lang
%exclude /exclude
%exclude %_includedir/mysql
%exclude %_K4apps/%rname/mysql/mysql*.server
%doc AUTHORS ChangeLog README
%ifdef _kde_alternate_placement
%_kde4_bindir/amarok
%_kde4_bindir/amarok_afttagger
%_kde4_bindir/amarokcollectionscanner
%_kde4_bindir/amarokmp3tunesharmonydaemon
%_kde4_bindir/amarokpkg
%_kde4_xdg_apps/amarok.desktop
%_kde4_xdg_apps/amarok_containers.desktop
%_kde4_iconsdir/hicolor/*/apps/amarok.*
%else
%_K4bindir/amarok
%_K4bindir/amarok_afttagger
%_K4bindir/amarokcollectionscanner
%_K4bindir/amarokmp3tunesharmonydaemon
%_K4bindir/amarokpkg
%_K4xdg_apps/amarok.desktop
%_K4xdg_apps/amarok_containers.desktop
%_K4iconsdir/hicolor/*/apps/amarok.*
%endif
%_K4apps/%rname/
%_K4conf_update/amarok*
%_K4libdir/libamarokcore.so.*
%_K4libdir/libamaroklib.so.*
%_K4libdir/libamarokpud.so.*
%_K4libdir/libamarokocsclient.so.*
%_K4libdir/libamarok-sqlcollection.so.*
%_K4libdir/libamarok-transcoding.so.*
#%_K4libdir/libamarokqtjson.so.*
%_K4libdir/libampache_account_login.so
#%_K4libdir/strigi/*.so
#
%_K4lib/amarok_collection-*.so
%_K4lib/amarok_containment_vertical.so
%_K4lib/amarok_context_applet_*.so
%_K4lib/amarok_data_engine_*.so
%_K4lib/amarok_service_*.so
%_K4lib/kcm_amarok_service_*.so
%_K4lib/amarok_appletscript_simple_javascript.so
%_K4lib/amarok_runnerscript_javascript.so
#
%_K4apps/desktoptheme/default/widgets/amarok-*.svg
%_K4apps/desktoptheme/Amarok-Mockup/
%_K4apps/solid/actions/amarok-play-audiocd.desktop
#
%_K4srv/ServiceMenus/amarok_append.desktop
%_K4srv/amarok.protocol
%_K4srv/amarokitpc.protocol
%_K4srv/amarok_collection-*.desktop
%_K4srv/amarok-containment-vertical.desktop
%_K4srv/amarok-context-applet-*.desktop
%_K4srv/amarok-data-engine-*.desktop
%_K4srv/amarok_service_*.desktop
%_K4srv/amarok-scriptengine-applet-simple-javascript.desktop
%_K4srv/amarok-scriptengine-runner-javascript.desktop
%_K4srv/amaroklastfm.protocol
%_K4srvtyp/amarok_codecinstall.desktop
%_K4srvtyp/amarok_context_applet.desktop
%_K4srvtyp/amarok_data_engine.desktop
%_K4srvtyp/amarok_plugin.desktop
#
%_K4dbus_interfaces/org.freedesktop.MediaPlayer.*.xml
%_K4dbus_interfaces/org.kde.amarok.*.xml
#
%_K4cfg/amarok*
%_K4conf/amarok*
#
%_K4lib/amarok_collection-mysqlecollection.so
%_K4srv/amarok_collection-mysqlecollection.desktop
#
%_K4lib/amarok_collection-mysqlservercollection.so
%_K4srv/amarok_collection-mysqlservercollection.desktop
#
%_K4lib/amarok_collection-audiocdcollection.so
%_K4srv/amarok_collection-audiocdcollection.desktop
#
%_K4lib/amarok_collection-umscollection.so
%_K4srv/amarok_collection-umscollection.desktop
#
%_K4lib/amarok_collection-daapcollection.so
%_K4srv/amarok_collection-daapcollection.desktop
#
%_K4lib/amarok_collection-ipodcollection.so
%_K4srv/amarok_collection-ipodcollection.desktop
#
%_K4lib/amarok_collection-mtpcollection.so
%_K4srv/amarok_collection-mtpcollection.desktop
#
%_K4lib/amarok_device_massstorage.so
%_K4srv/amarok_device_massstorage.desktop
%_K4lib/amarok_device_nfs.so
%_K4srv/amarok_device_nfs.desktop
%_K4lib/amarok_device_smb.so
%_K4srv/amarok_device_smb.desktop


%changelog
* Mon Feb 06 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt2
- fix build requires

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt0.M60P.1
- built for M60P

* Wed Dec 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1
- new version

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.3-alt0.M60P.1
- built for M60P

* Tue Aug 02 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.3-alt1
- new version

* Wed May 11 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.1-alt2
- fix build requires

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.1-alt1
- new version

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt4
- fix build requires

* Mon Mar 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt3
- move to standart place

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt2
- update mysql to 5.1.55

* Mon Jan 17 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt1
- new version

* Wed Sep 22 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt0.M51.1
- built for M51

* Tue Sep 21 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt1
- new version
- update mysql to 5.1.50

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt3
- rebuilt with new liblastfm

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt1.M51.1
- built for M51

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt2
- update mysql to 5.1.47

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.M51.2
- rebuilt with new KDE

* Wed Mar 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.M51.1
- built for M51

* Tue Mar 16 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- new version

* Wed Jan 13 2010 Sergey V Turchin <zerg@altlinux.org> 2.2.2-alt0.M51.1
- built for M51

* Wed Jan 13 2010 Sergey V Turchin <zerg@altlinux.org> 2.2.2-alt1
- new version

* Fri Nov 20 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt2.M51.1
- built for M51

* Thu Nov 19 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt3
- fix build requires

* Thu Nov 19 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt2
- fix build requires

* Thu Nov 19 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt1
- 2.2.1 release

* Thu Oct 01 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- 2.2 release
- update mysql to 5.1.39

* Fri Sep 25 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.90-alt1
- 2.2 RC1

* Thu Sep 17 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.85-alt1
- 2.2 beta2

* Tue Sep 08 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.80-alt1
- 2.2 beta1

* Tue Aug 18 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt2
- built with mysql embedded and taglib-extras

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt0.M50.1
- built for M50

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- 2.1.1 release

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 2.1-alt2
- add requires to Qt sqlite driver

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 2.1-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- 2.1 release

* Fri May 15 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.96-alt1
- 2.1 beta2

* Wed Apr 15 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.90-alt1
- 2.1 beta1

* Fri Mar 20 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0.60-alt0.0.941520
- svn 941520

* Fri Mar 06 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt1
- new version

* Mon Jan 12 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0.1.1-alt1
- new version

* Thu Dec 18 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt1
- release 2.0

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 1.80-alt0.0.1
- 1.80 test

%define qversion 0.3.1.0
%define qrelease alt1
%define jversion 1.1.0
%define jrelease alt1

Name: qutim
Epoch: 5
Version: %qversion
Release: %qrelease

Summary: qutIM Instant Messenger
Summary(ru_RU.UTF-8): Клиент сервисов мгновенных сообщений qutIM
License: GPLv3
Group: Networking/Instant messaging

URL: http://www.qutim.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://qutim.org/dwnl/34/%name-0.3.1.tar.bz2
Patch0: %name-%qversion-alt-fix-linking.patch
Patch1: %name-%qversion-alt-tmp-telepathy.patch

Requires: lib%name = %qversion-%qrelease
Requires: libqt4-svg

BuildPreReq: aspell
BuildPreReq: kde-common-devel
BuildPreReq: libqt4-devel >= 4.7.1

BuildRequires: attica-devel
BuildRequires: cmake >= 2.8.1
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: glibc-devel-static
BuildRequires: kde4libs-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libXft-devel
BuildRequires: libaspell-devel
BuildRequires: libhunspell-devel
BuildRequires: liblzma-devel
BuildRequires: libotr-devel
BuildRequires: libpurple-devel >= 2.6.0
BuildRequires: libqca2-devel
BuildRequires: libqt4-sql-mysql
BuildRequires: libtelepathy-qt4-devel >= 0.3.0
BuildRequires: phonon-devel

%description
qutIM - free open-source multiprotocol (ICQ, Jabber, Mail.Ru, IRC, VKontakte) instant messenger for Windows, Linux, MacOS X, OS/2, Symbian, Haiku, Solaris, Maemo/MeeGo and *BSD systems

%description -l ru_RU.UTF-8
qutIM — это свободный многопротокольный (ICQ, Jabber, Mail.Ru, IRC, VKontakte) клиент обмена мгновенными сообщениями для Windows, Linux, MacOS X, OS/2, Symbian, Haiku, Solaris, Maemo/MeeGo и *BSD

# qutIM library
%package -n lib%name
Summary: Shared library for qutIM
Group: System/Libraries

%description -n lib%name
Shared library for qutIM

# qutIM library development files
%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %qversion-%qrelease

%description -n lib%name-devel
Development files for %name

# Astral protocol
%package -n %name-protocol-astral
Summary: Astral protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-protocol-astral
Astral protocol support for qutIM

# IRC protocol
%package -n %name-protocol-irc
Summary: IRC protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-protocol-irc
IRC protocol support for qutIM

# Jabber protocol
%package -n %name-protocol-jabber
Summary: Jabber protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
Requires: libjreen >= %jversion-%jrelease

%description -n %name-protocol-jabber
Jabber protocol for qutIM

# Jreen library (for jabber protocol)
%package -n libjreen
Summary: Jreen is extensible Qt-based asynchronious Jabber library
Group: System/Libraries
Version: %jversion
Release: %jrelease

%description -n libjreen
Jreen is extensible Qt-based asynchronious Jabber library

# Jreen development files
%package -n libjreen-devel
Summary: Jreen is extensible Qt-based asynchronious Jabber library
Group: Development/C++
Version: %jversion
Release: %jrelease
Requires: libjreen = %jversion-%jrelease

%description -n libjreen-devel
Jreen is extensible Qt-based asynchronious Jabber library

# Mail.Ru protocol
%package -n %name-protocol-mrim
Summary: Mail.Ru protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-protocol-mrim
Mail.Ru protocol support for qutIM

# OSCAR protocol
%package -n %name-protocol-oscar
Summary: OSCAR protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
Requires: qca2-ossl

%description -n %name-protocol-oscar
OSCAR protocol support for qutIM

# Quetzal protocol
%package -n %name-protocol-quetzal
Summary: Quetzal protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-protocol-quetzal
Quetzal protocol support for qutIM

# VKontakte.Ru protocol
%package -n %name-protocol-vkontakte
Summary: VKontakte.Ru protocol for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-protocol-vkontakte
VKontakte.Ru protocol support for qutIM

# Adium webview plugin
%package -n %name-plugin-adiumwebview
Summary: Adium webview plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
Requires: lib%name-adiumwebview = %qversion-%qrelease

%description -n %name-plugin-adiumwebview
Aescrypto plugin support for qutIM

# qutIM Adium webview library
%package -n lib%name-adiumwebview
Summary: qutIM Adium webview shared library
Group: System/Libraries

%description -n lib%name-adiumwebview
qutIM Adium webview shared library

# qutIM Adium webview development files
%package -n lib%name-adiumwebview-devel
Summary: Development files for qutIM Adium webview
Group: Development/C++
Requires: lib%name-adiumwebview = %qversion-%qrelease

%description -n lib%name-adiumwebview-devel
Development files for qutIM Adium webview

# Aescrypto plugin
%package -n %name-plugin-aescrypto
Summary: Aescrypto plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-aescrypto
Aescrypto plugin support for qutIM

# Antiboss plugin
%package -n %name-plugin-antiboss
Summary: Antiboss plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-antiboss
Antiboss plugin support for qutIM

# Antispam plugin
%package -n %name-plugin-antispam
Summary: Antispam plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-antispam
Antispam plugin support for qutIM

# Aspeller plugin
%package -n %name-plugin-aspeller
Summary: Aspeller plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-aspeller
Aspeller plugin support for qutIM

# Bearer manager plugin
%package -n %name-plugin-bearermanager
Summary: Bearer manager plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-bearermanager
Bearer manager plugin support for qutIM

# Birthday reminder plugin
%package -n %name-plugin-birthdayreminder
Summary: Birthday reminder plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-birthdayreminder
Birthday reminder plugin support for qutIM

# Blog improver plugin
%package -n %name-plugin-blogimprover
Summary: Blog improver plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-blogimprover
Blog improver plugin support for qutIM

# ClConf plugin
%package -n %name-plugin-clconf
Summary: ClConf plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-clconf
ClConf plugin support for qutIM

# DBus API plugin
%package -n %name-plugin-dbusapi
Summary: DBus API plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-dbusapi
DBus API plugin support for qutIM

# DBus Notifications plugin
%package -n %name-plugin-dbusnotifications
Summary: DBus Notifications plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-dbusnotifications
DBus Notifications plugin support for qutIM

# Emoedit plugin
%package -n %name-plugin-emoedit
Summary: Emoedit plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-emoedit
Emoedit plugin support for qutIM

# Floaties plugin
%package -n %name-plugin-floaties
Summary: Floaties plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-floaties
Floaties plugin support for qutIM

# Highlighter plugin
%package -n %name-plugin-highlighter
Summary: Highlighter plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-highlighter
Highlighter plugin support for qutIM

# Histman plugin
%package -n %name-plugin-histman
Summary: Histman plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-histman
Histman plugin support for qutIM

# Hunspeller plugin
%package -n %name-plugin-hunspeller
Summary: Hunspeller plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-hunspeller
Hunspeller plugin support for qutIM

# KDE Integration plugin
%package -n %name-plugin-kdeintegration
Summary: KDE Integration plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-kdeintegration
KDE Integration plugin support for qutIM

# Kinetic Popups plugin
%package -n %name-plugin-kineticpopups
Summary: Kinetic Popups plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-kineticpopups
Kinetic Popups plugin support for qutIM

# Linux integration plugin
%package -n %name-plugin-linuxintegration
Summary: Linux integration plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-linuxintegration
Linux integration plugin support for qutIM

# Logger plugin
%package -n %name-plugin-logger
Summary: Logger plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-logger
Logger plugin support for qutIM

# Mass Messaging plugin
%package -n %name-plugin-massmessaging
Summary: Mass Messaging plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-massmessaging
Mass Messaging plugin support for qutIM

# Multimedia Backend plugin
%package -n %name-plugin-multimediabackend
Summary: Multimedia Backend plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-multimediabackend
Multimedia Backend plugin support for qutIM

# Now Playing plugin
%package -n %name-plugin-nowplaying
Summary: Now Playing plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-nowplaying
Now Playing plugin support for qutIM

# Off-the-Record plugin
%package -n %name-plugin-offtherecord
Summary: Off-the-Record plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-offtherecord
Off-the-Record plugin support for qutIM

# Old Delegate plugin
%package -n %name-plugin-olddelegate
Summary: Old Delegate plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-olddelegate
Old Delegate plugin support for qutIM

# Phonon Sound plugin
%package -n %name-plugin-phononsound
Summary: Phonon Sound plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-phononsound
Phonon Sound plugin support for qutIM

# Plugman plugin
%package -n %name-plugin-plugman
Summary: Plugman plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
Requires: libquasar = %qversion-%qrelease

%description -n %name-plugin-plugman
Plugman plugin support for qutIM

# Quasar library (for plugman plugin)
%package -n libquasar
Summary: Shared library (for %name plugman plugin)
Group: System/Libraries

%description -n libquasar
Shared library (for %name plugman plugin)

# Quasar development files
%package -n libquasar-devel
Summary: Development files for quasar
Group: Development/C++
Requires: libquasar = %qversion-%qrelease

%description -n libquasar-devel
Development files for quasar  (for %name plugman plugin)

# QML Chat plugin
%package -n %name-plugin-qmlchat
Summary: QML Chat plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-qmlchat
QML Chat plugin support for qutIM

# QRC Icons plugin
%package -n %name-plugin-qrcicons
Summary: QRC Icons plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-qrcicons
QRC Icons plugin support for qutIM

# Script API plugin
%package -n %name-plugin-scriptapi
Summary: Script API plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-scriptapi
Script API plugin support for qutIM

# SDL Sound plugin
%package -n %name-plugin-sdlsound
Summary: SDL Sound plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-sdlsound
SDL Sound plugin support for qutIM

# Unread Messages Keeper plugin
%package -n %name-plugin-unreadmessageskeeper
Summary: Unread Messages Keeper plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-unreadmessageskeeper
Unread Messages Keeper plugin support for qutIM

# Updater plugin
%package -n %name-plugin-updater
Summary: Updater plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-updater
Updater plugin support for qutIM

# URL Preview plugin
%package -n %name-plugin-urlpreview
Summary: URL Preview plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-urlpreview
URL Preview plugin support for qutIM

# Weather plugin
%package -n %name-plugin-weather
Summary: Weather plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-weather
Weather plugin support for qutIM

# Yandex.Narod.Ru plugin
%package -n %name-plugin-yandexnarod
Summary: Yandex.Narod.Ru plugin for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease

%description -n %name-plugin-yandexnarod
Yandex.Narod.Ru plugin support for qutIM

# Arabic language for qutIM
%package -n %name-lang-ar
Summary: Arabic language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-ar
Arabic language for qutIM

# Belarusian language for qutIM
%package -n %name-lang-be
Summary: Belarusian language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-be
Belarusian language for qutIM

# Bulgarian language for qutIM
%package -n %name-lang-bg
Summary: Bulgarian language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-bg
Bulgarian language for qutIM

# Chinese (Simplified) language for qutIM
%package -n %name-lang-cn
Summary: Chinese (Simplified) language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-cn
Chinese (Simplified) language for qutIM

# Czech language for qutIM
%package -n %name-lang-cz
Summary: Czech language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-cz
Czech language for qutIM

# German language for qutIM
%package -n %name-lang-de
Summary: German language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-de
German language for qutIM

# English (United Kingdom) language for qutIM
%package -n %name-lang-en
Summary: English (United Kingdom) language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-en
English (United Kingdom) language for qutIM

# Russian language for qutIM
%package -n %name-lang-ru
Summary: Russian language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-ru
Russian language for qutIM

# Slovak language for qutIM
%package -n %name-lang-sk
Summary: Slovak language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-sk
Slovak language for qutIM

# Ukrainian language for qutIM
%package -n %name-lang-uk
Summary: Ukrainian language for %name
Group: Networking/Instant messaging
Requires: %name = %qversion-%qrelease
BuildArch: noarch

%description -n %name-lang-uk
Ukrainian language for qutIM

# qutIM documentation
%package -n %name-docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
 
%description -n %name-docs
Documentation for qutIM

%prep
%setup -n %name-0.3.1
%patch0 -p1
%patch1 -p1
sed -i 's|TelepathyQt4/|TelepathyQt/|' protocols/astral/src/*.{cpp,h}

%build
export PATH=%_qt4dir/bin:$PATH
%Kbuild \
	-DQUTIM_ADDITIONAL_ART_PATH=../artwork

%install
%Kinstall

%files
%_bindir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libaccountcreator.so
%_libdir/%name/plugins/libaddcontactdlg.so
%_libdir/%name/plugins/libadiumchat.so
%_libdir/%name/plugins/libadiumsrvicons.so
%_libdir/%name/plugins/libauthdialog.so
%_libdir/%name/plugins/libchatnotificationsbackend.so
%_libdir/%name/plugins/libchatspellchecker.so
%_libdir/%name/plugins/libcontactinfo.so
%_libdir/%name/plugins/libdataformsbackend.so
%_libdir/%name/plugins/libemoticonssettings.so
%_libdir/%name/plugins/libfiletransfersettings.so
%_libdir/%name/plugins/libfiletransfer.so
%_libdir/%name/plugins/libidledetector.so
%_libdir/%name/plugins/libidlestatuschanger.so
%_libdir/%name/plugins/libjoinchatdialog.so
%_libdir/%name/plugins/libjoingroupchatdlg.so                                                                                                                                           
%_libdir/%name/plugins/libjsonconfig.so
%_libdir/%name/plugins/libjsonhistory.so
%_libdir/%name/plugins/libkineticscroller.so
%_libdir/%name/plugins/libkopeteemoticonsbackend.so
%_libdir/%name/plugins/liblocalization.so
%_libdir/%name/plugins/libmetacontacts.so
%_libdir/%name/plugins/libmigration02x03.so
%_libdir/%name/plugins/libmobileaboutdialog.so
%_libdir/%name/plugins/libmobilecontactinfo.so
%_libdir/%name/plugins/libmobilenotificationssettings.so
%_libdir/%name/plugins/libmobilesettingsdialog.so
%_libdir/%name/plugins/libnocryptoservice.so
%_libdir/%name/plugins/libnotificationfilter.so
%_libdir/%name/plugins/libnotificationssettings.so
%_libdir/%name/plugins/liboldsoundtheme.so
%_libdir/%name/plugins/libpassword.so
%_libdir/%name/plugins/libplaincontactsmodel.so
%_libdir/%name/plugins/libplistconfig.so
%_libdir/%name/plugins/libproxysettings.so
%_libdir/%name/plugins/libqticons.so
%_libdir/%name/plugins/libsearchdialog.so
%_libdir/%name/plugins/libseparatedcontactsmodel.so
%_libdir/%name/plugins/libservicechooser.so
%_libdir/%name/plugins/libsessionhelper.so
%_libdir/%name/plugins/libshortcutsettings.so
%_libdir/%name/plugins/libsimpleaboutdialog.so
%_libdir/%name/plugins/libsimpleactionbox.so
%_libdir/%name/plugins/libsimpleactions.so
%_libdir/%name/plugins/libsimplecontactdelegate.so
%_libdir/%name/plugins/libsimplecontactlist.so
%_libdir/%name/plugins/libsimplecontactlistwidget.so
%_libdir/%name/plugins/libsimplerosterstorage.so
%_libdir/%name/plugins/libsoundthemeselector.so
%_libdir/%name/plugins/libstackedchatform.so
%_libdir/%name/plugins/libtabbedchatform.so
%_libdir/%name/plugins/libtextchat.so
%_libdir/%name/plugins/libtorycontactlistwidget.so
%_libdir/%name/plugins/libtrayicon.so
%_libdir/%name/plugins/libtreecontactsmodel.so
%_libdir/%name/plugins/libxsettingsdialog.so
%_desktopdir/%name.desktop
%dir %_datadir/apps
%dir %_datadir/apps/%name
%_datadir/apps/%name/icons
%_datadir/apps/%name/sounds
%_datadir/apps/%name/webkitstyle
%_miconsdir/%name.png
%dir %_iconsdir/hicolor/22x22
%dir %_iconsdir/hicolor/22x22/apps
%_iconsdir/hicolor/22x22/apps/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%dir %_iconsdir/hicolor/64x64/places
%_iconsdir/hicolor/64x64/places/user-identity.png
%dir %_iconsdir/hicolor/80x80
%dir %_iconsdir/hicolor/80x80/apps
%_iconsdir/hicolor/80x80/apps/%name.png
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%_iconsdir/hicolor/128x128/apps/%name.png
%dir %_iconsdir/hicolor/256x256
%dir %_iconsdir/hicolor/256x256/apps
%_iconsdir/hicolor/256x256/apps/%name.png
%dir %_iconsdir/hicolor/512x512
%dir %_iconsdir/hicolor/512x512/apps
%_iconsdir/hicolor/512x512/apps/%name.png
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_iconsdir/hicolor/scalable/status
%_iconsdir/hicolor/scalable/status/*.svg
%dir %_iconsdir/ubuntu-mono-dark
%dir %_iconsdir/ubuntu-mono-dark/scalable
%dir %_iconsdir/ubuntu-mono-dark/scalable/status
%_iconsdir/ubuntu-mono-dark/scalable/status/*.svg
%dir %_iconsdir/ubuntu-mono-light
%dir %_iconsdir/ubuntu-mono-light/scalable
%dir %_iconsdir/ubuntu-mono-light/scalable/status
%_iconsdir/ubuntu-mono-light/scalable/status/*.svg
%_pixmapsdir/%name.xpm
%dir %_datadir/%name
%_datadir/%name/config
%_datadir/%name/doc
%dir %_datadir/apps/%name/languages

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_includedir/%name/adiumchat
%_includedir/%name/adiumchat/*.h
%dir %_includedir/%name/simplecontactlist
%_includedir/%name/simplecontactlist/*.h
%dir %_datadir/cmake
%dir %_datadir/cmake/Modules
%_datadir/cmake/Modules/*.cmake

%files -n %name-protocol-astral
%_libdir/%name/plugins/libastral.so

%files -n %name-protocol-irc
%_libdir/%name/plugins/libirc.so

%files -n %name-protocol-jabber
%_libdir/%name/plugins/libjabber.so

%files -n libjreen
%_libdir/libjreen.so.*

%files -n libjreen-devel
%_libdir/libjreen.so
%_pkgconfigdir/libjreen.pc
%dir %_includedir/jreen
%_includedir/jreen/*.h

%files -n %name-protocol-mrim
%_libdir/%name/plugins/libmrim.so

%files -n %name-protocol-oscar
%_libdir/%name/plugins/liboscar.so
%_libdir/%name/plugins/liboscaridentify.so
%_libdir/%name/plugins/liboscarxstatus.so

%files -n %name-protocol-quetzal
%_libdir/%name/plugins/libquetzal.so

%files -n %name-protocol-vkontakte
%_libdir/%name/plugins/libvkontakte.so
%_libdir/%name/plugins/libvphotoalbum.so
%_datadir/apps/%name/vphotoalbum
%_libdir/%name/plugins/libvkontaktewall.so

%files -n %name-plugin-adiumwebview
%_libdir/%name/plugins/libadiumwebview.so
%dir %_datadir/apps/%name/data
%dir %_datadir/apps/%name/data/webview
%_datadir/apps/%name/data/webview

%files -n lib%name-adiumwebview
%_libdir/lib%name-adiumwebview.so.*

%files -n lib%name-adiumwebview-devel
%_libdir/lib%name-adiumwebview.so

%files -n %name-plugin-aescrypto
%_libdir/%name/plugins/libaescrypto.so

%files -n %name-plugin-antiboss
%_libdir/%name/plugins/libantiboss.so

%files -n %name-plugin-antispam
%_libdir/%name/plugins/libantispam.so

%files -n %name-plugin-aspeller
%_libdir/%name/plugins/libaspeller.so

%files -n %name-plugin-bearermanager
%_libdir/%name/plugins/libbearermanager.so

%files -n %name-plugin-birthdayreminder
%_libdir/%name/plugins/libbirthdayreminder.so

%files -n %name-plugin-blogimprover
%_libdir/%name/plugins/libblogimprover.so

%files -n %name-plugin-clconf
%_libdir/%name/plugins/libclconf.so

%files -n %name-plugin-dbusapi
%_libdir/%name/plugins/libdbusapi.so

%files -n %name-plugin-dbusnotifications
%_libdir/%name/plugins/libdbusnotifications.so

%files -n %name-plugin-emoedit
%_libdir/%name/plugins/libemoedit.so

%files -n %name-plugin-floaties
%_libdir/%name/plugins/libfloaties.so

%files -n %name-plugin-highlighter
%_libdir/%name/plugins/libhighlighter.so

%files -n %name-plugin-histman
%_libdir/%name/plugins/libhistman.so

%files -n %name-plugin-hunspeller
%_libdir/%name/plugins/libhunspeller.so

%files -n %name-plugin-kdeintegration
%_libdir/%name/plugins/libkdeintegration.so
%dir %_K4apps/desktoptheme
%dir %_K4apps/desktoptheme/default
%dir %_K4apps/desktoptheme/default/icons
%_K4apps/desktoptheme/default/icons/%name.svg

%files -n %name-plugin-kineticpopups
%_libdir/%name/plugins/libkineticpopups.so
%_datadir/apps/%name/quickpopup

%files -n %name-plugin-linuxintegration
%_libdir/%name/plugins/liblinuxintegration.so

%files -n %name-plugin-logger
%_libdir/%name/plugins/liblogger.so

%files -n %name-plugin-massmessaging
%_libdir/%name/plugins/libmassmessaging.so

%files -n %name-plugin-multimediabackend
%_libdir/%name/plugins/libmultimediabackend.so

%files -n %name-plugin-nowplaying
%_libdir/%name/plugins/libnowplaying.so

%files -n %name-plugin-offtherecord
%_libdir/%name/plugins/libofftherecord.so

%files -n %name-plugin-olddelegate
%_libdir/%name/plugins/liboldcontactdelegate.so

%files -n %name-plugin-phononsound
%_libdir/%name/plugins/libphononsound.so

%files -n %name-plugin-plugman
%_libdir/%name/plugins/libplugman.so

%files -n libquasar
%_libdir/libquasar.so.*

%files -n libquasar-devel
%_libdir/libquasar.so
%_pkgconfigdir/libquasar.pc
%dir %_includedir/quasar
%_includedir/quasar/*.h

%files -n %name-plugin-qmlchat
%_libdir/%name/plugins/libqmlchat.so
%_datadir/apps/%name/qmlchat

%files -n %name-plugin-qrcicons
%_libdir/%name/plugins/libqrcicons.so

%files -n %name-plugin-scriptapi
%_libdir/%name/plugins/libscriptapi.so

%files -n %name-plugin-sdlsound
%_libdir/%name/plugins/libsdlsound.so

%files -n %name-plugin-unreadmessageskeeper
%_libdir/%name/plugins/libunreadmessageskeeper.so

%files -n %name-plugin-updater
%_libdir/%name/plugins/libupdater.so

%files -n %name-plugin-urlpreview
%_libdir/%name/plugins/liburlpreview.so

%files -n %name-plugin-weather
%_libdir/%name/plugins/libweather.so
%dir %_datadir/apps/%name/weatherthemes
%_datadir/apps/%name/weatherthemes

%files -n %name-plugin-yandexnarod
%_libdir/%name/plugins/libyandexnarod.so

%files -n %name-lang-ar
%dir %_datadir/apps/%name/languages/ar
%_datadir/apps/%name/languages/ar/*.qm

%files -n %name-lang-be
%dir %_datadir/apps/%name/languages/be
%_datadir/apps/%name/languages/be/*.qm

%files -n %name-lang-bg
%dir %_datadir/apps/%name/languages/bg
%_datadir/apps/%name/languages/bg/*.qm

%files -n %name-lang-cn
%dir %_datadir/apps/%name/languages/zh_CN
%_datadir/apps/%name/languages/zh_CN/*.qm

%files -n %name-lang-cz
%dir %_datadir/apps/%name/languages/cs
%_datadir/apps/%name/languages/cs/*.qm

%files -n %name-lang-de
%dir %_datadir/apps/%name/languages/de
%_datadir/apps/%name/languages/de/*.qm

%files -n %name-lang-en
%dir %_datadir/apps/%name/languages/en_GB
%_datadir/apps/%name/languages/en_GB/*.qm

%files -n %name-lang-ru
%dir %_datadir/apps/%name/languages/ru
%_datadir/apps/%name/languages/ru/*.qm

%files -n %name-lang-sk
%dir %_datadir/apps/%name/languages/sk
%_datadir/apps/%name/languages/sk/*.qm

%files -n %name-lang-uk
%dir %_datadir/apps/%name/languages/uk
%_datadir/apps/%name/languages/uk/*.qm

%files -n %name-docs
%doc AUTHORS COPYING README.* ChangeLog

%changelog
* Sun Apr 15 2012 Nazarov Denis <nenderus@altlinux.org> 5:0.3.1.0-alt1
- qutim version 0.3.1.0
- jreen version 1.1.0
- Add Off-the-Record plugin
- Add belarisian and slovak translations

* Wed Apr 04 2012 Nazarov Denis <nenderus@altlinux.org> 5:0.3.0.0-alt1
- Version 0.3.0.0

* Tue Apr 03 2012 Sergey V Turchin <zerg@altlinux.org> 4:0.2.80.1-alt3.git20120324
- rebuild with new telepathy-qt4

* Sun Mar 25 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt1.M60T.1.git20120324
- Build for branch t6
- Add arabic and chinese (simplified) translations

* Sat Mar 24 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt2.git20120324
- Version 0.2.80.1 (0.3 beta) from git on 24.03.2012

* Mon Mar 05 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt1.M60P.1.git20120304
- Build for branch p6

* Sun Mar 04 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt1.M60T.1.git20120304
- Build for branch t6

* Sun Mar 04 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt2.git20120304
- Version 0.2.80.1 (0.3 beta) from git on 04.03.2012
- Add qca2-ossl requires

* Thu Mar 01 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt2.git20120301
- Version 0.2.80.1 (0.3 beta) from git on 01.03.2012
- Add Highlighter plugin

* Thu Feb 23 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt1.M60T.1.git20120223
- Build for branch t6

* Thu Feb 23 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt2.git20120223
- Version 0.2.80.1 (0.3 beta) from git on 23.02.2012

* Fri Feb 10 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt1.M60T.1.git20120209
- Build for branch t6

* Fri Feb 10 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt2.git20120209
- Version 0.2.80.1 (0.3 beta) from git on 09.02.2012

* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 4:0.2.80.1-alt1.M60P.1.git20120130
- built for M60P

* Tue Jan 31 2012 Sergey V Turchin <zerg@altlinux.org> 4:0.2.80.1-alt2.git20120130
- rebuilt with kde-4.8

* Tue Jan 31 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt0.M60T.1.git20120130
- Build for branch t6

* Tue Jan 31 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.1-alt1.git20120130
- Version 0.2.80.1 (0.3 beta) from git on 30.01.2012
- Add Adium webview plugin
- Restore aspeller plugin

* Sun Jan 29 2012 Sergey V Turchin <zerg@altlinux.org> 4:0.2.80.0-alt2.git20120111
- rebuilt with kde-4.8
- cleanup spec

* Thu Jan 12 2012 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20120111
- Version 0.2.80.0 (0.3 beta) from git on 11.01.2012

* Tue Dec 13 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20111213
- Version 0.2.80.0 (0.3 beta) from git on 13.12.2011
- Fix undefined symbol: _ZN12QDomDocumentC1Ev

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4:0.2.80.0-alt1.git20111005.1
- Rebuild with Python-2.7

* Wed Oct 05 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20111005
- Version 0.2.80.0 (0.3 beta) from git on 05.10.2011

* Wed Aug 24 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110824
- Version 0.2.80.0 (0.3 beta) from git on 24.08.2011
- Add birthday reminder plugin

* Thu Aug 18 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110818
- Version 0.2.80.0 (0.3 beta) from git on 18.08.2011
- Fix core plugins

* Mon Jul 04 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110704
- Version 0.2.80.0 (0.3 beta) from git on 04.07.2011

* Mon Jun 13 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110613
- Version 0.2.80.0 (0.3 beta) from git on 13.06.2011

* Sun Jun 05 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110605
- Version 0.2.80.0 (0.3 beta) from git on 05.06.2011

* Mon May 30 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110530
- Version 0.2.80.0 (0.3 beta) from git on 30.05.2011

* Mon May 23 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110523
- Version 0.2.80.0 (0.3 beta) from git on 23.05.2011
- Add libqt4-svg requires

* Mon May 16 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110516
- Version 0.2.80.0 (0.3 beta) from git on 16.05.2011
- Rename protocols and plugins packages
- Fix russian description

* Sat May 07 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110507
- Version 0.2.80.0 (0.3 beta) from git on 07.05.2011
- Fix %name-quetzal requires
- Change default settings layer to normal

* Thu May 05 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110505
- Version 0.2.80.0 (0.3 beta) from git on 05.05.2011
- add requires

* Fri Apr 29 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110429
- Version 0.2.80.0 (0.3 beta) from git on 29.04.2011
  + add kineticpopups plugin
- fix post-install unowned files
- fix histman plugin
- add documentation package

* Thu Apr 28 2011 Nazarov Denis <nenderus@altlinux.org> 4:0.2.80.0-alt1.git20110428
- Version 0.2.80.0 (0.3 beta) from git on 28.04.2011

* Sat Oct  2 2010 Terechkov Evgenii <evg@altlinux.org> 3:0.2.0-alt3
- Rebuild with libssl10

* Sun May 23 2010 Terechkov Evgenii <evg@altlinux.ru> 3:0.2.0-alt2
- Fix build with new phonon-devel

* Sat Nov 28 2009 Terechkov Evgenii <evg@altlinux.ru> 3:0.2.0-alt1
- 0.2.0 (ALT #22124)

* Mon Aug  3 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt12.beta2
- 0.2 beta2
- Conflict with old qt4 (ALT #20900, thanks to vsu@)

* Tue Jul  7 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt11.beta
- bin/qutIM compat hardlink removed
- jabber-gnutls subpackage created

* Wed Jun 24 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt10.beta
- x86_64 build again. Authors are morons (ALT #20559)

* Sun Jun 21 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt9.beta
- Vkontakte plugin packaged

* Sun Jun 21 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt8.beta
- Fix some minor packaging errors (desktop, spec)

* Sat Jun 20 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt7.beta
- 0.2 beta
- Development headers packaged in subpackage

* Sat May  9 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt6.alpha
- Build with gcc4.4 fixed

* Wed Mar 18 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt5.alpha
- Build with OpenSSL by default (seems like gmail works only with openssl)
- Split package to plugins subpackages

* Fri Mar 13 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt4.alpha
- Missed optflags and make_build ressurected (thanks to drool@ again)

* Fri Mar 13 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt3.alpha
- Build with Gnutls support (thanks to drool@)

* Mon Mar  9 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt2.alpha
- x86_64 build "fixed" (Authors is idiots)
- bin/qutIM compat hardlink added

* Sun Mar  8 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.2-alt1.alpha
- 0.2 alpha

* Thu Jan 22 2009 Terechkov Evgenii <evg@altlinux.ru> 2:0.1.1-alt2
- Migrate to "one alt patch" gear scheme
- Update spec to new filetriggers system

* Sun Aug 17 2008 Terechkov Evgenii <evg@altlinux.ru> 2:0.1.1-alt1
- 0.1.1

* Sun Aug 17 2008 Evgenii Terechkov <evg@altlinux.ru> 1:0.1-alt1.20080720
- Svn revision: exported

* Sun Jul 20 2008 Evgenii Terechkov <evg@altlinux.ru> 1:0.1-alt1.20080720
- Svn revision: 174

* Wed Jul 09 2008 Evgenii Terechkov <evg@altlinux.ru> 1:0.1-alt1.20080709
- Svn revision: 154

* Wed Jul  2 2008 Terechkov Evgenii <evg@altlinux.ru> 1:0.1-alt1.20080702
- svn-20080702

* Mon Jun 30 2008 Terechkov Evgenii <evg@altlinux.ru> 1:0.1-alt1.20080629
- svn-20080629

* Tue Jun 24 2008 Terechkov Evgenii <evg@altlinux.ru> 1:0.1-alt1.20080624
- Package name changed due changes in upstream
- buildflags added (fix #16149)
- svn-20080624

* Fri Jun 20 2008 Terechkov Evgenii <evg@altlinux.ru> 1:0.1-alt1.20080620
- svn-20080620

* Wed Jun 18 2008 Terechkov Evgenii <evg@altlinux.ru> 1:0.1-alt1.20080618
- svn-20080618
- Obsoleted Patch1 removed (fixed in upstream)

* Wed Jun 18 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt3
- README.ALT included in binary package

* Tue Jun 17 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt2
- Patch1 added to look for emoicons in common dir (to hiddenman@)
- README.ALT added

* Sun Jun 15 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus

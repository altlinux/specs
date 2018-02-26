%define subver 5337

Name: psi-plus
Version: 0.15.%subver
Release: alt1
Group: Networking/Instant messaging

Summary: Psi+ Jabber client
Summary(ru_RU.UTF-8): Jabber клиент Psi+
License: GPL

Url: http://code.google.com/p/psi-dev/
Source0: psi.tar
Source1: psi-plus.tar
Source2: psi-plus-resources.tar
Source3: psi-plus-plugins.tar
Source4: psi-plus-ru.tar

Packager: Anton A. Vinogradov <arc@altlinux.org>
BuildRequires(pre): libqt4-devel libqt4-webkit

Requires: libqt4-core >= %{get_version libqt4-core}
Requires: qca2-ossl
Requires: qca2-gnupg

BuildRequires: gcc-c++ glibc-devel-static libXScrnSaver-devel libaspell-devel libqca2-devel qconf
BuildRequires: libX11-devel libXext-devel icon-theme-hicolor
Conflicts: psi

%description
Psi is a Jabber Instant Messaging client based on Qt.  Jabber supports
gateways (transports) to other IM systems, such as ICQ, MSN, Yahoo and
AIM.  Psi supports many Jabber features, such as simulatenous login to
several servers, conferences, cryptographic abilities (via SSL and
GnuPG), connection via HTTP(S) proxy, etc.
Psi+: Psi IM Mod from psi-dev@conference.jabber.ru

%description -l ru_RU.UTF-8
Psi - это удобный графический клиент сети быстрого обмена сообщениями
Jabber.  Jabber имеет шлюзы в другие сети, включая ICQ, MSN, Yahoo и
AIM.  Psi поддерживает такие возможности Jabber, как одновременная
работа с несколькими серверами, конференции, криптозащиту передаваемой
информации (через SSL и GnuPG), работу через HTTP(S) прокси-сервер и
т.д.
Цель проекта Psi+: сбор, доработка и создание новых патчей с целью передачи их в основную ветвь Psi

# Attention
%package -n %name-plugin-attention
Summary: Attention support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-attention
Obsoletes: %name-attention

%description -n %name-plugin-attention
Attention support plugin for %name

%description -n %name-plugin-attention -l ru_RU.UTF-8
Плагин для отправки и приёма сообщений типа Attention. Для работы необходимо, чтобы клиент собеседника поддерживал XEP-0224: Attention (например: Pidgin, Miranda IM с плагином Nudge) (by Dealer_WeARE)

# Autoreply
%package -n %name-plugin-autoreply
Summary: Autoreply support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-autoreply
Obsoletes: %name-autoreply

%description -n %name-plugin-autoreply
Autoreply support plugin for %name

%description -n %name-plugin-autoreply -l ru_RU.UTF-8
Плагин-автоответчик (by Dealer_WeARE)

# Birthday reminder
%package -n %name-plugin-birthdayreminder
Summary: Birthdayreminder support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-birthdayreminder
Obsoletes: %name-birthdayreminder

%description -n %name-plugin-birthdayreminder
Birthdayreminder support plugin for %name

%description -n %name-plugin-birthdayreminder -l ru_RU.UTF-8
Напоминалка о днях рождения (by Dealer_WeARE)

# Captcha forms
%package -n %name-plugin-captchaforms
Summary: Captcha forms support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-captchaforms
Obsoletes: %name-captchaforms

%description -n %name-plugin-captchaforms
Captcha forms support plugin for %name

# Chess
%package -n %name-plugin-chess
Summary: Chess forms support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-chess
Obsoletes: %name-chess

%description -n %name-plugin-chess
Chess forms support plugin for %name

# Cleaner
%package -n %name-plugin-cleaner
Summary: Cleaner support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-cleaner
Obsoletes: %name-cleaner

%description -n %name-plugin-cleaner
Cleaner support plugin for %name

%description -n %name-plugin-cleaner -l ru_RU.UTF-8
Плагин для очистки кэша аватарок и vCard, а также логов истории (by Dealer_WeARE)

# Client switcher
%package -n %name-plugin-clientswitcher
Summary: Client switcher support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-clientswitcher
Obsoletes: %name-clientswitcher

%description -n %name-plugin-clientswitcher
Client switcher support plugin for %name

# Conference logger
%package -n %name-plugin-conferencelogger
Summary: Conference logger support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-conferencelogger
Obsoletes: %name-conferencelogger

%description -n %name-plugin-conferencelogger
Conference logger support plugin for %name

%description -n %name-plugin-conferencelogger -l ru_RU.UTF-8
Плагин для ведения логов конференций (by Dealer_WeARE)

# Content downloader
%package -n %name-plugin-contentdownloader
Summary: Content downloader support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-contentdownloader
Obsoletes: %name-contentdownloader

%description -n %name-plugin-contentdownloader
Content downloader support plugin for %name

# Extended menu
%package -n %name-plugin-extendedmenu
Summary: Extended menu support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-extendedmenu
Obsoletes: %name-extendedmenu

%description -n %name-plugin-extendedmenu
Extended menu support plugin for %name

# Extended options
%package -n %name-plugin-extendedoptions
Summary: Extended options support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-extendedoptions
Obsoletes: %name-extendedoptions

%description -n %name-plugin-extendedoptions
Extended options support plugin for %name

%description -n %name-plugin-extendedoptions -l ru_RU.UTF-8
Плагин для более удобной настройки дополнительных параметров (advanced options) Psi+ (by Dealer_WeARE)

# GMail notify
%package -n %name-plugin-gmailnotify
Summary: GMail notify support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-gmailnotify
Obsoletes: %name-gmailnotify

%description -n %name-plugin-gmailnotify
GMail notify support plugin for %name

%description -n %name-plugin-gmailnotify -l ru_RU.UTF-8
Уведомления о новых письмах в Gmail (by VampiRUS)

# Gomoku game
%package -n %name-plugin-gomokugame
Summary: Gomoku game support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-gomokugame
Obsoletes: %name-gomokugame

%description -n %name-plugin-gomokugame
Gomoku game support plugin for %name

# History keeper
%package -n %name-plugin-historykeeper
Summary: History keeper support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-historykeeper
Obsoletes: %name-historykeeper

%description -n %name-plugin-historykeeper
History keeper support plugin for %name

# ICQ die
%package -n %name-plugin-icqdie
Summary: ICQ die support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-icqdie
Obsoletes: %name-icqdie

%description -n %name-plugin-icqdie
ICQ die support plugin for %name

%description -n %name-plugin-icqdie -l ru_RU.UTF-8
Плагин для перевода контактов с ICQ на Jabber (by ivan1986)

# Image
%package -n %name-plugin-image
Summary: Image support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-image
Obsoletes: %name-image

%description -n %name-plugin-image
Image support plugin for %name

%description -n %name-plugin-image -l ru_RU.UTF-8
Отправка графических файлов собеседнику в сообщении чата (by VampiRUS)

# Jabber disk
%package -n %name-plugin-jabberdisk
Summary: Jabber disk support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-jabberdisk
Obsoletes: %name-jabberdisk

%description -n %name-plugin-jabberdisk
Jabber disk support plugin for %name

# Juick
%package -n %name-plugin-juick
Summary: Juick support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-juick
Obsoletes: %name-juick

%description -n %name-plugin-juick
Juick support plugin for %name

%description -n %name-plugin-juick -l ru_RU.UTF-8
Плагин для более удобной работы с сервисом juick.com (by VampiRUS)

# Null
%package -n %name-plugin-null
Summary: Null support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-null
Obsoletes: %name-null

%description -n %name-plugin-null
Null support plugin for %name

# Pep change notify
%package -n %name-plugin-pepchangenotify
Summary: Pep change notify support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-pepchangenotify
Obsoletes: %name-pepchangenotify

%description -n %name-plugin-pepchangenotify
Pep change notify support plugin for %name

# QIP X-Statuses
%package -n %name-plugin-qipxstatuses
Summary: QIP X-Statuses support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-qipxstatuses
Obsoletes: %name-qipxstatuses

%description -n %name-plugin-qipxstatuses
QIP X-Statuses support plugin for %name

# Screenshot
%package -n %name-plugin-screenshot
Summary: Screenshot support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-screenshot
Obsoletes: %name-screenshot

%description -n %name-plugin-screenshot
Screenshot support plugin for %name

%description -n %name-plugin-screenshot -l ru_RU.UTF-8
Плагин для создания скриншотов с возможностью отправки на публичный ftp-сервер (by C.H.)

# Skins
%package -n %name-plugin-skins
Summary: Skins support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-skins
Obsoletes: %name-skins

%description -n %name-plugin-skins
Skins support plugin for %name

%description -n %name-plugin-skins -l ru_RU.UTF-8
Данный плагин предназначен для создания, хранения и применения скинов для Psi+. (by Dealer_WeARE)

# Stop spam
%package -n %name-plugin-stopspam
Summary: Stop spam support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-stopspam
Obsoletes: %name-stopspam

%description -n %name-plugin-stopspam
Stop spam support plugin for %name

%description -n %name-plugin-stopspam -l ru_RU.UTF-8
Антиспам-плагин (by Dealer_WeARE)

# Storage notes
%package -n %name-plugin-storagenotes
Summary: Storage notes support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-storagenotes
Obsoletes: %name-storagenotes

%description -n %name-plugin-storagenotes
Storage notes support plugin for %name

%description -n %name-plugin-extendedoptions -l ru_RU.UTF-8
Данный плагин представляет собой реализацию XEP-0049 - Private XML Storage.
Плагин полностью совместим с заметками, сохранёнными из клиента Miranda IM.
Предназначен для хранения заметок на jabber-сервере, с возможностью доступа к ним из любого места через клиент Psi+ или Miranda IM. 

# Translation
%package -n %name-plugin-translate
Summary: Translation support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-translate
Obsoletes: %name-translate

%description -n %name-plugin-translate
Translation support plugin for %name

%description -n %name-plugin-translate -l ru_RU.UTF-8
Транслитерация текста в окне ввода сообщения (by VampiRUS)

# Watcher
%package -n %name-plugin-watcher
Summary: Watcher support for %name
Group: Networking/Instant messaging
Requires: %name = %version-%release
Provides: %name-watcher
Obsoletes: %name-watcher

%description -n %name-plugin-watcher
Watcher support plugin for %name

%description -n %name-plugin-watcher -l ru_RU.UTF-8
Плагин для наблюдения за статусом определённых пользователей в ростере (by Dealer_WeARE)

%prep
%setup -q -n psi
%__tar -xf %SOURCE1
%__tar -xf %SOURCE2
%__tar -xf %SOURCE3
%__tar -xf %SOURCE4

%__cp -a -f psi-plus/iconsets ./
%__cp -a -f psi-plus-resources/{iconsets,skins,sound,themes} ./
%__cp -a -f psi-plus-plugins/* src/plugins/

%__mkdir_p lang/ru

%__cp -a -f psi-plus-ru/{psi_ru.ts,qt} lang/ru

for f in `ls -1 psi-plus/patches/*diff | sort`; do if (patch -p1 --dry-run -i "$f"); then patch -p1 -i "$f"; fi; done
VER=`cat psi-plus/version.txt`
%__subst "s/0.15.xxx/$VER/" src/applicationinfo.cpp

%build
qconf
./configure \
    --prefix=%prefix \
    --bindir=%_bindir \
    --libdir=%_libdir \
    --datadir=%_datadir \
    --qtdir=%_qt4dir \
    --disable-bundled-qca \
    --enable-plugins \
    --enable-webkit \
    --certstore-path=%_datadir/ca-certificates/ca-bundle.crt

%make_build

lrelease-qt4 lang/ru/psi_ru.ts lang/ru/qt/qt_ru.ts

# Attention
pushd src/plugins/generic/attentionplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" attentionplugin.pro
%make_build
popd

# Autoreply
pushd src/plugins/generic/autoreplyplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" autoreplyplugin.pro
%make_build
popd

# Birthday reminder
pushd src/plugins/generic/birthdayreminderplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" birthdayreminderplugin.pro
%make_build
popd

# Capthcha forms
pushd src/plugins/generic/captchaformsplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" captchaformsplugin.pro
%make_build
popd

# Chess
pushd src/plugins/generic/chessplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" chessplugin.pro
%make_build
popd

# Cleaner
pushd src/plugins/generic/cleanerplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" cleanerplugin.pro
%make_build
popd

# Client switcher
pushd src/plugins/generic/clientswitcherplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" clientswitcherplugin.pro
%make_build
popd

# Conference logger
pushd src/plugins/generic/conferenceloggerplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" conferenceloggerplugin.pro
%make_build
popd

# Content downloader
pushd src/plugins/generic/contentdownloaderplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" contentdownloaderplugin.pro
%make_build
popd

# Extended menu
pushd src/plugins/generic/extendedmenuplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" extendedmenuplugin.pro
%make_build
popd

# Extended options
pushd src/plugins/generic/extendedoptionsplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" extendedoptionsplugin.pro
%make_build
popd

# GMail notify
pushd src/plugins/generic/gmailserviceplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" gmailserviceplugin.pro
%make_build
popd

# Gomoku game
pushd src/plugins/generic/gomokugameplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" gomokugameplugin.pro
%make_build
popd

# History keeper
pushd src/plugins/generic/historykeeperplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" historykeeperplugin.pro
%make_build
popd

# ICQ die
pushd src/plugins/generic/icqdieplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" icqdieplugin.pro
%make_build
popd

# Image
pushd src/plugins/generic/imageplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" imageplugin.pro
%make_build
popd

# Jabber disk
pushd src/plugins/generic/jabberdiskplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" jabberdiskplugin.pro
%make_build
popd

# Juick
pushd src/plugins/generic/juickplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" juickplugin.pro
%make_build
popd

# Null
pushd src/plugins/generic/null
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" nullplugin.pro
%make_build
popd

# Pep change notify
pushd src/plugins/generic/pepchangenotifyplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" pepchangenotifyplugin.pro
%make_build
popd

# QIP X-Statuses
pushd src/plugins/generic/qipxstatusesplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" qipxstatusesplugin.pro
%make_build
popd

# Screenshot
pushd src/plugins/generic/screenshotplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" screenshotplugin.pro
%make_build
popd

# Skins
pushd src/plugins/generic/skinsplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" skinsplugin.pro
%make_build
popd

# Stopspam
pushd src/plugins/generic/stopspamplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" stopspamplugin.pro
%make_build
popd

# Storagenotes
pushd src/plugins/generic/storagenotesplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" storagenotesplugin.pro
%make_build
popd

# Translate
pushd src/plugins/generic/translateplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" translateplugin.pro
%make_build
popd

# Watcher
pushd src/plugins/generic/watcherplugin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" watcherplugin.pro
%make_build
popd

%install
%makeinstall INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_libdir/%name/plugins
install -Dp -m 0644 lang/ru/psi_ru.qm %buildroot%_datadir/%name/psi_ru.qm
install -Dp -m 0644 lang/ru/qt/qt_ru.qm %buildroot%_datadir/%name/qt_ru.qm

#Plugins
pushd src/plugins/generic
for i in attentionplugin/libattentionplugin.so \
	 autoreplyplugin/libautoreplyplugin.so \
	 birthdayreminderplugin/libbirthdayreminderplugin.so \
	 captchaformsplugin/libcaptchaformsplugin.so \
	 chessplugin/libchessplugin.so \
	 cleanerplugin/libcleanerplugin.so \
	 clientswitcherplugin/libclientswitcherplugin.so \
	 conferenceloggerplugin/libconferenceloggerplugin.so \
	 contentdownloaderplugin/libcontentdownloaderplugin.so \
	 extendedmenuplugin/libextendedmenuplugin.so \
	 extendedoptionsplugin/libextendedoptionsplugin.so \
	 gmailserviceplugin/libgmailserviceplugin.so \
	 gomokugameplugin/libgomokugameplugin.so \
	 historykeeperplugin/libhistorykeeperplugin.so \
	 icqdieplugin/libicqdieplugin.so \
	 imageplugin/libimageplugin.so \
	 jabberdiskplugin/libjabberdiskplugin.so \
	 juickplugin/libjuickplugin.so \
	 null/libnullplugin.so \
	 pepchangenotifyplugin/libpepchangenotifyplugin.so \
	 qipxstatusesplugin/libqipxstatusesplugin.so \
	 screenshotplugin/libscreenshotplugin.so \
	 skinsplugin/libskinsplugin.so \
	 stopspamplugin/libstopspamplugin.so \
	 storagenotesplugin/libstoragenotesplugin.so \
	 translateplugin/libtranslateplugin.so \
	 watcherplugin/libwatcherplugin.so ;do
  install -Dp -m 0644 $i %buildroot%_libdir/%name/plugins
done
popd

%__rm -Rf %buildroot%_datadir/%name/{README,COPYING,certs}
%__rm %buildroot%_bindir/%name.debug
%__ln_s %name %buildroot%_bindir/psi

%files
%doc README COPYING INSTALL TODO
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_datadir/%name
%attr(0755,root,root) %_bindir/%name
%_bindir/psi
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%_iconsdir/hicolor/128x128/apps/%name.png

# Attention
%files -n %name-plugin-attention
%_libdir/%name/plugins/libattentionplugin.so

# Autoreply
%files -n %name-plugin-autoreply
%_libdir/%name/plugins/libautoreplyplugin.so

# Birthday reminder
%files -n %name-plugin-birthdayreminder
%_libdir/%name/plugins/libbirthdayreminderplugin.so

# Capthcha forms
%files -n %name-plugin-captchaforms
%_libdir/%name/plugins/libcaptchaformsplugin.so

# Chess
%files -n %name-plugin-chess
%_libdir/%name/plugins/libchessplugin.so

# Cleaner
%files -n %name-plugin-cleaner
%_libdir/%name/plugins/libcleanerplugin.so

# Client switcher
%files -n %name-plugin-clientswitcher
%_libdir/%name/plugins/libclientswitcherplugin.so

# Conference logger
%files -n %name-plugin-conferencelogger
%_libdir/%name/plugins/libconferenceloggerplugin.so

# Content downloader
%files -n %name-plugin-contentdownloader
%_libdir/%name/plugins/libcontentdownloaderplugin.so

# Extended menu
%files -n %name-plugin-extendedmenu
%_libdir/%name/plugins/libextendedmenuplugin.so

# Extended options
%files -n %name-plugin-extendedoptions
%_libdir/%name/plugins/libextendedoptionsplugin.so

# Gmail notify
%files -n %name-plugin-gmailnotify
%_libdir/%name/plugins/libgmailserviceplugin.so

# Gomoku game
%files -n %name-plugin-gomokugame
%_libdir/%name/plugins/libgomokugameplugin.so

# History keeper
%files -n %name-plugin-historykeeper
%_libdir/%name/plugins/libhistorykeeperplugin.so

# ICQ die
%files -n %name-plugin-icqdie
%_libdir/%name/plugins/libicqdieplugin.so

# Image
%files -n %name-plugin-image
%_libdir/%name/plugins/libimageplugin.so

# Jabber disk
%files -n %name-plugin-jabberdisk
%_libdir/%name/plugins/libjabberdiskplugin.so

# Juick
%files -n %name-plugin-juick
%_libdir/%name/plugins/libjuickplugin.so

# Null
%files -n %name-plugin-null
%_libdir/%name/plugins/libnullplugin.so

# Pep change notify
%files -n %name-plugin-pepchangenotify
%_libdir/%name/plugins/libpepchangenotifyplugin.so

# QIP X-Statuses
%files -n %name-plugin-qipxstatuses
%_libdir/%name/plugins/libqipxstatusesplugin.so

# Screenshot
%files -n %name-plugin-screenshot
%_libdir/%name/plugins/libscreenshotplugin.so

# Skins
%files -n %name-plugin-skins
%_libdir/%name/plugins/libskinsplugin.so

# Stopspam
%files -n %name-plugin-stopspam
%_libdir/%name/plugins/libstopspamplugin.so

# Storagenotes
%files -n %name-plugin-storagenotes
%_libdir/%name/plugins/libstoragenotesplugin.so

# Translate
%files -n %name-plugin-translate
%_libdir/%name/plugins/libtranslateplugin.so

# Watcher
%files -n %name-plugin-watcher
%_libdir/%name/plugins/libwatcherplugin.so

%changelog
* Fri Jun 08 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5337-alt1
- Version 0.15.5337

* Wed Apr 25 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5320-alt1
- Version 0.15.5320

* Fri Mar 30 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5268-alt1
- Version 0.15.5268

* Sat Mar 24 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5242-alt1
- Version 0.15.5242

* Tue Mar 06 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5225-alt1
- Version 0.15.5225

* Sun Feb 12 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5195-alt1
- Version 0.15.5195

* Sun Jan 29 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5185-alt1
- Version 0.15.5185

* Wed Nov 23 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5145-alt1
- Version 0.15.5145

* Sun Oct 30 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5130-alt1
- Version 0.15.5130

* Tue Oct 04 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5122-alt0.M60T.1
- Build for branch t6

* Mon Oct 03 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5122-alt1
- Version 0.15.5122

* Wed Sep 14 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5116-alt0.M60T.1.svn4128
- Build for branch t6

* Tue Sep 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5116-alt1.svn4128
- Version 0.15.5116
- SVN revision 4128

* Fri Sep 02 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt0.M60T.1.svn4127
- Build for branch t6

* Thu Sep 01 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt1.svn4127
- SVN revision 4127

* Tue Aug 30 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt0.M60T.1.svn4126
- Build for branch t6

* Mon Aug 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt1.svn4126
- Version 0.15.5106
- SVN revision 4126
- Add qca2-gnupg in reqires

* Thu Aug 25 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5091-alt0.M60T.1.svn4125
- Build for branch t6

* Wed Aug 24 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5091-alt1.svn4125
- Version 0.15.5091
- SVN revision 4125
- Add qca2-ossl in reqires

* Thu Aug 18 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5074-alt0.M60T.1.svn4124
- Build for branch t6

* Wed Aug 17 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5074-alt1.svn4124
- SVN revision 4124

* Mon Aug 08 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5074-alt1.svn4123
- Version 0.15.5074
- SVN revision 4123

* Mon Jul 18 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5062-alt0.M60T.1.svn4122
- Build for branch t6

* Mon Jul 18 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5062-alt1.svn4122
- Version 0.15.5062
- SVN revision 4122
- Change profile location from ~/.psi to ~/.config/Psi+ 

* Tue Jul 05 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5031-alt0.M60T.1.svn4120
- Build for branch t6

* Tue Jul 05 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5031-alt1.svn4120
- Version 0.15.5031
- SVN revision 4120

* Fri Jul 01 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.4062-alt0.svn4118.M60T.1
- Build for branch t6

* Fri Jul 01 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.4062-alt1.svn4118
- SVN revision 4118

* Tue Jun 21 2011 Nazarov Denis <nenderus@altlinux.org> 0.15-alt4.svn4062
- SVN revision 4062
- Add plugins:
  - captcha forms  
  - chess
  - client switcher
  - content downloader
  - extended menu
  - gomoku game
  - history keeper
  - jabber disk
  - null
  - pep change notify
  - qip x-statuses

* Wed Mar 30 2011 Grigory Milev <week@altlinux.ru> 0.15-alt3.r3755
- new version 3755
- auto patch from psi to psi+

* Fri Jan 28 2011 Grigory Milev <week@altlinux.ru> 0.15-alt2.r3624
- new git version
- gmailnotifyplugin -> gmailserviceplugin

* Sat Oct 30 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3133
- new nightly revision

* Tue Oct 26 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3125
- new nightly revision

* Sun Oct 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3123
- new nightly revision

* Wed Oct 13 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3086
- new nightly revision

* Sat Jul 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2747
- new nightly revision

* Mon Jul 19 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2702
- new nightly revision

* Sun Jul 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2693
- new nightly revision

* Sun Jul 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2690
- new nightly revision

* Sun Jul 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2689
- new nightly revision
- enable webkit

* Sat Jul 17 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2687
- new nightly revision

* Mon May 31 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2486
- new nightly revision
- disable webkit

* Wed Apr 21 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2180
- new nightly revision

* Sun Apr 11 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2122
- new nightly revision

* Mon Apr 05 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2102
- new nightly revision

* Sat Mar 27 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r2049.1
- new nightly revision
- add skinsplugin
- with "--enable-qtwebkit"

* Mon Mar 22 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r2024.1
- new nightly revision

* Sun Mar 14 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1988.1
- new nightly revision

* Wed Mar 10 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1972.1
- new nightly revision

* Mon Mar 08 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1961.1
- new nightly revision

* Sun Feb 28 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1934.1
- new nightly revision

* Tue Feb 23 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1903.1
- new nightly revision

* Tue Feb 23 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1901.1
- new nightly revision
- add storagenotesplugin

* Mon Feb 22 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1900.1
- new nightly revision

* Sun Feb 14 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1860.1
- new nightly revision
- fixup plugins location (hope it's work)

* Sat Feb 06 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1818
- new nightly revision

* Fri Feb 05 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1813
- Initial build for ALT Linux


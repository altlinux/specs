Version:	1.0
Name:		facebook
Release:	alt1
Summary:	Simple Facebook client
Summary(ru_RU.UTF8): Простой клиент Facebook
Summary(uk_UA.UTF8): Простий клієнт Facebook
License: 	GPLv3+
Group: 		Networking/WWW
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://qt-apps.org/content/show.php/Facebook?content=156543
Source0:	%name.tar.bz2
Source1:	%name.desktop

BuildRequires: gcc-c++ libqt4-devel ImageMagick-tools

%description
Simple and stylish Facebook app. This app provides native Facebook
experience plus a system tray icon for providing notifications.

%description -l ru_RU.UTF8
Простой и стильный клиент Facebook. Это приложение обеспечивает
нативный доступ к Facebook и значек в системном лотке для уведомлений.

%description -l uk_UA.UTF8
Простий і стильний клієнт Facebook. Ця програма забезпечує нативний доступ до
Facebook та значок у системному лотку для сповіщень.

%prep
%setup -q -n %name

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" Facebook.pro
%make_build

%install
install -Dp -m 0755 Facebook %buildroot%_bindir/%name
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 ./res/logo/%name-256x256.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 ./res/logo/%name-256x256.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 ./res/logo/%name-256x256.png %buildroot%_miconsdir/%name.png

%files
%_bindir/*
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Wed Sep 04 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- initial build for ALT Linux

Name:		smtube
Version:	1.8
Release:	alt1
Summary:	Youtube Browser for SMPlayer
Summary(ru_RU.UTF8):	Браузер YouTube для SMPlayer
Summary(uk_UA.UTF8):	Переглядач YouTube для SMPlayer
Summary(de):	Youtube Browser für SMPlayer
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/smplayer/SMTube/%version/%name-%version.tar.bz2

BuildRequires:	gcc-c++ libqt4-devel

Patch0:		%name-1.8_ru-uk_desktop.diff

%description
SMTube is a tool for searching and downloading videos from YouTube.
It supports SMPlayer, VLC and some other players.

%description -l de
Dies ist ein Youtube-Browser für den SMPayer.
Es unterstützt das Durchsuchen von Ordnern, allgemeine Suche, sowie das Downloaden
und Abspielen von Youtube Videos. Die Videos werden derzeit in SMPlayer
abgespielt.

%description -l ru_RU.UTF8
SMTube является утилитой для поиска и скачивания видео с YouTube.
Поддерживается SMPlayer, VLC и некоторые другие проигрыватели.

%description -l uk_UA.UTF8
SMTube є утилітою для пошуку та завантаження відео з YouTube.
Підтримується SMPlayer, VLC та деякі інші програвачі.

%prep
%setup
%patch0 -p1

%build
subst 's|share/doc/smtube|share/doc/smtube-%version|g' Makefile
export PATH=$PATH:%_qt4dir/bin
lrelease ./src/translations/*.ts
cd ./src && qmake "QMAKE_CXXFLAGS+=%optflags -DTRANSLATION_PATH=%_datadir/%name/translations" PREFIX=%_prefix *.pro && cd ../
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%files
%dir %_datadir/%name/translations
%dir %_datadir/%name
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/translations/*.qm

%changelog
* Wed Oct 09 2013 Motsyo Gennadi <drool@altlinux.ru> 1.8-alt1
- initial build for ALT Linux (alt bug #29438)

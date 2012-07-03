%define		_giconsdir %_iconsdir/hicolor/128x128/apps
%define		svn svn26
%define		bld build7

Name:		qgoogletranslate
License:	GPLv2
Group:		System/Internationalization
Version:	0.2b.%bld
Release:	alt1
Summary:	GUI for Google Translate engine
Summary(ru_RU.UTF8): Графический интерфейс к сервису Google Translate
Summary(uk_UA.UTF8): Графічний інтерфейс до сервісу Google Translate
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://code.google.com/p/qgoogletranslate/
Source0:	%name-%svn.tar.bz2
Source1:	%name.desktop

BuildRequires:	/usr/bin/convert gcc-c++ libqt4-devel

Requires:	%{get_dep libqt4-core}

Provides:	google-translator > 0.9.12.20.1
Obsoletes:	google-translator <= 0.9.12.20.1

%description
This application translates text via
Google Translate engine. (http://translate.google.com/)

%description -l ru_RU.UTF8
Программа для перевода текстов с помощью сервиса Google
Translate. (http://translate.google.com/)

%description -l uk_UA.UTF8
Програма для перекладу текстів за допомогою сервісу
Google Translate. (http://translate.google.com/)

%prep
%setup -n %name-svn

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
%make_build

%install
%__install -Dp -m 0755 bin/QGoogleTranslate %buildroot%_bindir/%name
%__install -Dp -m 0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir}
convert -resize 48x48 rc/icons/wicon.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 rc/icons/wicon.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 rc/icons/wicon.png %buildroot%_miconsdir/%name.png
convert -resize 128x128 rc/icons/wicon.png %buildroot%_giconsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_giconsdir/%name.png

%changelog
* Thu Aug 12 2010 Motsyo Gennadi <drool@altlinux.ru> 0.2b.build7-alt1
- initial build for ALT Linux
- fix #23797

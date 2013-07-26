%define		_giconsdir %_iconsdir/hicolor/128x128/apps

Version:	0.9.8
Name:		qtdbf
Release:	alt1
Summary:	A simple DBF viewer and editor
Summary(ru_RU.UTF8): Простой просмотрщик и редактор DBF
Summary(uk_UA.UTF8): Простий переглядач та редактор DBF
License: 	GPLv3+
Group: 		Databases
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.va-soft.ru/project_8.html
Source0:	%name-%version.tar.gz

BuildRequires: ImageMagick-tools gcc-c++ libqt4-devel

Provides:	qtDbf
Obsoletes:	qtDbf < 0.9.4

%description
A simple DBF viewer and editor. Can be set as default dbf viewer.
Supports XBase, dDbase III, IV, FoxPro 2.x, Visual Foxpro files with memos.
Memo content can be viewed but can't be edited yet.

%description -l ru_RU.UTF8
Небольшая утилита для просмотра и редактирования DBF файлов. Поддерживает XBase,
dDbase III, IV, FoxPro 2.x, Visual Foxpro файлы с memo-полями.
Контент memo-полей на данный момент без возможности редактирования.

%description -l uk_UA.UTF8
Невелика утиліта для перегляду та редагування файлів DBF. Підтримує XBase,
dDbase III, IV, FoxPro 2.x, Visual Foxpro файли з memo-полями.
Вміст memo-полів на даний час без можливості редагування.

%prep
%setup -q

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" qtDbf.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir}
convert -resize 48x48 src/images/qtdbf.svg %buildroot%_giconsdir/%name.png
convert -resize 48x48 src/images/qtdbf.svg %buildroot%_liconsdir/%name.png
convert -resize 32x32 src/images/qtdbf.svg %buildroot%_niconsdir/%name.png
convert -resize 16x16 src/images/qtdbf.svg %buildroot%_miconsdir/%name.png

%files
%doc changelog README.md
%dir %_datadir/%name
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name

%changelog
* Fri Jul 26 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Thu Jul 25 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Mon Jul 22 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Thu Jul 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Fri Jul 12 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Wed Jul 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.3-alt2
- fixed MimeTipe in desktop-file

* Wed Jul 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.3-alt1
- initial build for ALT Linux

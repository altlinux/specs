Version:	1.0.0
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

Requires:	libqt4-sql-sqlite
BuildRequires:	gcc-c++ libqt4-devel

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
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc ChangeLog README.md
%dir %_datadir/%name
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name

%changelog
* Mon Oct 07 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Aug 29 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.11-alt2
- fix

* Thu Aug 29 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Wed Aug 21 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.10.3-alt1
- Ukrainian translation

* Tue Aug 20 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.10.2-alt1
- Bugfix release

* Sat Aug 03 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.10.1-alt2
- add requires for libqt4-sql-sqlite (alt bug #29261)

* Fri Aug 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.10.1-alt1
- Bugfix filter for field of types I and N

* Fri Aug 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Mon Jul 29 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Fri Jul 26 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.8.1-alt1
- bugfix release

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

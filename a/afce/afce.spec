Name: afce
Version: 0.9.8
Release: alt2
License: GPL
Group: Development/Other
Source: v%version.tar.gz
Url: http://vicking.narod.ru/flowchart
%define summary_en Flowchart editor with code generation and vector graphics
Summary: %summary_en
Summary(ru_RU.UTF-8):	Редактор блок-схем с генерацией исходных текстов и векторных диаграмм


BuildRequires(pre): rpm-build-xdg
# Automatically added by buildreq on Mon Oct 19 2015
# optimized out: libGL-devel libqt5-core libqt5-gui libqt5-printsupport libqt5-svg libqt5-widgets libqt5-xml libstdc++-devel qt5-base-devel
BuildRequires: gcc-c++ qt5-svg-devel qt5-tools qt5-translations

%description
%name -- %summary_en

%description -l ru_RU.UTF-8
Вашему вниманию представляется программа, которая предназначена для
создания, редактирования и экспорта блок-схем алгоритмов. Пользователю
не нужно заботиться о размещении и выравнивании объектов, программа
автоматически разместит все блоки. Редактор позволит экспортировать
блок-схему в исходный текст программы для разных языков программирования
(Pascal, C/C++, Алгоритмический язык). Редактор блок-схем позволяет
экспортировать изображение схемы в различные графические форматы: BMP,
JPEG, PNG, TIFF, ICO, PPM, XBM, XPM, SVG. Программа распространяется на
условиях лицензии GNU General Public License (GPL). Программа написана
на языке C++ на основе библиотеки Qt 4

Возможности

    * генерация исходного кода на основе блок-схемы в различные языки программирования;
    * автоматическое размещение блоков на схеме;
    * экспорт схемы в популярные растровые форматы;
    * экспорт схем в векторный формат SVG;
    * возможность работы с буфером обмена;
    * масштабирование блок-схемы;
    * поддержка нескольких языков переводов;
    * конвертация блок-схемы в исходный код на нескольких языках программирования;
    * бесплатность и открытость программы;
    * открытый формат файла, основанный XML;
    * кроссплатформенность: имеются сборки для Microsoft Windows и GNU/Linux.

%prep
%setup
sed -i "/Category=/aEducation;" afce.desktop

%build
qmake-qt5
%make_build

%install
INSTALL_ROOT=%buildroot %make install STRIP=touch

# TODO checko if this still needed
install locale/afce*.qm %buildroot%_datadir/%name/locale/

install -D %name.png %buildroot%_niconsdir/%name.png
install -D %name.png %buildroot%_liconsdir/%name.png

%files
%doc README*
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_iconsdir/*.ico
%_pixmapsdir/*.png
%_desktopdir/*
%_xdgmimedir/packages/*

%changelog
* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.8-alt2
- Updated build dependencies

* Mon Oct 19 2015 Fr. Br. George <george@altlinux.ru> 0.9.8-alt1
- Autobuild version bump to 0.9.8
- Rebuild with Qt5

* Fri Sep 23 2011 Fr. Br. George <george@altlinux.ru> 0.9.0-alt2.nntc095
- Temporary build new version from http://blog.nntc.nnov.ru/?p=1326

* Wed Jul 28 2010 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1.51
- Initial build from scratch

Name:		afce
%define rel 51
Version:	0.9.0
#Release:	alt1.%rel
Release:	alt2.nntc095
License:	GPL
Group:		Development/Other
Source1:	http://vicking.narod.ru/flowchart/%name-%version-%rel.tar.gz
Source:		afce-095-nntc-edition.tar.gz
URL:		http://vicking.narod.ru/flowchart
%define summary_en Flowchart editor with code generation and vector graphics
%define summary_ru Редактор блок-схем с генерацией исходных текстов и векторных диаграмм
Summary:		%summary_en
Summary(ru_RU.UTF-8):	%summary_ru

# Automatically added by buildreq on Wed Jul 28 2010
BuildRequires: gcc-c++ libqt4-devel

%description
%name -- %summary_en

There's no english documentation on %name, although it's interface
supports english so you can easily try it on you intuition.

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
#setup -n %name-%version-%rel
%setup -n %name
sed -i 's@/usr/share/doc/packages/afce@%_datadir/%name@g' thelpwindow.cpp
mv doc/primer.PNG doc/primer.png
cat > %name.desktop <<@@@
[Desktop Entry]
Name=Flowchart editor
Name[ru]=Редактор блок-схем
Comment=%summary_en
Comment[ru]=%summary_ru
Type=Application
Exec=%name
Icon=%name
Categories=QT;Development;GUIDesigner;
@@@

%build
qmake-qt4
make clean
%make_build

%install
mkdir -p %buildroot%_datadir/%name
install *.ts %buildroot%_datadir/%name/
install doc/* %buildroot%_datadir/%name/
install -D %name %buildroot%_bindir/%name
install -D %name.png %buildroot%_niconsdir/%name.png
install -D %name.png %buildroot%_liconsdir/%name.png
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc doc README*
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%changelog
* Fri Sep 23 2011 Fr. Br. George <george@altlinux.ru> 0.9.0-alt2.nntc095
- Temporary build new version from http://blog.nntc.nnov.ru/?p=1326

* Wed Jul 28 2010 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1.51
- Initial build from scratch


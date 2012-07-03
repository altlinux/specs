%define progname leocad
Summary: Data files for %progname: bricks, textures and font
Summary(ru_RU.KOI8-R): Файлы для %progname: описание блоков, текстуры и шрифт
Name:    leocad-data
#pieces-3934.zip (2010-09-22)
Version: 0.75.20100922
# 03-May-2009
Release: alt1

License: Distributable
Url:     http://www.leocad.org
Source1: http://www.leocad.org/files/pieces.zip
Group:   Games/Puzzles
Packager: Fr. Br. George <george@altlinux.ru>

BuildArch: noarch
BuildRequires: unzip

%description
Pieces, textures and font for LeoCAD

%description -l ru_RU.KOI8-R
Описание блоков, текстуры и шрифт для LeoCAD

%prep
unzip %SOURCE1

%build

%install
mkdir -p %buildroot%_datadir/%progname
for N in *; do install $N %buildroot%_datadir/%progname/; done

%files
%_datadir/%progname/*

%changelog
* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.75.20100922-alt1
- updated to pieces-3934.zip (2010-09-22)

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.75.20090503-alt1
- Fresh unversioned files

* Sun Oct 07 2007 Fr. Br. George <george@altlinux.ru> 0.75-alt1
- Initial build for ALT


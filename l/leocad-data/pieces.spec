%define progname leocad
Summary: Data files for %progname: bricks, textures and font
Summary(ru_RU.UTF-8): Файлы для %progname: описание блоков, текстуры и шрифт
Name: leocad-data
Version: 11331
Release: alt1

License: Distributable
Url: http://www.leocad.org
Source: pieces-%version.zip
Group: Games/Puzzles
Packager: Fr. Br. George <george@altlinux.ru>

BuildArch: noarch
BuildRequires: unzip

%description
Pieces, textures and font for LeoCAD

%description -l ru_RU.UTF-8
Описание блоков, текстуры и шрифт для LeoCAD

%prep
%setup -c

%build
%install
mkdir -p %buildroot%_datadir/%progname
for N in *; do install $N %buildroot%_datadir/%progname/; done

%files
%_datadir/%progname/*

%changelog
* Mon Jun 04 2018 Grigory Ustinov <grenka@altlinux.org> 11331-alt1
- Build new version (for %progname 18.02) (Closes: #34979).

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 7439-alt1
- Autobuild version bump to 7439

* Mon Mar 25 2013 Fr. Br. George <george@altlinux.ru> 7114-alt1
- Autobuild version bump to 7114

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.75.20100922-alt1
- updated to pieces-3934.zip (2010-09-22)

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.75.20090503-alt1
- Fresh unversioned files

* Sun Oct 07 2007 Fr. Br. George <george@altlinux.ru> 0.75-alt1
- Initial build for ALT


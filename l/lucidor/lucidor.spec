# SPEC file for Lucidor
#

Name:     lucidor
Version:  0.9.15
Release:  alt2

Summary: E-book reader application

Group:    Text tools
License:  %gpl3plus
URL:      http://lucidor.org/lucidor/
Packager: Nikolay Fetisov <naf@altlinux.ru>

ExclusiveArch: x86_64 aarch64 

Source0: %name-%version.tar
Source1: ru-RU.tar 


Patch0: %name-0.9.7-alt-desktop.patch
Patch1: %name-0.9.15-alt-basilisk.patch

Patch2: %name-0.9.15-translate_ru.patch
Patch3: %name-0.9.15-collection.patch
Patch4: %name-0.9.15-language.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: desktop-file-utils

# Automatically added by buildreq on Thu Jan 05 2012
# optimized out: fontconfig libgdk-pixbuf
BuildRequires: librsvg-utils

%description
Lucidor is a computer program for reading and handling e-books.
Lucidor supports e-books in the EPUB file format, and catalogs
in the OPDS format.

Lucidor provides functionality to:
- Read EPUB e-books.
- Organize a collection of e-books in a local bookcase.
- Search for and download e-books from the Internet, 
  for example by browsing OPDS catalogs.
- Convert web feeds into e-books.

%description -l ru_RU.UTF-8
Lucidor - компьютерная программа для чтения электронных книг и работы с ними.
Lucidor поддерживает электронные книги в формате epub и каталогив формате OPDS.

Lucidor позволяетя:
- Читать электронные книги формата epub.
- Организовать собственную коллекциию электронных книг в виде локальной книжной полки.
- Искать и загружать электронные книги из Интернета, например, просматривая каталоги OPDS.
- Конвертировать веб-каналы в электронные книги.

%prep
%setup
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cd lucidor/chrome/locale/
tar -xf %SOURCE1
cd -

rm  gpl-3.0.txt
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/gpl-3.0.txt) gpl-3.0.txt


%build
%make

%install
%make install install-man install-mime DESTDIR=%buildroot

install -d %buildroot%_miconsdir %buildroot%_niconsdir %buildroot%_liconsdir
/usr/bin/rsvg-convert -w 16 -h 16 -f png -o %buildroot%_miconsdir/%name.png -- data/icons/scalable/apps/lucidor.svg
/usr/bin/rsvg-convert -w 32 -h 32 -f png -o %buildroot%_niconsdir/%name.png -- data/icons/scalable/apps/lucidor.svg
/usr/bin/rsvg-convert -w 48 -h 48 -f png -o %buildroot%_liconsdir/%name.png -- data/icons/scalable/apps/lucidor.svg

%files
%doc credits.txt readme.html style.css
%doc --no-dereference gpl-3.0.txt

%_bindir/%name
%_datadir/%{name}*
%_man1dir/%{name}*

%_pixmapsdir/%name.*
%_desktopdir/%name.desktop

%_datadir/mime/packages/%name.xml

%exclude /usr/lib/mime/packages/lucidor

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Thu Nov 23 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.9.15-alt2
- Add Russin Translate

* Tue Oct 10 2023 Pavel Vasenkov <pav@altlinux.org> 0.9.15-alt1
- New version (Closes: #47908)

* Mon Sep 18 2023 Pavel Vasenkov <pav@altlinux.org> 0.9.10-alt4
- ExcludeArch: %{ix86} ppc64le

* Sun Jan 03 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt3
- ExcludeArch: armh

* Tue Feb 02 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.10-alt2
- Removing xulrunner usage

* Fri Sep 04 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.10-alt1
- New version (Closes: 31253)

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.8-alt1
- New version

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.7-alt1
- Initial build for ALT Linux Sisyphus




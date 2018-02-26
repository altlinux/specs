# SPEC file for Lucidor
#

Name:     lucidor
Version:  0.9.7
Release:  alt1

Summary: E-book reader application

Group:    Text tools
License:  %gpl3plus
URL:      http://lucidor.org/lucidor/
Packager: Nikolay Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source0: %name-%version.tar

Patch0: %name-0.9.7-alt-desktop.patch

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

%prep
%setup
%patch0

mv gpl-3.0.txt gpl-3.0.txt.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/gpl-3.0.txt) gpl-3.0.txt

%build
make

%install
make install install-man install-mime DESTDIR=%buildroot

mkdir -p %buildroot%_miconsdir %buildroot%_niconsdir %buildroot%_liconsdir
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
* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.7-alt1
- Initial build for ALT Linux Sisyphus

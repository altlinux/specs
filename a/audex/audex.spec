Name:		audex
Version:	0.74b1
Release:	alt1
Summary:	Audex is a new audio grabber tool for CD/DVD drives

Source0:	%name-%version.tar.bz2

Url:		http://opensource.maniatek.de/cgi-bin/audex/audex/
Group:		Sound
License:	GPLv2/LGPLv2.1
Packager:	Alex Karpov <karpov@altlinux.ru>

# Automatically added by buildreq on Tue Dec 22 2009
BuildRequires: cmake gcc-c++ kde4multimedia-devel kdemultimedia-libs libcdparanoia-devel libqt4-devel kde4libs-devel

#BuildRequires: cmake gcc-c++ ImageMagick libcdparanoia-devel libqt4-devel libqt4-network libqt4-sql

%description
Audex is a new audio grabber tool for CD-ROM drives based
on the application development framework Qt 4 (4.3.x). Archival
functions of the extended database mode are in the focus by now.
Several people can use audex to extract their audio cds and sync
metadata with a single sql database. Every time someone wants to
extract an audio cd that still exists in the database audex will
deny extracting. In normal mode audex behaves just like every cdda
extractor.
 
 Some more features:
 - Extracting with CDDA Paranoia. So you have quite perfect audio quality.
 - Extracting and encoding run parallel.
 - Filename editing with local and remote CDDB/FreeDB database.
 - Submit new entries to CDDB/FreeDB database.
 - Metadata correction tools like capitalize etc.
 - Multi-profile extraction (with one commandline-encoder per profile).
 - Synchronisation of metadata and even covers with MySQL/PostgreSQL/Firebird-Databases (e.g. explore it with a PHP-webinterface).
 - Fetch covers from amazon and store them in the database.
 - Create playlists and cover files in target directory.
 - Correct handling of samplers und multi-cd-albums.
 - Creates extraction and encoding protocols.
 - Proxy settings.

%prep
%setup -qn %name

%build
cmake -D CMAKE_INSTALL_PREFIX="/usr" .
%make_build

%install
mkdir %buildroot
%make_install DESTDIR="%buildroot" install

%find_lang %name

%files -f %name.lang
%doc LICENCE README TODO CHANGELOG
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/kde4/%name.desktop
%_datadir/apps/%name
%_datadir/apps/solid

%changelog
* Wed Aug 24 2011 Alex Karpov <karpov@altlinux.ru> 0.74b1-alt1
- new version

* Fri Jan 07 2011 Alex Karpov <karpov@altlinux.ru> 0.73b2-alt1
- new version

* Fri Nov 19 2010 Alex Karpov <karpov@altlinux.ru> 0.72b1-alt1.2
- really fixed build

* Tue Mar 09 2010 Alex Karpov <karpov@altlinux.ru> 0.72b1-alt1.1
- fix build (or not)

* Tue Dec 22 2009 Alex Karpov <karpov@altlinux.ru> 0.72b1-alt1
- new version. Now it is almost usable.
    + updated build requirements

* Fri Feb 27 2009 Alex Karpov <karpov@altlinux.ru> 0.62b-alt1
- new version

* Tue Dec 11 2007 Alex Karpov <karpov@altlinux.ru> 0.47dev-alt1
- new development version

* Thu Nov 29 2007 Alex Karpov <karpov@altlinux.ru> 0.46b-alt1
- first build for ALT Linux Sisyphus

* Sat Oct 27 2007 Motsyo Gennadi <drool@altlinux.ru> 0.46b-alt0
- initial build for ALT Linux

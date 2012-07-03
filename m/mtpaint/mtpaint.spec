%define docver 3.40

Summary: Painting program for creating icons and pixel-based artwork
Name: mtpaint
Version: 3.40
Release: alt2
License: GPLv3+
Group: Graphics
Url: http://mtpaint.sourceforge.net/
Source: %name-%version.tar.bz2
Source1: http://downloads.sf.net/%name/%{name}_handbook-%docver.zip
Patch: %name-3.40-xdg-open.patch
Patch1: %name-3.40-openjpeg.patch

BuildRequires: gtk2-devel zlib-devel unzip
BuildRequires: libpng-devel libungif-devel libjpeg-devel libtiff-devel
BuildRequires: desktop-file-utils gettext dos2unix

Requires: %name-handbook

%description
mtPaint is a simple painting program designed for creating icons and
pixel-based artwork. It can edit indexed palette or 24 bit RGB images
and offers basic painting and palette manipulation tools. Its main
file format is PNG, although it can also handle JPEG, GIF, TIFF, BMP,
XPM, and XBM files.

%package handbook
Summary: Handbook for the mtpaint painting application
Group: Graphics
License: GFDL
Buildarch: noarch
Requires: %name = %version-%release

%description handbook
Install this package is want to read the handbook for the painting
application mtpaint.

%prep
%setup -a 1
%patch -p1
%patch1 -p1

# We have moved docs
sed -i 's,#define HANDBOOK_LOCATION "/usr/doc/mtpaint/index.html",#define HANDBOOK_LOCATION "%_docdir/%name-handbook-%version/index.html",' src/spawn.c

chmod 0755 %{name}_handbook-%docver/docs/{en_GB,img,files,cs}
dos2unix -k %{name}_handbook-%docver/docs/index.html
dos2unix -k %{name}_handbook-%docver/docs/{en_GB,cs}/*.html

%build
# This is not a "normal" configure
./configure --datarootdir=%_datadir \
	cflags asneeded debug intl man gtk2 tiff jpeg GIF
%make_build

%install
rm -rf %buildroot
%makeinstall MT_PREFIX=%buildroot%prefix            \
                  MT_MAN_DEST=%buildroot%_mandir     \
		  MT_DATAROOT=%buildroot%_datadir \
                  MT_LANG_DEST=%buildroot%_datadir/locale \
                  BIN_INSTALL=%buildroot%_bindir

desktop-file-install --delete-original         \
    --vendor "" \
    --dir %buildroot%_datadir/applications \
    %buildroot%_datadir/applications/%name.desktop
%find_lang %name

%files -f %name.lang
%doc COPYING NEWS README
%_mandir/man1/%{name}*
%_bindir/%name
%_datadir/applications/*.desktop
%_datadir/pixmaps/%name.png

%files handbook
%doc %{name}_handbook-%docver/COPYING %{name}_handbook-%docver/docs/*

%changelog
* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 3.40-alt2
- Fix i18n and HTML help

* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 3.40-alt1
- Autobuild version bump to 3.40

* Sat Jul 24 2010 Fr. Br. George <george@altlinux.ru> 3.31-alt1
- Version up

* Sat Mar 07 2009 Fr. Br. George <george@altlinux.ru> 3.30-alt1
- Version up

* Fri Dec 12 2008 Fr. Br. George <george@altlinux.ru> 3.21-alt1
- Initial build from FC

* Fri Aug 15 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.21-1
- 3.21
- add %%defattr on handbook

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.20-3
- Rebuild

* Wed Jan 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.20-2
- Unzip by %%setup
- Simplify %%post/postun
- Added COPYING to handbook

* Sat Dec 29 2007 Terje Rosten <terje.rosten@ntnu.no> - 3.20-1
- 3.20
- include patch now upstream
- handbook patch now upstream

* Wed Dec 19 2007 Terje Rosten <terje.rosten@ntnu.no> - 3.20-0.1.rc2
- 3.20RC2
- disable openjpeg support
- icon and desktop file now upstream

* Sun Dec 16 2007 Terje Rosten <terje.rosten@ntnu.no> - 3.19-1
- upgrade to 3.19
- misc fixes to be rpmlint clean
- fix debuginfo package
- handle translations
- fix license
- compile with correct flags
- add patch to compile
- add handbook subpackage (and fix app to find docs)
- add xdg-open patch
- dont' use %%makeinstall
- add icon and mimetypes to desktop file

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 3.11-1 - 5280/dries
- Updated to release 3.11.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Updated to release 3.02.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 3.01-1
- Updated to release 3.01.

* Wed May 31 2006 Dries Verachtert <dries@ulyssis.org> - 2.31-1
- Updated to release 2.31.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.30-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.30-1
- Updated to release 2.30.

* Sun Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.20-1
- Updated to release 2.20.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.

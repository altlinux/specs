%define docver 3.49.03

Summary: Painting program for creating icons and pixel-based artwork
Name: mtpaint
Version: 3.50
Release: alt1
License: GPL-3.0+
Group: Graphics
Url: http://mtpaint.sourceforge.net/
Source: %name-%version.tar.bz2
Source1: http://downloads.sf.net/%name/%{name}_handbook-%docver.zip
Patch1: %name-xdg-open.patch
Patch2: %name-openjpeg.patch

# Automatically added by buildreq on Tue Apr 06 2021
# optimized out: at-spi2-atk fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libpng-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python2-base sh4 xorg-proto-devel zlib-devel
BuildRequires: libgif-devel libgtk+3-devel libjpeg-devel libtiff-devel unzip

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
%patch1 -p2
%patch2 -p2

%build
# This is not a "normal" configure
CFLAGS=-fcommon ./configure --datarootdir=%_datadir \
	cflags asneeded debug intl man gtk3 tiff jpeg GIF
sed -i "s/ -ggdb/ -fcommon -ggdb/" _conf.txt
%make_build

%install
%makeinstall MT_PREFIX=%buildroot%prefix            \
                  MT_MAN_DEST=%buildroot%_mandir     \
		  MT_DATAROOT=%buildroot%_datadir \
                  MT_LANG_DEST=%buildroot%_datadir/locale \
                  BIN_INSTALL=%buildroot%_bindir

desktop-file-install --delete-original         \
    --vendor "" \
    --dir %buildroot%_datadir/applications \
    %buildroot%_datadir/applications/%name.desktop

mkdir -p %buildroot%_defaultdocdir/%name
cp -a %{name}_handbook-%docver/docs/* %buildroot%_defaultdocdir/%name

%find_lang %name

%files -f %name.lang
%doc COPYING NEWS README
%_bindir/%name
%_man1dir/%name.1*
%_desktopdir/*.desktop
%_datadir/pixmaps/%name.png

%files handbook
%_defaultdocdir/%name/

%changelog
* Tue Apr 06 2021 Fr. Br. George <george@altlinux.ru> 3.50-alt1
- Autobuild version bump to 3.50
- Switch to GTK3

* Wed Jun 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.49.27-alt1
- New version from https://github.com/wjaguar/mtPaint.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.40-alt2.1
- Rebuilt with libpng15

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

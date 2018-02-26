%define series 2.7.5
%define patchlevel 2
%define tstamp 13May11

Name: RasMol
Version: %series.%patchlevel
Release: alt3

Summary: Molecular Graphics Visualisation Tool
License: GPL-like
Group: Sciences/Chemistry

Url: http://www.openrasmol.org
Source: http://sourceforge.net/projects/openrasmol/files/RasMol/RasMol_%series/rasmol-%series.%patchlevel-%tstamp.tar.gz
Source1: rasmol.sh
Source2: rasmol.xpm
Source3: rasmol_16x14.png
Source4: rasmol_32x29.png
Source5: rasmol_64x58.png
Source6: rasmol.desktop
Patch: RasMol-2.7.5-gentoo-bundled-lib.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Инструмент для визуализации молекулярных структур
Summary(uk_UA.KOI8-U): ╤нструмент для в╕зуал╕зац╕╖ молекулярних структур

# Automatically added by buildreq on Fri Sep 23 2011
# optimized out: CBFlib CQRlib CVector CVector-devel NearTree libX11-devel libXext-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libCBFlib-devel libCQRlib-devel libNearTree-devel imake libXi-devel libgfortran-devel xorg-cf-files

Provides: rasmol = %version-%release
Requires: fonts-bitmap-75dpi xdpyinfo

%description
RasMol is a molecular graphics program intended for the visualisation of
proteins, nucleic acids and small molecules. The program is aimed at
display, teaching and generation of publication quality images.

%description -l ru_RU.KOI8-R
RasMol - программа молекулярной графики, используемая для визуализации
протеинов, нуклеиновых кислот и небольших молекул.  Пригодна для
отображения, обучения и генерации изображений для публикаций.

%description -l uk_UA.KOI8-U
RasMol - програма молекулярно╖ граф╕ки, що застосову╓ться для
в╕зуал╕зац╕╖ проте╖н╕в, нукле╖нових кислот та невеликих молекул.
Придатна до в╕дображення, навчання та генерац╕╖ зображень для
публ╕кац╕й.

%prep
%setup
%patch -p1
sed -i 's,^#include \(<\|"\)cbf,#include \1cbf/cbf,' src/{cif.h,maps.c}

%build
CFLAGS="%optflags"
pushd src
xmkmf
subst 's/-mcpu=i686/-mtune=i686/' Makefile
make clean rasmol "DEPTHDEF=-DEIGHTBIT"
mv rasmol rasmol-8bpp
make clean rasmol "DEPTHDEF=-DSIXTEENBIT"
mv rasmol rasmol-16bpp
make clean rasmol "DEPTHDEF=-DTHIRTYTWOBIT"
mv rasmol rasmol-32bpp
popd

%install
find -type f -name .DS_Store -execdir rm {} +

install -pDm755 %SOURCE1 %buildroot%_bindir/rasmol
install -pm755 src/rasmol-8bpp %buildroot%_bindir/rasmol-8bpp
install -pm755 src/rasmol-16bpp %buildroot%_bindir/rasmol-16bpp
install -pm755 src/rasmol-32bpp %buildroot%_bindir/rasmol-32bpp

mkdir -p %buildroot%_datadir/%name %buildroot%_man1dir/
install -pm644 doc/rasmol.1.gz %buildroot%_man1dir/rasmol.1.gz
install -pm644 doc/rasmol.hlp %buildroot%_datadir/%name/rasmol.hlp
install -pm644 doc/rasmol.html %buildroot%_datadir/%name/rasmol.html

pushd doc
rm rasmol.hlp rasmol.html rasmol.1.gz
mkdir doc
install -pm644 *.html *.pdf.gz *.ps.gz *.rtf.gz rasmol.doc.gz doc/
mkdir examples
popd

mv data/* doc/examples/

install -pDm644 %SOURCE2 %buildroot%_niconsdir/rasmol.xpm
install -pDm644 %SOURCE3 %buildroot%_iconsdir/hicolor/16x16/apps/rasmol.png
install -pDm644 %SOURCE4 %buildroot%_iconsdir/hicolor/32x32/apps/rasmol.png
install -pDm644 %SOURCE5 %buildroot%_iconsdir/hicolor/64x64/apps/rasmol.png
install -pDm644 %SOURCE6 %buildroot%_desktopdir/%name.desktop

%files
%doc doc/
%doc NOTICE PROJECTS RASLIC README* INSTALL* TODO* ChangeLog* history.html
%_bindir/*
%_niconsdir/rasmol.xpm
%_iconsdir/hicolor/??x??/apps/rasmol.png
%_desktopdir/%name.desktop
%_datadir/%name/
%_man1dir/*

# TODO:
# - consider adding rasmol-gtk

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 2.7.5.2-alt3
- rebuilt with current NearTree

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.7.5.2-alt2
- wrapper Requires: xdpyinfo
- tweaked desktop file with a few {th,str}ings
  from debian's rasmol-classic.desktop

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.7.5.2-alt1
- 2.7.5.2
- applied Gentoo patch to avoid extra bundling

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 2.7.3.1-alt6
- adapted freedesktop menu file from Mandriva
- applied repocop patch

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 2.7.3.1-alt5
- fix build (buildreq)
- removed debian menufile
- NB: 2.7.4.2 out there; build changed

* Mon Sep 01 2008 Michael Shigorin <mike@altlinux.org> 2.7.3.1-alt4
- fix build (libXext-devel)

* Tue May 06 2008 Michael Shigorin <mike@altlinux.org> 2.7.3.1-alt3
- cleanup OSX metadata, thanks viy@

* Wed Mar 26 2008 Michael Shigorin <mike@altlinux.org> 2.7.3.1-alt2
- added font dependency, thanks Denis Medvedev (nbr@); fixes #15051

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 2.7.3.1-alt1
- 2.7.3.1, see the patch list here:
  http://www.openrasmol.org/#pending_2_7_4
- spec macro abuse cleanup
- buildreq
- s/-mcpu=i686/-mtune=athlon/
  (since pentium4 isn't worth the trouble ;-P )

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 2.7.3-alt1
- 2.7.3
- fixed #5622 (one-byte, cosmetic)
- spec update/cleanup

* Fri Aug 15 2003 Michael Shigorin <mike@altlinux.ru> 2.7.1.1-alt1
- multi build for 8/16/32-bpp, modified wrapper to select proper binary
- spec cleanup

* Sat Jun 28 2003 Denis G. Samsonenko <denis@che.nsk.su>
- build for ALTLinux Master 2.2

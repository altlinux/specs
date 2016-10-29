Name: blobwars
Version: 1.19
Release: alt2

Summary: Mission and Objective based 2D Platform Game
License: %gpl2plus
Group: Games/Arcade

Url: http://www.parallelrealities.co.uk/blobWars.php
Source: %name-%version.tar
Patch1: %name-1.19-alt-fix-as-needed-linking.patch
Patch2: %name-1.19-alt-fixes.patch
#found in fc
Patch3: blobwars-1.19-check-chdir-ret.patch
#found in suse
Patch4: blobwars-icons_blobwars.desktop.patch
Patch5: blobwars-1.19-fix-gzclose.patch
Source1: %{name}.appdata.xml


BuildRequires: rpm-build-licenses

BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libSDL_net-devel zlib-devel

%description
Blob Wars : Metal Blob Solid. This is Episode I of the Blob Wars Saga.
You must undertake the role of fearless Blob solider, Bob, as he infiltrates
various enemy installations and hideouts in an attempt to rescue as many
MIAs as possible.

%prep
%setup -q
%patch1
%patch2
%patch3 -p1
%patch4
%patch5

%build
%make_build VERSION=%version PREFIX=%_prefix USEPAK=1
# RELEASE=0

%install
%makeinstall DESTDIR=%buildroot PREFIX=%_prefix  USEPAK=1

# icons
mkdir -p %buildroot%_liconsdir
install -m 644 icons/blobwars-large.png %buildroot%_liconsdir/blobwars.png

# disabled because USEPAK=0 is broken
# fonts
#pushd %buildroot%_gamesdatadir/%name
#rm data/vera.ttf
#ln -s %_ttffontsdir/dejavu/DejaVuSans.ttf data/vera.ttf
#popd

# Install appdata
mkdir -p %{buildroot}%{_datadir}/appdata
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/appdata

%find_lang %name

%files -f %name.lang
%_gamesbindir/%name
%_gamesdatadir/%name
%_desktopdir/%name.desktop
%{_datadir}/appdata/*
%_iconsdir/hicolor/*/apps/%name.png
%doc doc/*

%changelog
* Sat Oct 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt2
- added rh and suse patches
- USEPAK=1 as build w/o pak seems to be broken

* Fri Jun 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- new version

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.04-alt4.qa3
- Fixed build with zlib 1.2.7

* Sun Nov 29 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.04-alt4.qa2
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for blobwars
  * update_menus for blobwars
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for blobwars

* Tue Sep 18 2007 Alexey Rusakov <ktirf@altlinux.org> 1.04-alt4
- fixed desktop file category (bug #12825)
- use license macro
- removed %%__ macros

* Sat Jul 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.04-alt3
- fixed building with GCC 4.
- DejaVu font file is now taken from fonts-ttf-dejavu package (still at
  the building time, however).

* Wed Mar 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.04-alt2
- revised dependencies.
- fixed linking with --as-needed.
- removed Debian menu stuff.

* Thu Apr 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.04-alt1
- New upstream release.

* Fri Apr 01 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.03-alt3
- Fixed menu category.
- Prepared the game for internationalization; bundle DejaVu font instead of Vera for this purpose.

* Tue Mar 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.03-alt2
- Use bzip2 instead of gzip.
- Fixed duplicate desktop entries.
- Added menu-file generation.

* Tue Mar 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.03-alt1
- Initial Sisyphus packaging.


%define _release 1

Name: blobwars
Version: 1.04
Release: alt4.qa2

Summary: Mission and Objective based 2D Platform Game
License: %gpl2plus
Group: Games/Arcade

Url: http://www.parallelrealities.co.uk/blobWars.php
Source: %name-%version-%_release.tar.bz2
Patch1: %name-1.04-alt-fix-as-needed-linking.patch
Patch2: %name-1.04-alt-fixes.patch
Patch3: %name-1.04-fix-gcc4-compile.patch
Patch4: %name-1.04-fix-fdo-categories.patch

BuildRequires: rpm-build-licenses

BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel zlib-devel
# TODO: The package should depend on fonts-ttf-dejavu in runtime and take
# the font from there. rpm-build-fonts contains %_ttffontsdir macro.
BuildRequires: rpm-build-fonts fonts-ttf-dejavu

%description
Blob Wars : Metal Blob Solid. This is Episode I of the Blob Wars Saga.
You must undertake the role of fearless Blob solider, Bob, as he infiltrates
various enemy installations and hideouts in an attempt to rescue as many
MIAs as possible.

%prep
%setup -q
%patch1
%patch2
%patch3
%patch4
%__subst 's/TTF_RenderText/TTF_RenderUTF8/' src/*
%__subst 's/vera\.ttf/font.ttf/' src/*
cp %_ttffontsdir/dejavu/DejaVuSans.ttf data/font.ttf

%build
%make_build VERSION=%version RELEASE=%_release PREFIX=%_prefix

%install
%makeinstall DESTDIR=%buildroot PREFIX=%buildroot%_prefix

# icons
mkdir -p %buildroot%_niconsdir %buildroot%_miconsdir %buildroot%_liconsdir
pushd %buildroot%_iconsdir
mv mini/*.* %buildroot%_miconsdir/
mv large/*.* %buildroot%_liconsdir/
mv *.* %buildroot%_niconsdir/
rmdir mini large
popd

%files
%_gamesbindir/%name
%dir %_gamesdatadir/parallelrealities
%_gamesdatadir/parallelrealities/%name.pak
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%doc doc/*

%changelog
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


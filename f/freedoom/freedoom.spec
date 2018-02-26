Name: freedoom
Version: 0.7
Release: alt1

Summary: Freedoom is a free data files for Doom II
License: BSD-like
Group: Games/Arcade
Url: http://www.nongnu.org/freedoom/
Source0: %name-iwad-%version.zip
#Source1: %name-iwad-%version.zip.sig
Source1: freedoom.desktop
Source2: freedoom.png

BuildArch: noarch

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Fri Mar 20 2009
BuildRequires: unzip

BuildRequires:  desktop-file-utils

%description
Freedoom is a project to create a complete Doom II-compatible
IWAD file which is Free Software.

The IWAD file is the file used by Doom which contains all the
game data (graphics, sound effects, music, etc.). While the
Doom source code is Free, you currently still need one of the
proprietary IWAD files from id in order to play Doom. Freedoom
aims to create a Free alternative. Combined with the GPL-licensed
Doom source code this will result in a complete Free Doom-based
game.

%prep
%setup -n %name-iwad-%version

%build
%install
mkdir -p %buildroot%_gamesdatadir/doom/
install -m640 -p doom2.wad %buildroot%_gamesdatadir/doom/

desktop-file-install --dir %buildroot/%_datadir/applications %SOURCE1

mkdir -p %buildroot/%_datadir/icons/hicolor/48x48/apps/
install -p -m 644 %SOURCE2 %buildroot/%_datadir/icons/hicolor/48x48/apps/

%files
%doc COPYING CREDITS ChangeLog NEWS README README.html
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/48x48/apps/*.png

%_gamesdatadir/doom/doom2.wad

%changelog
* Mon Jan 09 2012 Ilya Mashkin <oddity@altlinux.ru> 0.7-alt1
- 0.7
- add desktop file

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 0.6.4-alt1
- 0.6.3 -> 0.6.4

* Fri Mar 20 2009 Igor Zubkov <icesik@altlinux.org> 0.6.3-alt1
- 0.6.2 -> 0.6.3

* Thu Mar 27 2008 Igor Zubkov <icesik@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Sun Mar 16 2008 Igor Zubkov <icesik@altlinux.org> 0.6.1-alt1
- 0.6 -> 0.6.1

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.6-alt1
- 0.5 -> 0.6

* Wed Sep 27 2006 Igor Zubkov <icesik@altlinux.org> 0.5-alt1
- 0.4.1 -> 0.5

* Mon Mar 13 2006 Igor Zubkov <icesik@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.4-alt1
- 0.4

* Wed Nov 09 2005 Igor Zubkov <icesik@altlinux.ru> 0.3-alt1
- Initial build for Sisyphus

Name: AlephOne
Version: 1.0.1
Release: alt1

Summary: 3D first-person shooter game
License: %gpl2plus
Group: Games/Arcade
Url: http://marathon.sourceforge.net/

Packager: Artem Zolochevskiy <azol@altlinux.ru>

# http://downloads.sourceforge.net/marathon/AlephOne-20100118.tar.bz2
Source0: %name-%version.tar
Source1: %name.desktop
Source2: %name-48x48.png
Source3: alephone-wrapper.sh

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Jan 26 2010
BuildRequires: boost-devel gcc-c++ libGL-devel libSDL_image-devel libSDL_net-devel libSDL_ttf-devel libalsa-devel libmad-devel libpng-devel libsmpeg-devel libsndfile-devel libspeex-devel libvorbis-devel zziplib-devel
BuildRequires: desktop-file-utils

%description
Aleph One is an Open Source 3D first-person shooter game, based on the game
Marathon 2 by Bungie Software. It is set in a Sci-Fi universe dominated by
deviant computer AIs and features a well thought-out plot. Aleph One
supports, but doesn't require, OpenGL for rendering.

Aleph One requires additional data -- shape, sound, and map
information -- in order to run. The easiest way to get this is to go
to http://source.bungie.org/get/, and download one of the scenario zip
files there. Unzip it, and pass the resulting directory as an argument
to alephone. For example:

alephone "~/Marathon Infinity"

%prep
%setup

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir %SOURCE1
install -pD -m644 %SOURCE2 %buildroot%_liconsdir/%name.png
install -pD -m755 %SOURCE3 %buildroot%_gamesbindir/

%files
%doc AUTHORS INSTALL.Unix README docs/*.html examples
%dir %_gamesdatadir/%name
%dir %_gamesdatadir/%name/MML
%dir %_gamesdatadir/%name/Themes
%_gamesbindir/*
%_gamesdatadir/%name/Fonts
%_gamesdatadir/%name/MML/*.mml
%_gamesdatadir/%name/Themes/Default
%_liconsdir/%name.png
%_desktopdir/*
%_man6dir/*

%changelog
* Sat Mar 17 2012 Artem Zolochevskiy <azol@altlinux.ru> 1.0.1-alt1
- update to 1.0.1

* Sun Jul 25 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.23.2-alt1
- update to 0.23.2

* Tue Apr 06 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.23.1-alt1.1
- rebuild with new zziplib

* Thu Mar 11 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.23.1-alt1
- update to 0.23.1
- fix previous changelog entries

* Tue Jan 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.23-alt1
- update to 0.23
- remove ChangeLog COPYING* from package according to Docs Policy

* Fri Jan 08 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.22.1-alt1
- update to 0.22.1
- switch to use freedesktop menu
- show xmessage if data files not found
- spec changes:
  + use macro for License tag
  + fix URL
  + add Packager
  + update description, remove russian Summary and description
  + use one menu 48x48 icon
  + remove the dependence on AlephOne-core-data (users can use unimap zip files)
  + remove obsolete %%update_menus/%%clean_menus calls

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.12.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Dec 15 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.12.0-alt1
- Initial release for Sisyphus
- AlephOne-icons.tar.bz2 taken from Mandrake

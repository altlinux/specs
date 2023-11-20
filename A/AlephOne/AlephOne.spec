Name: AlephOne
Version: 1.0.2
%define uversion 20220115

Release: alt1.1

Summary: 3D first-person shooter game
License: %gpl2plus
Group: Games/Arcade
Url: https://alephone.lhowon.org
# Url git  https://github.com/Aleph-One-Marathon/alephone

# https://github.com/Aleph-One-Marathon/alephone/releases/download/release-20220115/AlephOne-20220115.tar.bz2

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source0: %name-%uversion.tar
Source1: %name.desktop
Source2: %name-48x48.png
Source3: alephone-wrapper.sh

#Patch0: %name-1.0.1-gcc8-fix.patch
Patch1: ax_boost_base-loongarch64.patch


BuildRequires(pre): rpm-build-licenses

BuildPreReq: libSDL2-devel libSDL2_image-devel libSDL2_net-devel  boost-program_options-devel
BuildPreReq: libsdl2_sound-devel libSDL2_ttf-devel boost-filesystem-devel


# Automatically added by buildreq on Sat Jul 16 2022
# optimized out: boost-devel boost-devel-headers glibc-kernheaders-generic glibc-kernheaders-x86 libSDL2-devel libglvnd-devel libgpg-error libogg-devel libsasl2-3 libstdc++-devel perl pkg-config python3 python3-base sh4 zlib-devel zziplib
BuildRequires: boost-filesystem-devel gcc-c++ libGLU-devel libSDL2_image-devel libSDL2_net-devel libSDL2_ttf-devel libalsa-devel
BuildRequires: libcurl-devel libmad-devel libminiupnpc-devel libpng-devel libsmpeg-devel libsndfile-devel libspeex-devel libspeexdsp-devel
BuildRequires: libvorbis-devel lua5.3 python3-dev zziplib-devel /usr/bin/python3

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
%setup -n %name-%uversion
#patch0 -p2
%patch1 -p1

%build
#add_optflags -fpermissive
#configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
#make_build

%autoreconf

%configure \
--enable-dependency-tracking

%make_build

%install
%makeinstall_std
#desktop-file-install --dir %buildroot%_desktopdir %SOURCE1
#install -pD -m644 %SOURCE2 %buildroot%_liconsdir/%name.png
#install -pD -m755 %SOURCE3 %buildroot%_gamesbindir/

%files
%doc AUTHORS COPYING INSTALL.Unix README docs/*.html examples
%_bindir/alephone
#%_datadir/AlephOne/Fonts
%_datadir/AlephOne/MML
%_datadir/AlephOne/Plugins
%_datadir/mime/packages/*.xml

%_iconsdir/hicolor/*/mimetypes/*.png

%_man6dir/*

#doc AUTHORS COPYING  INSTALL.Unix README docs/*.html examples
#dir %_gamesdatadir/%name
#dir %_gamesdatadir/%name/MML
#dir %_gamesdatadir/%name/Themes
#_gamesbindir/*
#_gamesdatadir/%name/Fonts
#_gamesdatadir/%name/MML/*.mml
#_gamesdatadir/%name/Themes/Default
#_liconsdir/%name.png
#_desktopdir/*
#_man6dir/*


%changelog
* Mon Nov 20 2023 Ivan A. Melnikov <iv@altlinux.org> 1.0.2-alt1.1
- NMU: fix FTBFS on loongarch64

* Sun Jul 17 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.2-alt1
- Update to Release 20220115 from github

* Mon Feb 11 2019 Pavel Moseev <mars@altlinux.org> 1.0.1-alt1.3
- no return statement in the non-void function fixed (according g++8)

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1.2
- fixed build - added BR libspeexdsp-devel

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt with libpng15

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

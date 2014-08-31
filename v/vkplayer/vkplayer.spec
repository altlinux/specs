Name: vkplayer
Version: 0.08.16
Release: alt5
Summary: VKPlayer Search music, load MyAudio and Recommendations playlists, save stream while"
Summary(ru_RU.UTF-8): Музыка из vk.com
License: GPL
Group: Sound
Url: http://forum.ubuntu.ru/index.php?topic=168217"
Packager: Konstantin Artyushkin <akv@altlinux.org>
Source: %name-%version.tar.gz
Patch: buildroot.patch
Patch1: phonondev.patch
Patch2: make.patch

#Requires:
BuildRequires: phonon-devel rpm-macros-qt4 gcc4.7-c++
#Conflicts:
#Obsoletes:
#Provides:

%description
VKPlayer Search music, load MyAudio and Recommendations playlists,
save stream while"
%description -l ru_RU.UTF-8
Музыка из vk.com

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%qmake_qt4
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/apps/%name.svg

%changelog
* Sun Aug 31 2014 Konstantin Artyushkin <akv@altlinux.org> 0.08.16-alt5
-  final commit for sisyphus 

* Fri Feb 28 2014 Konstantin Artyushkin <akv@altlinux.org> 0.08.16-alt4
- phonondev +=

* Sat Jan 25 2014 gBopHuk<gbophuk_alt@altlinux.org> 0.08.16-alt1.M70P.2
- This packeg was create with --no-sisyphus-chek parameter and can contains some mistakes

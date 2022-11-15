Name: flowblade
Version: 2.8.0.2
Release: alt1.1

Summary: non-linear video editor
Summary(ru_RU.utf8): Редактор нелинейного видео монтажа
License: GPL-3.0-or-later
Group: Video

Url: https://jliljebl.github.io/flowblade/

VCS: https://github.com/jliljebl/flowblade/
Source: %name-%version.tar
Patch1: %name-trunk-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): libappindicator-gtk3-gir-devel librsvg-devel
BuildRequires: intltool python3-module-chardet python3-module-setuptools

%add_python3_self_prov_path %buildroot%python3_sitelibdir/Flowblade

#Filtered because there is no blender package on i586 and armh architectures
%filter_from_requires /^python3(bpy)/d

%description
Flowblade is a multitrack non-linear video editor released under GPL3 
license. From beginners to masters, Flowblade helps make your vision
a reality of image and sound.

Flowblade supports all the media that in general can be accessed in
a Linux system when the FFMPEG library is working as the backend.

To use Blender projects in Flowblade you should install Blender.

%prep
%setup -q
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%_man1dir/%name.1*
%python3_sitelibdir/Flowblade
%python3_sitelibdir/flowblade*
%_datadir/metainfo/io.github.jliljebl.Flowblade.appdata.xml
%_datadir/applications/io.github.jliljebl.Flowblade.desktop
%dir %_datadir/icons/hicolor/128x128
%dir %_datadir/icons/hicolor/128x128/apps
%_datadir/icons/hicolor/128x128/apps/io.github.jliljebl.Flowblade.png
%_datadir/mime/packages/flowblade
%_datadir/mime/packages/io.github.jliljebl.Flowblade.xml

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.8.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sat Mar 27 2021 Andrey Sokolov <keremet@altlinux.ru> 2.8.0.2-alt1
- Updated to 2.8.0.2

* Sun Jan 17 2021 Andrey Sokolov <keremet@altlinux.ru> 2.6.0-alt3
- Remove unusable files which add dependency on Java

* Sat Oct 17 2020 Andrey Sokolov <keremet@altlinux.ru> 2.6.0-alt2
- Updated to v2.2-719-g56b8b6da.

* Sat Oct 10 2020 Andrey Sokolov <keremet@altlinux.ru> 2.6.0-alt1
- Initial build for Sisyphus

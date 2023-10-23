Name: flowblade
Version: 2.10.0.2
Release: alt2

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
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libayatana-indicator3-devel librsvg-devel
BuildRequires: python3-module-chardet

%py3_requires mlt7

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
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%_man1dir/%name.1.*
%python3_sitelibdir/Flowblade/
%python3_sitelibdir/flowblade-%version.dist-info/*
%_datadir/metainfo/io.github.jliljebl.Flowblade.appdata.xml
%_datadir/applications/io.github.jliljebl.Flowblade.desktop
%_datadir/icons/hicolor/128x128/apps/io.github.jliljebl.Flowblade.png
%_datadir/mime/packages/flowblade
%_datadir/mime/packages/io.github.jliljebl.Flowblade.xml

%changelog
* Mon Oct 23 2023 Anton Midyukov <antohami@altlinux.org> 2.10.0.2-alt2
- NMU:
  + migrating to PEP517-aware RPM macros
  + cleanup spec
  + add %%py3_requires mlt7 (Closes: 46788)

* Mon Jun 26 2023 Artyom Bystrov <arbars@altlinux.org> 2.10.0.2-alt1
- New version 2.10.0.2.

* Mon Jun 26 2023 Artyom Bystrov <arbars@altlinux.org> 2.8.0.2-alt1.2
- Rise from the archive!

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

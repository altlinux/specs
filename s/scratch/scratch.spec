Name: scratch

%define installdir %_datadir/scratch

Summary: A new programming language
Summary(ru.UTF-8): Программирование для детей на основе Logo

Group: Education
Version: 1.4.0.1
Release: alt4

License: Artistic License
Url: http://scratch.mit.edu/

Packager: Anton A. Vinogradov <arc@altlinux.org>

Source: %name.tar.gz
Source1: %name.png



Patch: 001-usr-bin-scratch.patch
Patch1: 002-locale-fix.patch
Patch2: 003-cameraplugin-dirty-rollback.patch
Patch3: 004-unicodeplugin-dirty-rollback.patch
Patch4: 005-fix-desktop-file.patch
Patch5: 006-usr-bin64-scratch.patch
Patch6: 007-fix-scrathplugin-build.patch

Requires: %name-image %name-plugins
Obsoletes: %name-bin

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: libpango-devel libv4l-devel

%description
Scratch is a new programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

Scratch is designed to help young people (ages 8 and up) develop 21st century
learning skills. As they create Scratch projects, young people learn important
mathematical and computational ideas, while also gaining a deeper understanding
of the process of design.

#Virtual package which provides a complete environment
%package full
Summary: Virtual package which provides a complete environment for %name
Group: Education
Requires: %name %name-image %name-media %name-plugins %name-projects

%description full
Virtual package which provides a complete environment for %name

%description full -l ru_RU.UTF-8
Виртуальный пакет устанавливающий все файлы для %name

#Scrath image
%package image
Summary: Image file of %name
Group: Education
Requires: %name-plugins %name
BuildArch: noarch
%description image
Image file of %name

%description image -l ru_RU.UTF-8
Файл образа %name

#Scrath help-en
%package help-en
Summary: English help files for %name
Group: Education
Requires: %name
BuildArch: noarch
%description help-en
English help files for %name

%description help-en -l ru_RU.UTF-8
Файлы справки для %name (Английский)

#Scrath Media
%package media
Summary: Media files for %name
Group: Education
Requires: %name-image
BuildArch: noarch
%description media
Media files for %name

%description media -l ru_RU.UTF-8
Медиафайлы для %name

#Scrath Projects
%package projects
Summary: Projects files for %name
Group: Education
Requires: %name
BuildArch: noarch
%description projects
Projects files for %name

%description projects -l ru_RU.UTF-8
Подборка готовых проектов для %name

#Scrath Plugins
%package plugins
Summary: Squeak plugins for %name
Group: Education
Requires: squeak-vm => 4.0.3
%description plugins
Squeak plugins for %name

%description plugins -l ru_RU.UTF-8
Squeak плагины для %name

%prep
%setup -q -n %name

%ifarch i586
%patch0 -p1
%endif

%ifarch x86_64
%patch5 -p1
%endif

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1

%build
pushd src/plugins/scratch
	sh build.sh
popd
pushd src/plugins/unicode
	sh unixBuild.sh
popd
pushd src/plugins/camera
	sh build.sh
popd

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/scratch
mkdir -p %buildroot%_libdir/squeak
mkdir -p %buildroot%_libdir/squeak/current

mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps
mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps
mkdir -p %buildroot%_datadir/mime/application

install -Dm644 src/plugins/scratch/ScratchPlugin %buildroot%_libdir/squeak/current/so.ScratchPlugin
install -Dm644 src/plugins/unicode/UnicodePlugin %buildroot%_libdir/squeak/current/so.UnicodePlugin
install -Dm644 src/plugins/camera/CameraPlugin %buildroot%_libdir/squeak/current/so.CameraPlugin

install -Dm644 Scratch.image %buildroot%installdir/Scratch.image
install -Dm644 src/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %SOURCE1 %buildroot%_pixmapsdir/%name.png
install -Dm644 src/icons/48x48/* %buildroot%_iconsdir/hicolor/48x48/apps/
install -Dm644 src/icons/128x128/* %buildroot%_iconsdir/hicolor/128x128/apps/

install -Dm644 src/%name.xml %buildroot%_datadir/mime/application/
install -Dm755 src/%name %buildroot%_bindir/%name

install -Dm644 license.txt %buildroot%installdir/license.txt
install -Dm644 Scratch.ini %buildroot%installdir/Scratch.ini
install -Dm644 README.txt %buildroot%installdir/README.txt

mkdir -p %buildroot%installdir

mv Help %buildroot%installdir/
mv locale %buildroot%installdir/
mv Media %buildroot%installdir/
mv Projects %buildroot%installdir/
#%_bindir/scratch is a shell script
%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

#virtual package which provides a complete environment for Scratch
%files full

#Scrath image
%files image
%installdir/Scratch.image
%installdir/locale
%installdir/README.txt
%installdir/Scratch.ini
%installdir/license.txt
%_iconsdir/hicolor/48x48/apps/*
%_iconsdir/hicolor/128x128/apps/*
%_datadir/mime/application/*
#Scrath image
%files help-en
%installdir/Help
#Scrath Media
%files media
%installdir/Media
#Scrath Projects
%files projects
%installdir/Projects
#Scrath Plugins
%files plugins
%_libdir/squeak/current/*

%changelog
* Tue Aug 16 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.0.1-alt4
- Remove all .svn subdirectories from source
- Cleanup patches

* Mon Aug 15 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.0.1-alt3
- Enable patch to fix Cyrillic letter show in GUI (closes: #26051)

* Thu May 06 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4.0.1-alt2
- spec cleanup

* Tue May 04 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4.0.1-alt1
- totally reworked
- add webcam support (/dev/video0 only)
- some ru.po fix

* Sat Jan 30 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.7
- spec cleanup

* Fri Jan 29 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.6
- some ru.po fix from edmdv

* Thu Jan 28 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.5
- yet another build

* Thu Jan 28 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.4
- switch arch to "noarch"
- spec cleanup

* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.3
- initial build for ALT Linux


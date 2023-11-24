%define _unpackaged_files_terminate_build 1
%define electron_version 23

Name: scratch-desktop
Version: 3.30.5
Release: alt1

Group: Education
License: BSD-3-Clause
URL: https://scratch.mit.edu/
VCS: https://github.com/scratchfoundation/scratch-desktop

%define scratch_installdir %_datadir/%name

Summary: Scratch-desktop is a set of React components that comprise the interface for creating and running Scratch 3.0 projects. Scratch-desktop is a standalone Electron based desktop application.
Summary(ru.UTF-8): Scratch-desktop - это набор компонентов React, которые составляют интерфейс для создания и запуска проектов Scratch 3.0. Scratch-desktop - отдельное настольное приложение на базе Electron.

Source: %name-%version.tar
Source1: node_modules.tar
Source2: static.tar
Source3: scratch-desktop.desktop
Source4: scratch-microbit.hex.zip

Patch1: 0001-Fix-package-build.patch
Patch2: 0002-Fix-launch-application.patch
Patch3: 0003-alt-use-static-microbit.patch
Patch4: 0004-linux-build.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: npm
BuildRequires: node
BuildRequires: electron%electron_version
BuildRequires: node-asar
BuildRequires: node-gyp
BuildRequires: unzip

Requires: electron%electron_version

%description
Scratch is a new programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

Scratch is designed to help young people (ages 8 and up) develop 21st century
learning skills. As they create Scratch projects, young people learn important
mathematical and computational ideas, while also gaining a deeper understanding
of the process of design.

%description -l ru_RU.UTF-8
Scratch - это новый язык программирования, который позволяет легко создавать
свои собственные интерактивные истории, анимацию, игры, музыку и искусство
- и делиться своими творениями в Интернете.

Scratch разработан, чтобы помочь молодым людям (в возрасте 8 лет и старше)
развить навыки обучения 21-го века. При создании Scratch-проектов молодые люди
изучают важные математические и вычислительные идеи, а также получают более
глубокое понимание процесса проектирования.

%prep
%setup -a1 -a2
mkdir -p node_modules/scratch-gui/static/microbit
unzip %SOURCE4 -d node_modules/scratch-gui/static/microbit
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p1
%define electronvers %(rpm -q --qf '%%{VERSION}' electron%electron_version)
sed -i -e "s:@electronVersion@:%electronvers:g" webpack.makeConfig.js

%build
pushd node_modules/scratch-gui
node scripts/prepublish.mjs
popd
export NODE_OPTIONS=--openssl-legacy-provider
#npm run dist
npm run compile

cat <<EOF >%name
#!/bin/sh
electron%electron_version %scratch_installdir/app.asar "\$@"
EOF

mkdir -p asar_resources/node_modules
mkdir -p asar_resources/static/assets/
mkdir -p asar_resources/static/blocks-media/

cp -a dist/main/* asar_resources/
cp -a dist/renderer/* asar_resources/
cp -a node_modules/buffer-from asar_resources/node_modules
cp -a node_modules/source-map asar_resources/node_modules
cp -a node_modules/source-map-support asar_resources/node_modules
cp -a package.json asar_resources/

asar pack asar_resources/ app.asar

%install
install -D -m644 src/icon/ScratchDesktop.png %buildroot%_iconsdir/hicolor/1024x1024/apps/ScratchDesktop.png
install -D -m644 src/icon/ScratchDesktop.svg %buildroot%_iconsdir/hicolor/scalable/apps/ScratchDesktop.svg
install -D -m755 %name %buildroot%_bindir/%name
install -D -m755 app.asar %buildroot%scratch_installdir/app.asar
install -D -m644 %SOURCE3 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_libdir/electron4/resources/static/
cp -a static/* %buildroot%_libdir/electron4/resources/static/

%files
%doc LICENSE TRADEMARK README.md
%scratch_installdir/
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_libdir/electron4/resources/static
%exclude %dir %_libdir/electron4
%exclude %dir %_libdir/electron4/resources

%changelog
* Fri Nov 24 2023 Andrey Cherepanov <cas@altlinux.org> 3.30.5-alt1
- New version.
- Build only for x86_64 and aarch64.

* Fri Sep 02 2022 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt3.1
- NMU: added node-gyp to build requirements

* Mon Sep 09 2019 Pavel Moseev <mars@altlinux.org> 3.4.0-alt3
- change path to media files

* Fri Sep 06 2019 Pavel Moseev <mars@altlinux.org> 3.4.0-alt2
- fix location of additional media files

* Thu Aug 01 2019 Pavel Moseev <mars@altlinux.org> 3.4.0-alt1
- initial release for ALT Linux

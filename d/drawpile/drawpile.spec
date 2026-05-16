Name: drawpile
Version: 2.3.0
Release: alt2

Summary: A collaborative drawing program
Summary(ru_RU.UTF-8): Программа для совместного рисования
License: GPL-3.0-only
Group: Graphics

Url: https://%name.net
Vcs: https://github.com/%name/Drawpile

# Source-url: https://github.com/%name/Drawpile/archive/%version/Drawpile-%version.tar.gz
Source0: Drawpile-%version.tar
# cargo vendor
Source1: vendor.tar
Source2: config

Patch0: %name-2.2.2-alt-desktop.patch
Patch1: qt6_build_fix.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: git-core
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: libsodium-devel
BuildRequires: libswscale-devel
BuildRequires: libwebp-devel
BuildRequires: libzip-devel
BuildRequires: libzstd-devel
BuildRequires: qt6-sql-interbase
BuildRequires: qt6-sql-mysql
BuildRequires: qt6-sql-odbc
BuildRequires: qt6-sql-postgresql
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-translations
BuildRequires: qt6-websockets-devel
BuildRequires: rust-cargo
BuildRequires: zlib-devel

%description
Drawpile is a Free/Libre networked drawing program that allows multiple people
to sketch on the same image simultaneously. It supports the OpenRaster image
file format and thus works well with applications such as MyPaint,
rita and GIMP.

%description -l ru_RU.UTF-8
Drawpile - бесплатная сетевая программа для рисования, которая позволяет
нескольким людям одновременно рисовать на одном и том же холсте.
Drawpile поддерживает формат файла изображения OpenRaster(ora) и поэтому хорошо
работает с такими приложениями, как MyPaint, Krita и GIMP.

%prep
%setup -n Drawpile-%version
tar xf %SOURCE1
%__mkdir_p cargo
%__cp %SOURCE2 cargo
%autopatch -p1

%build
export LANG=C.UTF-8
export CARGO_HOME=${PWD}/cargo
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DTOOLS:BOOL=ON \
	-Wno-dev \
	%nil
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog README.md
%_bindir/dprectool
%_bindir/%{name}*
%_desktopdir/net.%name.%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/hicolor/*/mimetypes/*
%_datadir/metainfo/net.%name.%name.appdata.xml
%_datadir/mime/application/vnd.%name.canvas.xml
%_datadir/mime/application/vnd.%name.recording.xml
%_datadir/mime/text/vnd.%name.recording.xml

%changelog
* Sun May 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt2
- fixed FTBFS

* Sat Nov 22 2025 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Thu Oct 09 2025 Nazarov Denis <nenderus@altlinux.org> 2.2.2-alt1
- New version 2.2.2.

* Tue Aug 30 2022 Evgeny Chuck <koi@altlinux.org> 2.1.20-alt2
- Fixed category in desktop file

* Tue Feb 01 2022 Evgeny Chuck <koi@altlinux.org> 2.1.20-alt1
- initial build for ALT Linux Sisyphus

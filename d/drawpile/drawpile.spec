%define _unpackaged_files_terminate_build 1

Name: drawpile
Version: 2.3.1
Release: alt1

Summary: A collaborative drawing program
Summary(ru_RU.UTF-8): Программа для совместного рисования
License: GPL-3.0-only
Group: Graphics

Url: https://%name.net
Vcs: https://github.com/%name/Drawpile

Source: %name-%version.tar
Source1: vendor.tar

Patch: %name-2.2.2-alt-desktop.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-rust
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
BuildRequires: libzstd-devel-static

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
%setup -a1
%rust_prep
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
%_datadir/mime/application/vnd.%name.*.xml
%_datadir/mime/text/vnd.%name.recording.xml

%changelog
* Thu Oct 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.1-alt1
- 2.3.0 -> 2.3.1

* Wed Jul 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt3
- fixed FTBFS

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

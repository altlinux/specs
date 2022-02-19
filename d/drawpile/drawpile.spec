Name: drawpile
Version: 2.1.20
Release: alt1

Summary: A collaborative drawing program
Summary(ru_RU.UTF-8): Программа для совместного рисования
License: GPL-3.0-only
Group: Graphics
Url: https://drawpile.net

# Source-url: https://github.com/drawpile/Drawpile/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: extra-cmake-modules
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kf5-karchive-devel
BuildRequires: libminiupnpc-devel
BuildRequires: kf5-kdnssd-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: libsodium-devel 
BuildRequires: libmicrohttpd-devel
BuildRequires: libgif-devel
BuildRequires: libvpx-devel

BuildRequires(pre): rpm-macros-cmake

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
%setup

%build
%cmake -DTOOLS=on
%cmake_build

%install
%cmake_install

%files
%_defaultdocdir/%name
%_bindir/drawpile*
%_bindir/dprectool
%_desktopdir/net.drawpile.drawpile.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/drawpile*
%_iconsdir/hicolor/*/mimetypes/application*
%_man1dir/%name-srv.1.*
%_datadir/metainfo/net.drawpile.drawpile.appdata.xml
%_datadir/mime/packages/x-drawpile.xml

%changelog
* Tue Feb 01 2022 Evgeny Chuck <koi@altlinux.org> 2.1.20-alt1
- initial build for ALT Linux Sisyphus

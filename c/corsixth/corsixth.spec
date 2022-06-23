Name: corsixth
Version: 0.65.1
Release: alt1

Summary: Open source clone of Theme Hospital
Summary(ru_RU.UTF-8): Клон Theme Hospital с открытым исходным кодом
License: MIT
Group: Games/Strategy
Url: https://github.com/CorsixTH/CorsixTH

Requires: TiMidity++
Requires: lua5.3-module-luafilesystem
Requires: lua5.3-module-lpeg

# Source-url: https://github.com/CorsixTH/CorsixTH/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libluajit-devel
BuildRequires: liblua5.3-devel
BuildRequires: libfreetype-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libswresample-devel
BuildRequires: libavformat-devel
BuildRequires: libavcodec-devel
BuildRequires: libswscale-devel

BuildRequires(pre): rpm-macros-cmake

%description
Re-implementation of the 1997 Bullfrog simulator Theme Hospital. In addition
to faithfully recreating the original, CorsixTH adds support for modern
operating systems (Windows, macOS, Linux, and BSD), high resolution, and more.

%description -l ru_RU.UTF-8
Повторная реализация симулятора Bullfrog 1997 года Theme Hospital.
Помимо точного воссоздания оригинала, CorsixTH добавляет поддержку
современных операционных систем (Windows, macOS, Linux и BSD),
высокое разрешение и многое другое.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md changelog.txt CONTRIBUTING.txt README.txt
%_bindir/corsix-th
%_desktopdir/*.desktop
%_datadir/corsix-th
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/scalable/apps/*.svg
%_man6dir/corsix-th.6.*

%changelog
* Thu Jun 23 2022 Evgeny Chuck <koi@altlinux.org> 0.65.1-alt1
- initial build for ALT Linux Sisyphus

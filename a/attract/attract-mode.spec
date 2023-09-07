%define optflags_lto %nil

Name: attract
Version: 2.7.0
Release: alt3

Summary: Arcade-like front-end for emulators
Summary(ru_RU.UTF-8): Оболочка в стиле аркадных автоматов для эмуляторов

License: GPLv2+
Group: Games/Arcade
Url: http://attractmode.org/

Source: %name-%version.tar

BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: libxcb
BuildRequires: libGLU-devel
BuildRequires: libSFML-devel
BuildRequires: libXinerama-devel
BuildRequires: libarchive-devel
BuildRequires: libavformat-devel
BuildRequires: libswresample-devel
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libjpeg-devel
BuildRequires: libopenal-devel
BuildRequires: libswscale-devel
BuildRequires: zlib-devel
BuildRequires: libXrandr-devel
BuildRequires: ImageMagick-tools

%description
Attract-Mode is a graphical frontend for command line emulators such as MAME,
MESS and Nestopia. It hides the underlying operating system and is intended to be
controlled with a joystick, gamepad or spin dial, making it ideal for use in arcade cabinets.
Attract-Mode is open source and runs on Linux, OS X and Windows-based systems.

%description -l ru_RU.UTF-8
Attract Mode - графическая оболочка для эмуляторов типа MAME, MESS, или Nestopia.
Скрывая привычный интерфейс операционной системы, оболочка расчитана под управление с помощью
геймпада или аркадного стика, что делает её идеальной для использования в аркадных автоматах.
Attract Mode является проектом с открытым исходным кодом, и может работать на Linux,
Mac OS X и Windows.

%prep
%setup -n %name-%version

%build
%make_build OPTIMISE="%optflags" prefix=%_prefix

%install
%makeinstall_std prefix=%_prefix

# install menu icons
for N in 16 32 48 64 128;
do
convert util/linux/attract-mode.png -scale ${N}x${N} $N.xpm;
install -D -m 0644 $N.xpm %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.xpm
done

install -Dm644 util/linux/attract-mode.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml
install -Dm644 util/linux/attract-mode.desktop         %buildroot%_desktopdir/%name.desktop


%files
%dir %_datadir/attract
%doc License.txt Readme.md Layouts.md
%_bindir/%name
%_datadir/%name/*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.xpm

%changelog
* Thu Sep  7 2023 Artyom Bystrov <arbars@altlinux.org> 2.7.0-alt3
- Change libavresample-devel to libswresample-devel (preparing for ffmpeg6.0)

* Tue Jul  4 2023 Artyom Bystrov <arbars@altlinux.org> 2.7.0-alt2
- Fix content installation (layouts and languages)

* Tue Jun 13 2023 Artyom Bystrov <arbars@altlinux.org> 2.7.0-alt1
- New version

* Fri Sep 16 2022 Artyom Bystrov <arbars@altlinux.org> 2.6.2-alt2
- Fixing desktop icons

* Mon May 2 2022 Artyom Bystrov <arbars@altlinux.org> 2.6.2-alt1
- Update to latest state of upstream
- Fixed build proccess on GCC11

* Sun Oct 10 2021 Artyom Bystrov <arbars@altlinux.org> 2.6.1-alt2
- Update to latest state of upstream
- walk-around build on Sisyphus (yes, it's creepy, but it's works)

* Mon Jan 20 2020 Artyom Bystrov <arbars@altlinux.org> 2.6.1-alt1
- Update version to 2.6.1

* Tue Nov 26 2019 Artyom Bystrov <arbars@altlinux.org> 2.5.1-alt1
- initial build for ALT Sisyphus

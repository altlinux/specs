%define optflags_lto %nil

Name: attractplus
Version: 3.0.5
Release: alt2

Summary: Arcade-like front-end for emulators
Summary(ru_RU.UTF-8): Оболочка в стиле аркадных автоматов для эмуляторов

License: GPLv2+
Group: Games/Arcade
Url: http://attractmode.org/

Source: %name-%version.tar

BuildRequires: fontconfig-devel
BuildRequires: gcc-c++ cmake
BuildRequires: libxcb
BuildRequires: libGLU-devel libbrotli-devel 
BuildRequires: libSFML-devel libcurl-gnutls-compat
BuildRequires: libXinerama-devel
BuildRequires: libarchive-devel
BuildRequires: libavformat-devel
BuildRequires: libswresample-devel
BuildRequires: libcurl-devel libudev-devel
BuildRequires: libexpat-devel libvorbis-devel libflac-devel
BuildRequires: libjpeg-devel libpng-devel libXcursor-devel
BuildRequires: libopenal-devel
BuildRequires: libswscale-devel
BuildRequires: bzlib-devel libpcre2-devel
BuildRequires: libXrandr-devel
BuildRequires: ImageMagick-tools
BuildRequires: bzip2-devel libpcre-devel
Conflicts: attract

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
%_datadir/attract/*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.xpm

%changelog
* Fri Sep  8 2023 Artyom Bystrov <arbars@altlinux.org> 3.0.5-alt2
- Make buildable on P10

* Thu Sep  7 2023 Artyom Bystrov <arbars@altlinux.org> 3.0.5-alt1
- New version

* Tue Jul  4 2023 Artyom Bystrov <arbars@altlinux.org> 3.0.3-alt1
- New version

* Tue Jun 13 2023 Artyom Bystrov <arbars@altlinux.org> 3.0.2-alt1
- New version

* Tue Oct 25 2022 Artyom Bystrov <arbars@altlinux.org> 2.6.2-alt1
- initial build for ALT Sisyphus

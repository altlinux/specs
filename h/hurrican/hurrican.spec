Name: hurrican
Version: 1.0.9.2
Release: alt5

Summary: Turrican freeware clone
Summary(ru_RU.UTF-8): Бесплатный клон Turrican

License: freeware
Group: Games/Arcade
Url: https://github.com/thrimbor/Hurrican/archive/%version.tar.gz

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name.png
Patch: hurrican-1.0.9.2-CMakelists-3rdparty-glm.patch

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: python-base python-modules python3 python3-base
BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: gcc-c++ bc
BuildRequires: libstdc++-devel-static
BuildRequires: libglm-devel
BuildRequires: libepoxy-devel
BuildRequires: libSDL-devel
BuildRequires: libSDL_image-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libmodplug-devel
BuildRequires: libGLES-devel

%description
Hurrican is a freeware jump and shoot game created by Poke53280
that is based on the Turrican game series.
Blast your way through nine large action-packed levels
filled with different enemies and powerups.

%description -l ru_RU.UTF-8
Hurrican - бесплатный экшн-платформер, созданный Poke53280,
основанный на идеях серии игр Turrican.
Прочищайте себе путь к выходу через девять крупных,
упакованных экшеном и забитых врагами и бонусами уровней.

%prep
%setup -n %name-%version
rm -r ./Hurrican/data/textures/pvr
%patch0 -p1
%ifarch %e2k
# because of "multiple definition of" errors at linking
%define lcc_fix() \
  sed -i "1i #define preferred_separator preferred_separator_$(echo %1 | tr /- __)" Hurrican/src/%1.cpp
%lcc_fix Console
%lcc_fix Texts
%lcc_fix SDLPort/texture
%lcc_fix SDLPort/SDL_port
%lcc_fix Tileengine
%lcc_fix DX8Sound
%lcc_fix DX8Texture
%lcc_fix Main
%endif

%build
%set_verify_elf_method no
%cmake_insource ./Hurrican

make TARGET=linux_GL2

%install
install -Dpm0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dm0644 %SOURCE2 %buildroot%_liconsdir/%name.png
mkdir -p %buildroot%_datadir/%name/data
mkdir -p %buildroot%_datadir/%name/lang
install -Dm0755 %name %buildroot%_bindir/%name
install -d %buildroot%_datadir/%name/data
cp -R Hurrican/data/* %buildroot%_datadir/%name/data/
install -d %buildroot%_datadir/%name/lang
cp -R Hurrican/lang/*.lng %buildroot%_datadir/%name/lang/

%files
%doc *.md
%_bindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/data
%dir %_datadir/%name/lang
%_datadir/%name/data/*
%_datadir/%name/lang/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Wed Oct 27 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0.9.2-alt5
- Fixed build for Elbrus

* Fri Mar 27 2020 Artyom Bystrov <arbars@altlinux.org> 1.0.9.2-alt4
- Fix post-install unowned files

* Fri Mar 27 2020 Artyom Bystrov <arbars@altlinux.org> 1.0.9.2-alt3
- Fixup build for other architectures (ix86, aarch64)

* Thu Mar 26 2020 Artyom Bystrov <arbars@altlinux.org> 1.0.9.2-alt2
- add patch for removing 3rdparty libglm deps
- minor spec cleanup

* Sun Sep 08 2019 Artyom Bystrov <arbars@altlinux.org> 1.0.9.2-alt1
- initial build for ALT Sisyphus

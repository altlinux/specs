%set_gcc_version 13
Name:     kronos
Version:  2.6.2
Release:  alt1

Summary:  Sega Saturn Emulator
License:  GPL2
Group:    Emulators
Url:      https://github.com/FCare/Kronos

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc13-c++ libSDL2_mixer-devel libSDL2-devel libpng-devel zlib-devel libGLEW-devel doxygen libfreeglut-devel qt5-base-devel qt5-multimedia-devel

%description
Yet Another Buggy And Uncomplete Saturn Emulator

%prep
%setup
export CC=%__cc
export CXX=%__cxx

%build
cd yabause
%cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE='Release' \
      -DYAB_USE_QT5=ON
%cmake_build

%install
cd yabause
%cmake_install

%files

%doc README.md yabause/COPYING yabause/README
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%_pixmapsdir/%name.png

%changelog
* Tue Nov  5 2024 Artyom Bystrov <arbars@altlinux.org> 2.6.2-alt1
- Update to new version

* Fri Feb 17 2023 Artyom Bystrov <arbars@altlinux.org> 2.5.0-alt1
- Update to new version

* Thu Dec 08 2022 Artyom Bystrov <arbars@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus

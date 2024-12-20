Name:    sdl2-gamepad-mapper
Version: 0.0.9
Release: alt1.git2c7a017

Summary: GUI application to map a generic controller to the SDL2 GameController spec and generate an SDL2 mapping string
License: GPLv3
Group:   Games/Other
Url:     https://gitlab.com/ryochan7/sdl2-gamepad-mapper

Source: %name-%version.tar

BuildRequires(pre): cmake rpm-build-cmake rpm-build-qml6
BuildRequires: gcc-c++ libSDL2-devel libevdev-devel qt6-declarative-devel
Requires: libqt6-qmlworkerscript libqt6-quickdialogs2 libqt6-quickcontrols2fusion libqt6-quicklayouts libqt6-quickcontrols2basic

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

install -Dpm0644 sdl2-gamepad-mapper.desktop %buildroot%_desktopdir/%name.desktop

install -Dm0644 sdl2-gamepad-mapper.png %buildroot%_liconsdir/%name.png

%files

%doc *.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Thu Dec 19 2024 Artyom Bystrov <arbars@altlinux.org> 0.0.9-alt1.git2c7a017
- Initial build
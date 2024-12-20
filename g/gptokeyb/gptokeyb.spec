Name:    gptokeyb
Version: 0.2.1
Release: alt1.git2c7a017

Summary: Gamepad to Keyboard/mouse/xbox360(gamepad) emulator
License: GPLv2
Group:   Games/Other
Url:     https://github.com/PortsMaster/gptokeyb

Source: %name-%version.tar

BuildRequires(pre): cmake rpm-build-cmake
BuildRequires: gcc-c++ libSDL2-devel libevdev-devel

%description
gptokeyb provides a kill switch for an application and mapping of gamepad buttons to keys and/or mouse. It also provides an xbox360-compatible controller mode.

%prep
%setup

%build
%cmake
%cmake_build

%install
install -Dm0755 ./%_cmake__builddir/gptokeyb %buildroot%_bindir/%name
mkdir -p %buildroot%_sysconfdir/%name
cp configs/*.gptk %buildroot%_sysconfdir/%name

%files
%doc *.md
%_bindir/%name
%_sysconfdir/%name/*

%changelog
* Thu Dec 19 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt1.git2c7a017
- Initial build
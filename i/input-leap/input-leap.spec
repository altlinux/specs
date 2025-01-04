%define nameL io.github.input_leap.InputLeap

Name: input-leap
Version: 3.0.2
Release: alt1

Summary: Open-source KVM software
Summary(ru_RU.UTF-8): Программное обеспечение KVM с открытым исходным кодом

License: GPL-2.0-only BSD-3-Clause MIT
Group: Networking/Other

Url: https://github.com/input-leap/input-leap
Vcs: https://github.com/input-leap/input-leap

Source0: %name-%version.tar
Source1: gtest.tar
Source2: gulrak-filesystem.tar

BuildRequires(Pre): rpm-macros-cmake rpm-build-cmake
BuildRequires: cmake clang libstdc++-devel qt6-base-devel
BuildRequires: libavahi-devel libXrandr-devel libXi-devel
BuildRequires: libXinerama-devel libXtst-devel libSM-devel 
BuildRequires: libICE-devel libXdmcp-devel qt6-tools-devel
BuildRequires: libuuid-devel llvm-devel ctest

Provides: inputleap = %EVR

%description
Input Leap is software that mimics the functionality of a KVM switch,
which historically would allow you to use a single keyboard and mouse
to control multiple computers by physically turning a dial on the box
to switch the machine you're controlling at any given moment. Input 
Leap does this in software, allowing you to tell it which machine to 
control by moving your mouse to the edge of the screen, or by using a
keypress to switch focus to a different system.

%description -l ru_RU.UTF8
Input Leap — это программное обеспечение, которое имитирует функциональность
переключателя KVM, который исторически позволял вам использовать одну 
клавиатуру и мышь для управления несколькими компьютерами, физически 
поворачивая диск на коробке, чтобы переключать машину, которой вы управляете 
в любой момент. Input Leap делает это программно, позволяя вам сообщать ему, 
какой машиной управлять, перемещая мышь к краю экрана или используя
нажатие клавиши для переключения фокуса на другую систему.

%prep
%setup
tar -xf %SOURCE1 -C ext/
tar -xf %SOURCE2 -C ext/

%build
export CC=clang
export CXX=clang++

%cmake
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%_bindir/*
%_datadir/applications/%nameL.desktop
%_iconsdir/hicolor/scalable/apps/%nameL.svg
%_mandir/man?/*
%_datadir/metainfo/%nameL.appdata.xml
%doc *.md 

%changelog
* Sat Jan 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus.

%define _unpackaged_files_terminate_build 1

Name: gamecontrollerdb
Version: 2026.01.13
Release: alt1.16ac3e5

Summary: Controller Mappings
License: Zlib
Group: Development/Databases
URL: https://github.com/mdqinc/SDL_GameControllerDB
Vcs: https://github.com/mdqinc/SDL_GameControllerDB.git
BuildArch: noarch

Source0: %name-%version.tar

%description
A community sourced database of game controller mappings to be used with SDL2
and SDL3 Game Controller functionality.

%prep
%setup

%install
mkdir -pv %buildroot%_datadir/SDL_GameControllerDB
cp -r %_builddir/gamecontrollerdb-%version/* %buildroot%_datadir/SDL_GameControllerDB

%files
%doc README.md LICENSE
%_datadir/SDL_GameControllerDB

%changelog
* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2026.01.13-alt1.16ac3e5
- Initial build.

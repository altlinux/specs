%define git_commit 2fb55450610a4d10479a1eed1408f905d79318e3
%define git_rev 7859
%define sover 0.10

Name: mgba
Version: %sover.2
Release: alt2.1

Summary: Game Boy Advance emulator
License: MPL-2.0
Group: Emulators

Url: https://%name.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %arm

# https://github.com/%name-emu/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildPreReq: libpostproc-devel
BuildPreReq: libzstd-devel

BuildRequires: cmake
BuildRequires: libSDL2-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libedit-devel
BuildRequires: libelf-devel
BuildRequires: libepoxy-devel
BuildRequires: libminizip-devel
BuildRequires: libpng-devel
BuildRequires: libsqlite3-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libzip-devel
BuildRequires: libzip-utils
BuildRequires: lua-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel

%description
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and more accurate than many existing Game Boy Advance emulators, as well as adding features that other emulators lack. It also supports Game Boy and Game Boy Color games.

%package cli
Summary: Game Boy Advance emulator (CLI version)
Group: Emulators

%description cli
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and more accurate than many existing Game Boy Advance emulators, as well as adding features that other emulators lack. It also supports Game Boy and Game Boy Color games.

This package provides SDL2-based CLI version of mGBA.

%package -n lib%name%sover
Summary: Shared library of mGBA
Group: System/Libraries

%description -n lib%name%sover
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and more accurate than many existing Game Boy Advance emulators, as well as adding features that other emulators lack. It also supports Game Boy and Game Boy Color games.

This package provides shared library of mGBA.

%package -n lib%name-devel
Summary: Development files for library of mGBA
Group: Development/C

%description -n lib%name-devel
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and more accurate than many existing Game Boy Advance emulators, as well as adding features that other emulators lack. It also supports Game Boy and Game Boy Color games.

This package provides development files for library of mGBA.

%prep
%setup

%build
# Generate version strings
sed -i -e 's/${GIT_COMMIT}/%git_commit/' src/core/version.c.in
sed -i -e 's/${GIT_COMMIT_SHORT}/%(c=%{git_commit}; echo ${c:0:8})/' src/core/version.c.in
sed -i -e 's/${GIT_BRANCH}/%version/' src/core/version.c.in
sed -i -e 's/${GIT_REV}/%git_rev/' src/core/version.c.in

%add_optflags -Wno-error=return-type
%cmake -Wno-dev
%cmake_build

%install
%cmake_install

%files
%_bindir/%name-qt
%_datadir/%name
%_iconsdir/hicolor/*/apps/io.mgba.mGBA.png
%_desktopdir/io.mgba.mGBA.desktop
%_defaultdocdir/mGBA
%_man6dir/%name-qt.6*

%files cli
%_bindir/%name
%_man6dir/%name.6*

%files  -n lib%name%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_includedir/%name-util
%_libdir/lib%name.so

%changelog
* Sun Sep 10 2023 Nazarov Denis <nenderus@altlinux.org> 0.10.2-alt2.1
- Fix FTBFS

* Sat Sep 02 2023 Nazarov Denis <nenderus@altlinux.org> 0.10.2-alt2
- Fix version strings

* Sat Sep 02 2023 Nazarov Denis <nenderus@altlinux.org> 0.10.2-alt1
- Initial build for ALT Linux

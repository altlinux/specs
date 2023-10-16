%define _unpackaged_files_terminate_build 1

Name: pioneerspacesim
Version: 20230203
Release: alt2

Summary: A game of lonely space adventure
License: GPLv3 and BSD and MIT and Apache-2.0 and ALT-Public-Domain and CC-BY-SA-3.0 and Bitstream-Vera and OFL-1.1
Group: Games/Other
Url: https://pioneerspacesim.net/
Vcs: https://github.com/pioneerspacesim/pioneer

# Apparently, the upstream developers do not care about 32-bit systems.  For
# instance, the src/lua/LuaPushPull.h header is not aware that the size_t type
# could potentially be equivalent to an unsigned int.
# There is no point for us to invest efforts in 32-bit systems either.
ExcludeArch: armh i586

Source: %name-%version.tar

Patch1: suse-use-system-fmt.patch
Patch2: alt-add-return-value.patch
Patch3: alt-fix-fmt-wont-format-enum.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(assimp) >= 5.0
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(vorbis)

Requires: %name-data = %EVR

%description
Pioneer is a space adventure game set in the Milky Way galaxy at the turn of
the 31st century.

The game is open-ended, and you are free to explore the millions of star
systems in the game. You can land on planets, slingshot past gas giants, and
burn yourself to a crisp flying between binary star systems. You can try your
hand at piracy, make your fortune trading between systems, or do missions for
the various factions fighting for power, freedom or self-determination.

%package data
Summary: Data files for %name
Group: Games/Other
BuildArch: noarch

%description data
Pioneer is a space adventure game set in the Milky Way galaxy at the turn of
the 31st century.

This package contains models, scripts and other data for the game.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

#fix the version, otherwise it will be set to the build date
#also, instead of the commit hash, write the alt release version
sed -i "/^string(TIMESTAMP PROJECT_VERSION/c\set(PROJECT_VERSION %version)\nset(PROJECT_VERSION_GIT %release)" CMakeLists.txt

%build
%cmake \
    -DUSE_SYSTEM_LIBGLEW=ON \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DPIONEER_DATA_DIR=%_datadir/%name \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

# precompile model files - game launch much faster
%cmake_build --target build-data

%install
%cmake_install

%check
%_cmake__builddir/unittest

%files
%_bindir/*
%_desktopdir/*.desktop
%_datadir/appdata/*.xml

%files data
%doc AUTHORS.txt Changelog.txt Modelviewer.txt Quickstart.txt README.md

# custom licenses
%doc licenses/Image\ Use\ Policy\ -\ NASA\ Spitzer\ Space\ Telescope.html
%doc licenses/GLEW.txt
%doc licenses/DejaVu-license.txt

%_iconsdir/hicolor/*/apps/*.png
%_datadir/%name/

%changelog
* Mon Oct 16 2023 Anton Golubev <golubevan@altlinux.org> 20230203-alt2
- fix FTBFS due to libfmt update
- better commentary on unused architectures
- fix warnings about cmake rpm macro not found

* Fri Mar 17 2023 Anton Golubev <golubevan@altlinux.org> 20230203-alt1
- initial build


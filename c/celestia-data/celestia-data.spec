Name: celestia-data
Version: 1.7.0
Release: alt1
Epoch: 1

Summary: Astronomical data files for Celestia
License: GPL-2.0
Group: Education
Url: https://celestiaproject.space/

# Data: git snapshot of CelestiaContent 00a1e8f3 (2025-09-23)
#   https://github.com/CelestiaProject/CelestiaContent
Vcs: https://github.com/CelestiaProject/CelestiaContent.git
# Source-url: https://github.com/CelestiaProject/CelestiaContent/commit/00a1e8f3
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc
BuildRequires: gettext-tools
BuildRequires: ImageMagick-tools

%description
Celestia is a free real-time space simulation that
lets you experience our universe in three dimensions.

This package contains the architecture independent
astronomical data shared by all Celestia frontends:
star and deep sky object catalogs, planet and moon
textures, 3D models and object name translations.

%prep
%setup

%build
%cmake \
    -DENABLE_NLS:BOOL=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %name.lang
%doc README
%_datadir/celestia/

%changelog
* Tue Jun 30 2026 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.0-alt1
- split out from the celestia package
- data from CelestiaContent (git snapshot 00a1e8f, 2025-09-23)

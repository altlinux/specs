Name: quaternion
Version: 0.0.9.3
Release: alt1

Summary: A Qt5-based IM client for Matrix

License: %gpl3only
Group: Networking/Instant messaging
Url: https://github.com/QMatrixClient/Quaternion

# Source-url: https://github.com/QMatrixClient/Quaternion/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5 rpm-macros-cmake

#BuildRequires(pre): rpm-build-compat >= 2.1.5
#BuildRequires(pre): rpm-build-intro >= 2.1.5
# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
#_tune_parallel_build_by_procsize 3000

BuildRequires: cmake gcc-c++ libstdc++-devel

BuildRequires: qt5-base-devel libqt5-core libqt5-network libqt5-gui qt5-imageformats qt5-quickcontrols2-devel qt5-tools-devel
# possible needs for smiles and emojicons
Requires: qt5-imageformats

BuildRequires: libqmatrixclient-devel

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.
This file contains general information about application usage and settings.

%prep
%setup

%build
%cmake_insource
# due precompiled headers
#export CCACHE_SLOPPINESS=pch_defines,time_macros
%make_build

%install
%makeinstall_std
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%doc README.md
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svgz
%_datadir/metainfo/com.github.quaternion.appdata.xml

%changelog
* Mon Jan 21 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.9.3-alt1
- initial build for ALT Sisyphus

Name: quaternion
Version: 0.0.97.1
Release: alt1

Summary: A Qt6-based IM client for Matrix

License: %gpl3only
Group: Networking/Instant messaging
Url: https://github.com/quotient-im/Quaternion

# Source-url: https://github.com/quotient-im/Quaternion/archive/%version.tar.gz
# Source-url: https://github.com/quotient-im/Quaternion/archive/master.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-macros-qt6 rpm-macros-cmake

BuildRequires: cmake gcc-c++ libstdc++-devel

BuildRequires: qt6-base-devel qt6-declarative-devel qt6-tools-devel qt6-multimedia-devel
# possible needs for smiles and emojicons
Requires: qt6-imageformats

BuildRequires: libquotient-qt6-devel libqtkeychain-qt6-devel libolm-devel

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.
This file contains general information about application usage and settings.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/io.github.quotient_im.Quaternion.desktop
%doc README.md
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/io.github.quotient_im.Quaternion.appdata.xml

%changelog
* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.97.1-alt1
- new version 0.0.97.1
- switch to Qt6 and libquotient-qt6

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.0.9.5-alt0.1.git6166373
- new version (0.0.9.5) with rpmgs script
- build from git 6166373

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.9.4c-alt1
- new version 0.0.9.4c (with rpmrb script)
- build with libquotient-devel (renamed from libqmatrixclient-devel)

* Mon Jan 21 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.9.3-alt1
- initial build for ALT Sisyphus

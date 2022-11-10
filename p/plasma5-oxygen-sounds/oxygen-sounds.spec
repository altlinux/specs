%define rname oxygen-sounds

Name: plasma5-oxygen-sounds
Version: 5.26.3
Release: alt2
Epoch: 1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: Oxygen sounds
Url: http://www.kde.org
License: GPL-2.0-or-later

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Tue Aug 30 2022 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libgpg-error libqt5-core libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-paste rpm-build-file rpm-build-python3 sh4 tzdata
BuildRequires: extra-cmake-modules qt5-base-devel

%description
%name provides encrypted vaults.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data sounds

%files
%doc LICENSES/*
%_K5snd/*

%changelog
* Thu Nov 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt2
- fix internal version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt1
- new version

* Tue Aug 30 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt1
- initial build

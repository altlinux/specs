%define rname oxygen-sounds

Name: oxygen-sounds
Version: 6.1.5
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: Oxygen sounds
Url: http://www.kde.org
License: LGPL-3.0-or-later

BuildArch: noarch

Provides: plasma5-oxygen-sounds = 1:%version-%release
Obsoletes: plasma5-oxygen-sounds < 1:%version-%release

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: qt5-base-devel

%description
%name provides encrypted vaults.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKF5_SUPPORT:BOOL=ON \
    #

%install
%K6install
%K6install_move data sounds

%files
%doc LICENSES/*
%_K6snd/*


%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


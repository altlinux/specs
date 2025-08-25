%define rname ocean-sound-theme

Name: ocean-sound-theme
Version: 6.4.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Ocean Sound Theme
Url: https://invent.kde.org/plasma/%rname
License: CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel

%description
%{summary}.

%package -n sound-theme-ocean
Group: Graphical desktop/Other
Summary: %{summary}
Requires: kde-common
Provides: ocean-sound-theme = %EVR
Obsoletes: ocean-sound-theme < %EVR
%description -n sound-theme-ocean
%{summary}.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data sounds

%files -n sound-theme-ocean
%doc LICENSES/*
%_K6snd/*

%changelog
* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Wed Jul 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- initial build

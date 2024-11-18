%define rname kmouth

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Speech Synthesizer Frontend for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kmouth = %EVR
Obsoletes: kde5-kmouth < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-speech-devel
BuildRequires: libssl-devel
BuildRequires: kf6-kcrash-devel kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel

%description
KMouth is an application that enables persons that cannot speak to let their computers speak.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKF_IGNORE_PLATFORM_CHECK=ON \
    #

%install
%K6install
%K6install_move data kmouth
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%config(noreplace) %_K6xdgconf/*rc
%_K6bin/kmouth
%_K6xdgapp/org.kde.kmouth.desktop
%_K6icon/*/*/apps/kmouth.*
%_K6icon/*/*/actions/*.*
%_K6data/kmouth/
%_datadir/metainfo/*kmouth*.xml

%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


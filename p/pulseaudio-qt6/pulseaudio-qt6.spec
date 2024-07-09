%define rname pulseaudio-qt

%define sover 5
%define libkf6pulseaudioqt libkf6pulseaudioqt%sover

Name: pulseaudio-qt6
Version: 1.5.0
Release: alt1

Group: System/Libraries
Summary: Qt-style wrapper for pulseaudio
License: LGPL-2.1-or-later
Url: https://invent.kde.org/libraries/pulseaudio-qt

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)

%description
It allows querying and manipulation of various PulseAudio objects such as
Sinks, Sources and Streams. It does not wrap the full feature set of libpulse.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
%summary.

%package -n %libkf6pulseaudioqt
Group: System/Libraries
Summary: %name library
%description -n %libkf6pulseaudioqt
%summary.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --all-name --with-qt

%files -n %libkf6pulseaudioqt
%doc LICENSES/*
%_K6lib/libKF6PulseAudioQt.so.%sover
%_K6lib/libKF6PulseAudioQt.so.*

%files devel
%_K6link/lib*.so
%_K6inc/*
%_libdir/cmake/KF6PulseAudioQt/
%_pkgconfigdir/KF6PulseAudioQt.pc

%changelog
* Tue Jul 09 2024 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- initial build

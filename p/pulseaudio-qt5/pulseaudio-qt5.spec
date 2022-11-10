%define rname pulseaudio-qt

%define sover 3
%define libkf5pulseaudioqt libkf5pulseaudioqt%sover

Name: pulseaudio-qt5
Version: 1.3
Release: alt1

Group: System/Libraries
Summary: Qt-style wrapper for pulseaudio
License: LGPL-2.1-or-later
Url: https://invent.kde.org/libraries/pulseaudio-qt

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel qt5-declarative-devel
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

%package -n %libkf5pulseaudioqt
Group: System/Libraries
Summary: %name library
%description -n %libkf5pulseaudioqt
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name --with-qt

%files -n %libkf5pulseaudioqt
%doc LICENSES/*
%_K5lib/libKF5PulseAudioQt.so.%sover
%_K5lib/libKF5PulseAudioQt.so.*

%files devel
%_K5link/lib*.so
%_K5inc/KF5PulseAudioQt/
%_K5inc/pulseaudioqt_version.h
%_libdir/cmake/KF5PulseAudioQt/

%changelog
* Thu Nov 10 2022 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- initial build

Name: liri-pulseaudio
Version: 0.0.20190816
Release: alt1

Summary: PulseAudio support for Liri
License: GPL
Group: Graphical desktop/Other
Url: https://github.com/lirios/pulseaudio

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(libpulse)
BuildRequires: qml(Fluid.Controls)

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/qt5/qml/Liri/PulseAudio
%_datadir/liri-settings/modules/pulseaudio
%_datadir/liri-settings/translations/modules/*.qm
%_datadir/liri-shell/indicators/pulseaudio

%changelog
* Fri Nov 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20190816-alt1
- initial

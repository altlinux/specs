Name: qmidiarp
Version: 0.7.1
Release: alt1

Summary: An arpeggiator, sequencer and MIDI LFO
License: GPLv2
Group: Sound
Url: https://sourceforge.net/projects/qmidiarp/

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ qt5-tools
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)

%package -n lv2-qmidiarp-plugin
Summary: An arpeggiator, sequencer and MIDI LFO as LV2
Group: Sound

%description
QMidiArp is an arpeggiator, sequencer and MIDI LFO for ALSA and JACK.

%description -n lv2-qmidiarp-plugin
QMidiArp is an arpeggiator, sequencer and MIDI LFO for ALSA and JACK.
This package contains above as LV2 plugin.

%prep
%setup

%build
%cmake -DCONFIG_LV2_UI_RTK=OFF
%cmake_build

%install
%cmake_install

%files
%_bindir/qmidiarp
%_datadir/qmidiarp/translations
%_datadir/metainfo/*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.svg
%_man1dir/qmidiarp.1*

%files -n lv2-qmidiarp-plugin
%_libdir/lv2/*.lv2

%changelog
* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.1-alt1
- 0.7.1 released

* Mon Jan 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 released

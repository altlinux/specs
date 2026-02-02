Name: qmidiarp
Version: 0.7.4
Release: alt1

Summary: An arpeggiator, sequencer and MIDI LFO
License: GPLv2
Group: Sound
Url: https://sourceforge.net/projects/qmidiarp/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ qt6-tools
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)
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
This package contains above as LV2 plugins.

%prep
%setup

%build
%cmake -DCONFIG_LV2_UI_RTK=OFF
%cmake_build

%install
%cmake_install

%files
%_bindir/qmidiarp
%_datadir/metainfo/*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.svg
%_man1dir/qmidiarp.1*

%files -n lv2-qmidiarp-plugin
%_libdir/lv2/*.lv2

%changelog
* Mon Feb 02 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.4-alt1
- 0.7.4 released

* Mon Jan 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.3-alt1
- 0.7.3 released

* Wed Dec 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.2-alt1
- 0.7.2 released

* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.1-alt1
- 0.7.1 released

* Mon Jan 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 released

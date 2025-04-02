Name: muse
Version: 4.2.1
Release: alt1

Summary: MIDI/Audio sequencer
License: GPLv2
Group: Sound
Url: https://github.com/muse-sequencer/muse

Source: %name-%version.tar

BuildRequires: cmake extra-cmake-modules gcc-c++ ladspa_sdk
BuildRequires: rpm-build-python3
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(dssi)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(serd-0)
BuildRequires: pkgconfig(sord-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(rubberband)

%description
MusE is a MIDI/Audio sequencer with recording and editing capabilities
written originally by Werner Schweer now developed and maintained by
the MusE development team.
MusE aims to be a complete multitrack virtual studio for Linux.

%prep
%setup

%build
%cmake -DMODULES_BUILD_STATIC=ON
%cmake_build

%install
%cmakeinstall_std
# already linked in
find %buildroot%_libdir/muse -type f -name \*.a |xargs rm -v
# internal synths, borked
rm -rf %buildroot%_libdir/muse/synthi
# no embedded python for now
rm -fr %buildroot%_datadir/muse/pybridge

%global _customdocdir %_defaultdocdir/muse

%files
%_customdocdir
%_bindir/muse
%_bindir/muse_plugin_scan
%_bindir/grepmidi
%_libdir/muse
%_datadir/muse
%_desktopdir/*.desktop
%_datadir/mime/packages/*.xml
%_datadir/metainfo/*.xml
%_iconsdir/*/*/*/*.png
%_man1dir/muse.1*
%_man1dir/grepmidi.1*

%changelog
* Fri Mar 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.2.1-alt1
- 4.2.1 released

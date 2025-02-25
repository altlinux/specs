Name: jc303
Version: 0.11.1
Release: alt1

Summary: Roland TB-303 clone plugin
License: GPLv3
Group: Sound
Url: https://midilab.co/jc303/

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: deps-%version.tar

%ifdef bootstrap
BuildRequires: git-core
%endif

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%package -n lv2-jc303-plugin
Summary: Roland TB-303 clone plugin
Group: Sound

%package -n vst3-jc303-plugin
Summary: Roland TB-303 clone plugin
Group: Sound

%define desc\
JC303 is Bass Synthesizer Audio Plugin, clone of Roland TB-303.\
This project is a JUCE port of Robin Schmidt's Open303 DSP engine

%description %desc.

%description -n lv2-jc303-plugin %desc,
in form of LV2 plugin.

%description -n vst3-jc303-plugin %desc,
in form of VST3 plugin.

%prep
%setup
%ifdef bootstrap
%cmake
tar cf %SOURCE1 lib/JUCE
%else
tar xf %SOURCE1
%endif

%build
%cmake -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
mkdir -p %buildroot%_libdir/{lv2,vst3}
cp -av %_cmake__builddir/*_artefacts/LV2/* %buildroot%_libdir/lv2                                                                                                   
cp -av %_cmake__builddir/*_artefacts/VST3/* %buildroot%_libdir/vst3

%files -n lv2-jc303-plugin
%doc LICENSE README*
%_libdir/lv2/*

%files -n vst3-jc303-plugin
%doc LICENSE README*
%_libdir/vst3/*

%changelog
* Tue Feb 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.11.1-alt1
- initial

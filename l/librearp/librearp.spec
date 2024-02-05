Name: librearp
Version: 2.5
Release: alt1

Summary: A pattern-based arpeggio generator
License: GPLv3
Group: Sound
Url: https://librearp.gitlab.io/

ExcludeArch: ppc64le

Source0: %name-%version-%release.tar
Source1: juce.tar

BuildRequires: cmake gcc-c++
BuildRequires: ladspa_sdk
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xcursor)

%package -n lv2-librearp-plugin
Summary: A pattern-based arpeggio generator plugin
Group: Sound

%package -n vst3-librearp-plugin
Summary: A pattern-based arpeggio generator plugin
Group: Sound

%description
%summary

%description -n lv2-librearp-plugin
%summary as LV2 plugin

%description -n vst3-librearp-plugin
%summary as VST3 plugin

%prep
%setup -a1

%build
%cmake
%cmake_build

%install
mkdir -p %buildroot%_libdir/{lv2,vst3}
cp -av %_cmake__builddir/LibreArp_artefacts/LV2/* %buildroot%_libdir/lv2/
cp -av %_cmake__builddir/LibreArp_artefacts/VST3/* %buildroot%_libdir/vst3/

%if 0
%files -n lv2-librearp-plugin
%doc LICENSE.* README.*
%_libdir/lv2/*
%endif

%files -n vst3-librearp-plugin
%doc LICENSE.* README.*
%_libdir/vst3/*

%changelog
* Tue Jan 30 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- 2.5 released

Name: socalabs-plugins
Version: 1.1.0
Release: alt1

Summary: Various LV2/VST3 plugins from socalabs.com
License: BSD-3-Clause
Group: Sound
Url: https://github.com/FigBug/slPlugins

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%package -n lv2-socalabs-plugins
Summary: Various LV2 plugins from socalabs.com
Group: Sound

%package -n vst3-socalabs-plugins
Summary: Various VST3 plugins from socalabs.com
Group: Sound

%description
%summary

%description -n lv2-socalabs-plugins
Various LV2 plugins from socalabs.com

%description -n vst3-socalabs-plugins
Various VST3 plugins from socalabs.com

%prep
%setup -a1
sed -i /Maths/d plugins/CMakeLists.txt
sed -i /SFX8/d plugins/CMakeLists.txt

%build
%cmake
%cmake_build

%install
mkdir -p %buildroot%_libdir/{lv2,vst3}
cp -av %_cmake__builddir/plugins/*/*/LV2/*.lv2 %buildroot%_libdir/lv2
cp -av %_cmake__builddir/plugins/*/*/VST3/*.vst3 %buildroot%_libdir/vst3

%files -n lv2-socalabs-plugins
%_libdir/lv2/*

%files -n vst3-socalabs-plugins
%_libdir/vst3/*

%changelog
* Wed Dec 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- initial

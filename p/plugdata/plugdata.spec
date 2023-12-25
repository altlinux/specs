ExclusiveArch: x86_64

Name: plugdata
Version: 0.8.2
Release: alt1

Summary: Pure Data as a plugin, with a new GUI
License: GPLv3
Group: Sound

Url: https://plugdata.org
VCS: https://github.com/plugdata-team/plugdata.git

Source: %name-%version.tar
Source1: %name-%version-libraries-juce.tar
Source2: %name-%version-libraries-clap-juce-extensions.tar
Source3: %name-%version-libraries-clap-juce-extensions-clap-libs-clap.tar
Source4: %name-%version-libraries-clap-juce-extensions-clap-libs-clap-helpers.tar
Source5: %name-%version-libraries-concurrentqueue.tar
Source6: %name-%version-libraries-heavylib.tar
Source7: %name-%version-libraries-pd-else.tar
Source8: %name-%version-libraries-pd-lua.tar
Source9: %name-%version-libraries-plugdata-ofelia.tar
Source10: %name-%version-libraries-plugdata-ofelia-libraries-cppsockets.tar
Source11: %name-%version-libraries-pure-data.tar
Source100: plugdata.desktop

Patch0: %name-%version-%release.patch
Patch1: 001-juceaide-fix-return-type.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++
BuildRequires: cmake >= 3.21
BuildRequires: ctest >= 3.21
BuildRequires: python3
BuildRequires: libX11-devel libXcomposite-devel libXcursor-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXi-devel
BuildRequires: libGL-devel
BuildRequires: libfreetype-devel bzlib-devel libpcre2-devel libbrotli-devel
BuildRequires: libcurl-devel
BuildRequires: libalsa-devel
BuildRequires: pipewire-jack-libs-devel
BuildRequires: liblua5.4-devel

%description
Plugin wrapper around Pure Data to allow patching in a wide selection of DAWs.

%package -n vst3-%name
Group: Sound
Summary: Pure Data as a plugin, with new GUI (VST3)

%description -n vst3-%name
Plugin wrapper around PureData to allow patching in a wide selection of DAWs.

%package -n lv2-%name
Group: Sound
Summary: Pure Data as a plugin, with new GUI (LV2)

%description -n lv2-%name
Plugin wrapper around PureData to allow patching in a wide selection of DAWs.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11
%patch0 -p1

pushd Libraries/JUCE
%patch1 -p1
popd

%build
%cmake
%cmake_build

%install
mkdir -p %buildroot%_bindir
install Plugins/Standalone/* %buildroot%_bindir/
mkdir -p %buildroot%_libdir/vst3
cp -r Plugins/VST3/*.vst3 %buildroot%_libdir/vst3/
mkdir -p %buildroot%_libdir/lv2
cp -r Plugins/LV2/*.lv2 %buildroot%_libdir/lv2/

install -D -m 644 Resources/Icons/plugdata_logo.png %buildroot%_datadir/pixmaps/PlugData.png
install -D -m 644 %SOURCE100 %buildroot%_datadir/applications/plugdata.desktop

%files
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%doc README* LICENSE*

%files -n vst3-%name
%_libdir/vst3/
%doc README* LICENSE*

%files -n lv2-%name
%_libdir/lv2/
%doc README* LICENSE*

%changelog
* Wed Dec 13 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri Nov 17 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.1-alt1
- 0.8.1

* Fri Oct 27 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Oct 26 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

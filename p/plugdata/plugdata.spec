ExcludeArch: ppc64le %ix86

Name: plugdata
Version: 0.9.1
Release: alt1

Summary: JUCE-based plugin wrapper for Pure Data visual programming language
License: GPLv3
Group: Sound

Url: https://plugdata.org
VCS: https://github.com/plugdata-team/plugdata.git

Source: %name-%version.tar
Source1: %name-%version-libraries-gem.tar
Source2: %name-%version-libraries-juce.tar
Source3: %name-%version-libraries-clap-juce-extensions.tar
Source4: %name-%version-libraries-clap-juce-extensions-clap-libs-clap.tar
Source5: %name-%version-libraries-clap-juce-extensions-clap-libs-clap-helpers.tar
Source6: %name-%version-libraries-concurrentqueue.tar
Source7: %name-%version-libraries-fuzzysearchdatabase.tar
Source8: %name-%version-libraries-heavylib.tar
Source9: %name-%version-libraries-melatonin_blur.tar
Source10: %name-%version-libraries-nanovg.tar
Source11: %name-%version-libraries-pd-cyclone.tar
Source12: %name-%version-libraries-pd-else.tar
Source13: %name-%version-libraries-pd-lua.tar
Source14: %name-%version-libraries-pd-lua-lua.tar
Source15: %name-%version-libraries-plf_stack.tar
Source16: %name-%version-libraries-pure-data.tar
Source17: %name-%version-libraries-readerwriterqueue.tar
Source100: plugdata.desktop

Patch0: %name-%version-%release.patch
Patch1: 001-juceaide-fix-return-type.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: /proc

# build tools
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.21
BuildRequires: ctest >= 3.21
BuildRequires: python3

# generic libs
BuildRequires: libghc_filesystem-devel
BuildRequires: bzlib-devel libpcre2-devel libbrotli-devel

# curl and stuff
BuildRequires: libcurl-devel
BuildRequires: libidn2-devel libzstd-devel libkrb5-devel libgnutls-devel
BuildRequires: libnettle-devel libtasn1-devel libp11-kit-devel libpsl-devel
BuildRequires: libgsasl-devel libssh2-devel libssl-devel
BuildRequires: libngtcp2-devel libnghttp2-devel libnghttp3-devel

# audio stuff
BuildRequires: libalsa-devel
BuildRequires: pipewire-jack-libs-devel

# X11, graphics stuff
BuildRequires: libX11-devel libXcomposite-devel libXcursor-devel
BuildRequires: libXext-devel libXinerama-devel libXrandr-devel
BuildRequires: libXrender-devel libXi-devel libGL-devel
BuildRequires: libfreetype-devel

%description
PlugData is a plugin wrapper for Pure Data, featuring a modern JUCE-based GUI.
Includes the ELSE collection of externals and abstractions, providing a comprehensive set of tools for audio processing.
PlugData aims to offer an improved patching experience for various DAWs and can also function as a standalone replacement for Pure Data.

Key Features:
- Modern JUCE-based graphical interface
- DAW compatibility (as LV2 or VST3 plugins)
- Standalone replacement for Pure Data
- Integrated ELSE collection of externals and abstractions
- Enhanced patching experience

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
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17
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
* Thu Jun 19 2025 Aleksandr Yukhnenko <neff@altlinux.org> 0.9.1-alt1
- Version 0.9.1.

* Wed Jun 11 2025 Aleksandr Yukhnenko <neff@altlinux.org> 0.9.0-alt1
- Version 0.9.0.
- Build for more architectures.

* Mon Jan 29 2024 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.3-alt1
- 0.8.3

* Wed Dec 13 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri Nov 17 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.1-alt1
- 0.8.1

* Fri Oct 27 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Oct 26 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

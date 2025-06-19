ExcludeArch: ppc64le %ix86

Name: dexed
Version: 0.9.7
Release: alt1

License: GPLv3
Summary: Dexed FM synthesizer
Group: Sound

Vcs: https://github.com/asb2m10/dexed.git
Url: https://asb2m10.github.io/dexed/

Source: %name-%version.tar
Source1: %name-%version-libs-juce.tar
Source2: %name-%version-libs-mts-esp.tar
Source3: %name-%version-libs-clap-juce-extensions.tar
Source4: %name-%version-libs-clap-juce-extensions-clap-libs-clap.tar
Source5: %name-%version-libs-clap-juce-extensions-clap-libs-clap-helpers.tar
Source6: %name-%version-libs-surgesynthteam_tuningui.tar
Source7: %name-%version-libs-tuning-library.tar
Source8: %name-%version-libs-vst3sdk.tar
Source9: %name-%version-libs-vst3sdk-base.tar
Source10: %name-%version-libs-vst3sdk-cmake.tar
Source11: %name-%version-libs-vst3sdk-doc.tar
Source12: %name-%version-libs-vst3sdk-pluginterfaces.tar
Source13: %name-%version-libs-vst3sdk-public.sdk.tar
Source14: %name-%version-libs-vst3sdk-vstgui4.tar
Source100: dexed.desktop

Patch0: 001-juceaide-fix-return-type.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: /proc

# build tools
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.21
BuildRequires: ctest >= 3.21
BuildRequires: python3

# generic libs
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
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.

%package -n vst3-%name
Group: Sound
Summary: Dexed FM synthesizer as VST3 plugin.

%description -n vst3-%name
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.

%package -n clap-%name
Group: Sound
Summary: Dexed FM synthesizer as CLAP plugin.

%description -n clap-%name
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14

pushd libs/JUCE
%patch0 -p1
popd

%build
%cmake
%cmake_build

%install
mkdir -p %buildroot%_bindir
install %_target_alias/Source/Dexed_artefacts/Standalone/Dexed %buildroot%_bindir/
mkdir -p %buildroot%_libdir/vst3
cp -r %_target_alias/Source/Dexed_artefacts/VST3/Dexed.vst3 %buildroot%_libdir/vst3/
mkdir -p %buildroot%_libdir/clap
install %_target_alias/Source/Dexed_artefacts/CLAP/Dexed.clap %buildroot%_libdir/clap/

install -D -m 644 Resources/ui/dexedIcon.png %buildroot%_datadir/pixmaps/dexed.png
install -D -m 644 %SOURCE100 %buildroot%_datadir/applications/dexed.desktop

%files
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%doc README* LICENSE*

%files -n vst3-%name
%_libdir/vst3/
%doc README* LICENSE*

%files -n clap-%name
%_libdir/clap/
%doc README* LICENSE*

%changelog
* Mon Jun 16 2025 Aleksandr Yukhnenko <neff@altlinux.org> 0.9.7-alt1
- Version 0.9.7.
- Build CLAP plugin.
- Disable build for x86 (32-bit) architectures.

* Tue Dec 26 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.9.6-alt2
- NMU: Build on more architectures. Use all available cores.

* Thu Dec 14 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus

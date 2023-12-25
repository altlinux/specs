ExclusiveArch: %ix86 x86_64

Name: dexed
Version: 0.9.6
Release: alt1

License: GPLv3
Summary: DX7 FM multi plaform/multi format plugin
Group: Sound

Vcs: https://github.com/asb2m10/dexed.git
Url: https://asb2m10.github.io/dexed/

Source: %name-%version.tar
Source1: %name-%version-libs-surgesynthteam_tuningui.tar
Source2: %name-%version-libs-tuning-library.tar
Source3: %name-%version-libs-vst3sdk.tar
Source4: %name-%version-libs-vst3sdk-base.tar
Source5: %name-%version-libs-vst3sdk-cmake.tar
Source6: %name-%version-libs-vst3sdk-doc.tar
Source7: %name-%version-libs-vst3sdk-pluginterfaces.tar
Source8: %name-%version-libs-vst3sdk-public.sdk.tar
Source9: %name-%version-libs-vst3sdk-vstgui4.tar
Source10: %name-%version-juce.tar
Source100: dexed.desktop

Patch0: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libfreetype-devel
BuildRequires: libcurl-devel
BuildRequires: libX11-devel libXrandr-devel libXinerama-devel libXcursor-devel
BuildRequires: libalsa-devel
BuildRequires: pipewire-jack-libs-devel

%description
DX7 FM multi plaform/multi format plugin.

%package -n vst3-%name
Group: Sound
Summary: DX7 FM multi plaform/multi format plugin

%description -n vst3-%name
DX7 FM multi plaform/multi format plugin.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10
%patch0 -p1

%build
# Build Projucer
pushd ./assets/JUCE/extras/Projucer/Builds/LinuxMakefile
make all
popd
cp ./assets/JUCE/extras/Projucer/Builds/LinuxMakefile/build/Projucer ./assets/JUCE/

# Build Dexed
./scripts/projuce.sh
./scripts/build-lin.sh

%install
mkdir -p %buildroot%_bindir
install Builds/Linux/build/Dexed %buildroot%_bindir/
mkdir -p %buildroot%_libdir/vst3
cp -r Builds/Linux/build/Dexed.vst3 %buildroot%_libdir/vst3/

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

%changelog
* Thu Dec 14 2023 Aleksandr Yukhnenko <neff@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus

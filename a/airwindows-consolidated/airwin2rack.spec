
%define aw_git 444daa9502

%define _unpackaged_files_terminate_build 1
%define _optlevel 3
%define aw_build_type RelWithDebInfo

Name:    airwindows-consolidated
Version: 2.12.0
Release: alt1.git%aw_git

Summary: Airwindows, Consolidated into a single DAW plugin
License: MIT
Group:   Sound
Url:     https://github.com/baconpaul/airwin2rack

ExcludeArch: %ix86 ppc64le

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: airwin2rack-snapshot.tar

# We manage dependencies via gear-subrepo, and bundle them all together here:
Source1: deps.tar

Patch1: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)


%define common_description This is Airwindows plugins, of the Airwindows plugins\
originally developed by Chris Johnson (https://www.airwindows.com),\
presented as a consolidated plugin for your DAW.\
%nil

%description
%common_description

%package standalone
Summary: Airwindows, Consolidated into a single executable
Group:   Sound

%description standalone
%common_description

This package contains Airwindows Consolidated built as
a standalone executable.


%package -n lv2-%name-plugin
Summary: Airwindows, Consolidated into a single LV2 plugin
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains Airwindows Consolidated built as a LV2 plugin.


%package -n vst3-%name-plugin
Summary: Airwindows, Consolidated into a single VST3 plugin
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains Airwindows Consolidated built as a VST3 plugin.


%prep
%setup -n airwin2rack-snapshot
tar -xaf %{SOURCE1}

%autopatch -p1

# build juceaid on in parallel
sed -i -r "s/(--config\s+\S+)/\1 --parallel %_smp_build_ncpus/" \
    deps/JUCE/extras/Build/juceaide/CMakeLists.txt
grep parallel deps/JUCE/extras/Build/juceaide/CMakeLists.txt || exit 1

sed -i "s/unknownhash/%aw_git/" cmake/basic-installer.cmake
grep "%aw_git" cmake/basic-installer.cmake || exit 1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=%aw_build_type \
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  -DBUILD_JUCE_PLUGIN=ON \
  -DCPM_LOCAL_PACKAGES_ONLY=ON \
  -DCPM_SOURCE_CACHE=$(pwd)/deps/cpm \
  -DCPM_JUCE_SOURCE=$(pwd)/deps/JUCE \
  %nil

%cmake_build

%install
cd "%_cmake__builddir/awcons-products"

mkdir -p %buildroot%_libdir/lv2
cp -a *.lv2 %buildroot%_libdir/lv2/

mkdir -p %buildroot%_libdir/vst3
cp -a *.vst3 %buildroot%_libdir/vst3/

install -Dm755 'Airwindows Consolidated' \
    '%buildroot/%_bindir/Airwindows Consolidated'

%files standalone
%_bindir/Airwindows*

%files -n lv2-%name-plugin
%_libdir/lv2/*

%files -n vst3-%name-plugin
%_libdir/vst3/*

%changelog
* Mon Jun 16 2025 Ivan A. Melnikov <iv@altlinux.org> 2.12.0-alt1.git444daa9502
- initial build for Sisyphus

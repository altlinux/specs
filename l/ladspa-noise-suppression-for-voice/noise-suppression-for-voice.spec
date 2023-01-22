%define _unpackaged_files_terminate_build 1

Name: ladspa-noise-suppression-for-voice
Version: 1.03
Release: alt1.20230122.gc1cf430

Summary: Real-time noise suppression plugin
Group: Sound
License: GPL-3.0
Url: https://github.com/werman/noise-suppression-for-voice

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ladspa_sdk
BuildRequires: rpm-macros-cmake

%description
Real-time noise suppression plugin for voice based on Xiph's RNNoise.
The plugin is meant to suppress a wide range of noise origins: computer fans,
office, crowd, airplane, car, train, construction.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_LADSPA_PLUGIN=ON \
	-DBUILD_VST_PLUGIN=OFF \
	-DBUILD_VST3_PLUGIN=OFF \
	-DBUILD_LV2_PLUGIN=OFF \
	-DBUILD_AU_PLUGIN=OFF \
	-DBUILD_AUV3_PLUGIN=OFF

%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/ladspa/librnnoise_ladspa.so
%doc README.md

%changelog
* Sun Jan 22 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.03-alt1.20230122.gc1cf430
- Initial build

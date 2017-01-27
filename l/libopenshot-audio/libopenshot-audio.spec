%define _name libopenshot
%define ver_major 0.1
%define api_ver 0
%define libopenshot_ver %ver_major.3

Name: %_name-audio
Version: %ver_major.2
Release: alt1

Summary: OpenShot Audio Library
Group: System/Libraries
License: GPLv3
Url: https://launchpad.net/%_name

Source: %url/%ver_major/%libopenshot_ver/+download/%name-%version.tar.gz

BuildRequires: gcc-c++ cmake libalsa-devel libfreetype-devel
BuildRequires: libX11-devel libXrandr-devel libXext-devel libXinerama-devel libXcursor-devel

%description
OpenShot Audio Library is a program that allows the high-quality editing
and playback of audio, and is based on the amazing JUCE library.

%package devel
Summary: OpenShot Audio Library development package
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup -D -c -n %name-%version

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/openshot-audio-test-sound
%_libdir/%name.so.*
%_man1dir/openshot-audio-test-sound.1.*
%doc AUTHORS README

%files devel
%_includedir/%name/
%_libdir/%name.so

%changelog
* Fri Jan 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus



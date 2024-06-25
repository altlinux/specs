%define _name libopenshot
%define ver_major 0.3
%define api_ver 9
%define libopenshot_ver 0.3

# no tests
%def_disable check

Name: %_name-audio
Version: %ver_major.3
Release: alt1

Summary: OpenShot Audio Library
Group: System/Libraries
License: GPL-3.0
Url: https://launchpad.net/%_name

Vcs: https://github.com/OpenShot/libopenshot-audio.git
#Source: %url/%ver_major/%libopenshot_ver/+download/%name-%version.tar.gz
Source: https://github.com/OpenShot/%name/archive/v%version/%name-%version.tar.gz

%define python_ver 3.0

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++ python3 >= %python_ver zlib-devel libalsa-devel libfreetype-devel
%{?_enable_check:BuildRequires: ctest}

%description
OpenShot Audio Library is a program that allows the high-quality editing
and playback of audio, and is based on the amazing JUCE library.

%package devel
Summary: OpenShot Audio Library development package
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%ifarch %e2k
%add_optflags -DJUCE_NO_INLINE_ASM=1 -DJUCE_USE_SIMD=0
%endif
%cmake \
    -DENABLE_AUDIO_DOCS=OFF
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files
%_bindir/openshot-audio-demo
%_libdir/%name.so.*
%_man1dir/openshot-audio-demo.1.*
%doc AUTHORS README*

%files devel
%_includedir/%name/
%_libdir/%name.so
%_libdir/cmake/OpenShotAudio/

%changelog
* Tue Jun 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Fri Apr 21 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Fri Apr 07 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Dec 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0
- applied fix for %%e2k (ilyakurdyukov@ & mike@)

* Tue Sep 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Wed Aug 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1.1
- rebuild with new cmake macros

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Sat Mar 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Sat Jun 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Mon Nov 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Fri Jan 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus



%define git %nil

Name: libaptx
Version: 1.3.1
Release: alt1
Summary: reverse-engineered apt-X codec library
License: MIT
Group: System/Libraries
Url: https://github.com/Arkq/openaptx
Packager: L.A. Kostis <lakostis@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: libsndfile-devel libavcodec-devel doxygen

Obsoletes: libopenaptx <= 1.2.0-alt1

%description
[open]aptx - reverse-engineered apt-X

This project is for research purposes only. Without a proper license private
and commercial usage might be a case of a patent infringement. If you are
looking for a library, which can be installed and used legally (commercial,
private and educational usage), go to the Qualcomm(R) aptX(TM) and contact
Qualcomm customer service.

The source code itself is licensed under the terms of the MIT license. However,
compression algorithms are patented and licensed under the terms of a
proprietary license. Hence, compilation and redistribution in a binary format
is forbidden!

%package tools
Summary: apt-X library tools
Group: Sound
Requires: %name = %EVR
Obsoletes: libopenaptx-tools <= 1.2.0-alt1

%description tools
Tools to work with %name.

%package devel
Summary: apt-X header files
Group: Development/C
Requires: %name = %EVR
Obsoletes: libopenaptx-devel <= 1.2.0-alt1

%description devel
%name-devel contains header files needed to
develop programs which make use of %name

%prep
%setup -q

%build
%cmake \
	-DENABLE_DOC=ON \
	-DENABLE_APTX422=ON \
	-DENABLE_APTXHD100=ON \
	-DWITH_FFMPEG=ON \
	-DWITH_SNDFILE=ON
%cmake_build

%install
%cmake_install

%files
%_libdir/*.so

%files tools
%_bindir/*

%files devel
%_includedir/*.h
%_pkgconfigdir/*.pc
%_man3dir/openaptx.h.*

%changelog
* Wed Dec 14 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.1-alt1
- 1.3.1.
- use cmake.

* Thu Jan 07 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2.0-alt2
- libopenaptx->libaptx to co-exists with another openaptx for pipewire.

* Thu Dec 10 2020 L.A. Kostis <lakostis@altlinux.ru> 1.2.0-alt1
- 1.2.0.
- use ffmpeg for encoding.

* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.gebcf004
- Initial build for ALTLinux.

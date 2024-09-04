Name: libavif
Version: 1.1.1
Release: alt1

Summary: Implementation of the AV1 Image File Format
License: BSD
Group: System/Libraries
Url: https://github.com/AOMediaCodec/libavif

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(libyuv)
BuildRequires: pkgconfig(dav1d)
BuildRequires: pkgconfig(rav1e)

%package devel
Summary: Implementation of the AV1 Image File Format
Group: Development/C

%define desc\
This library aims to be a friendly, portable C implementation\
of the AV1 Image File Format, as described here:\
https://aomediacodec.github.io/av1-avif/

%description %desc

%description devel %desc
this package contains development part of libavif

%prep
%setup

%build
%cmake -DAVIF_CODEC_DAV1D=ON -DAVIF_CODEC_RAV1E=ON
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/libavif
%_pkgconfigdir/*

%changelog
* Wed Sep 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt1
- 1.1.1 released

* Fri Feb 09 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt1
- 1.0.4 released

* Thu Dec 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3 released

* Tue Nov 21 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- 1.0.2 released

* Tue Aug 29 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Thu Nov 24 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt1
- 0.11.1 released

* Mon Apr 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt1
- 0.10.1 released

* Fri Nov 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.3-alt1
- initial

Name: AMF
Version: 1.5.2
Release: alt1
Summary: Advanced Media Framework (AMF) SDK
License: MIT
Url: https://gpuopen.com/advanced-media-framework/
VCS: https://github.com/GPUOpen-LibrariesAndSDKs/AMF
Group: Development/C
BuildArch: noarch
Source0: %name-%version.tar

%description
The AMD Advanced Media Framework (AMF) SDK provides GPU-accelerated video processing,
including hardware encoding (H.264/AVC, H.265/HEVC, AV1) and decoding via AMD GPUs.
It is optimized for low-latency streaming, transcoding, and professional media workflows.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
The AMD Advanced Media Framework (AMF) SDK provides GPU-accelerated video processing,
including hardware encoding (H.264/AVC, H.265/HEVC, AV1) and decoding via AMD GPUs.
It is optimized for low-latency streaming, transcoding, and professional media workflows.

The %name-devel package contains header files for developing applications that use %name.

%package docs
Summary: PDF documentation for %name
Group: Development/C

%description docs
API reference, programming guides, and examples for AMD AMF.
Includes details on driver requirements and hardware acceleration support.

%prep
%setup

%install
mkdir -p %buildroot%_includedir/%name
cp -fr amf/public/include/* %buildroot%_includedir/%name/
mkdir docs
mv amf/doc/*pdf docs/

%files devel
%doc amf/doc/* LICENSE.txt
%_includedir/%name/

%files docs
%doc LICENSE.txt
%doc docs/*

%changelog
* Mon May 18 2026 Anton Farygin <rider@altlinux.org> 1.5.2-alt1
- 1.5.0 -> 1.5.2

* Sun Nov 23 2025 Anton Farygin <rider@altlinux.com> 1.5.0-alt1
- 1.4.26 -> 1.5.0

* Thu Jun 26 2025 Anton Farygin <rider@altlinux.com> 1.4.36-alt1
- initial build for ALT Linux

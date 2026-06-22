# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with check

%define sover 3

Name: vmaf
Version: 3.2.0
Release: alt1

Summary: Perceptual video quality assessment based on multi-method fusion
License: BSD-2-Clause-Patent
Group: Video
URL: https://github.com/Netflix/vmaf
VCS: https://github.com/Netflix/vmaf

# Source-url: %vcs/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch: vmaf-3.2.0-test-predict-double-cmp-fix.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: xxd
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: nasm

%description
VMAF is an Emmy-winning perceptual video quality assessment algorithm
developed by Netflix.

%package -n libvmaf%sover
Summary: Shared library for VMAF
Group: System/Libraries

%description -n libvmaf%sover
Shared library for VMAF, with additional implementations
for PSNR, PSNR-HVS, SSIM, MS-SSIM and CIEDE2000.

%package -n libvmaf-devel
Summary: Development files for libvmaf
Group: Development/C
Requires: libvmaf%sover = %EVR

%description -n libvmaf-devel
Development files for libvmaf.

%package -n libvmaf-devel-doc
Summary: Development documentation for libvmaf
Group: Documentation
BuildArch: noarch

%description -n libvmaf-devel-doc
Development documentation for libvmaf.

%package models
Summary: VMAF model files
Group: Other
BuildArch: noarch

%description models
Additional models for VMAF in JSON/Pickle format.
Typically used when builtin models are not appropriate.

%prep
%setup
%autopatch -p1

%build
pushd libvmaf
%meson \
    -Ddefault_library=shared
%meson_build
%meson_build doc/html
popd

%install
pushd libvmaf
%meson_install
popd

pushd model
find . -type f -print0 \
    | xargs -r0 -I{} install -pD -m644 {} %buildroot%_datadir/vmaf/models/{}
popd

%if_with check
%check
pushd libvmaf
%meson_test
popd
%endif

%files
%doc README.md CHANGELOG.md LICENSE
%_bindir/vmaf

%files -n libvmaf%sover
%_libdir/libvmaf.so.%sover
%_libdir/libvmaf.so.%version

%files -n libvmaf-devel
%_includedir/libvmaf
%_libdir/libvmaf.so
%_pkgconfigdir/libvmaf.pc

%files -n libvmaf-devel-doc
%doc CONTRIBUTING.md resource/doc/*.md libvmaf/%__builddir/doc/html

%files models
%dir %_datadir/vmaf
%_datadir/vmaf/models

%changelog
* Mon Jun 22 2026 Valery Zabrovsky <brow@altlinux.org> 3.2.0-alt1
- New version 3.2.0.

* Wed May 27 2026 Valery Zabrovsky <brow@altlinux.org> 3.1.0-alt1
- Initial build for ALT Sisyphus.

%define _unpackaged_files_terminate_build 1

Name: lv2-triforce-plugin
Version: 0.3.2
Release: alt1
Summary: A microphone beamformer for Linux on Apple Silicon Macs written in Rust
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://github.com/chadmed/triforce
VCS: https://github.com/chadmed/triforce.git

ExclusiveArch: aarch64

Source: %name-%version.tar
Source1: vendor.tar

Requires: lv2

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(lv2)

%description
Triforce implements a Minimum Variance Distortionless Response adaptive
beamformer for the microphone array found in the Apple Silicon laptops.

%prep
%setup -a1
%rust_prep

%build
%make

%install
%makeinstall_std \
    DESTDIR=%buildroot \
    LIBDIR=%_libdir

%files
%doc README.md
%_libdir/lv2/triforce.lv2

%changelog
* Fri Aug 28 2026 Vasiliy Doylov <neko@altlinux.org> 0.3.2-alt1
- Initial build for ALT.

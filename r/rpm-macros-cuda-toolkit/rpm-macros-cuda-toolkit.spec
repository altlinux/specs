Name: rpm-macros-cuda-toolkit
Version: 0.1
Release: alt1

Summary: RPM helper macros to rebuild packages depending on nvidia-cuda-toolkit

Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/

Source0: cuda-toolkit

BuildArch: noarch

%description
These helper macros provide the ability to rebuild
packages dependent on nvidia-cuda-toolkit: supported compute
capabilities, host compiler (gcc version supported by nvcc),
ready-made nvcc/cmake/torch flags.

%install
install -D -m644 %SOURCE0 %buildroot%_rpmmacrosdir/cuda-toolkit

%files
%_rpmmacrosdir/cuda-toolkit

%changelog
* Mon Sep 14 2026 Mikhail Tergoev <fidel@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus

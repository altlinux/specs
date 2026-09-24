Name: rpm-macros-cuda-toolkit
Version: 0.2
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
* Thu Sep 24 2026 Mikhail Tergoev <fidel@altlinux.org> 0.2-alt1
- Fix %%cuda_version and %%cuda_gcc_version for p11 (Closes: #60651)
- For CUDA 12 returned Maxwell/Pascal/Volta archs to %%cuda_archs

* Mon Sep 14 2026 Mikhail Tergoev <fidel@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus

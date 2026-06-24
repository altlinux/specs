%define _unpackaged_files_terminate_build 1

%def_with check

Name: llmfit
Version: 0.9.33
Release: alt1

Summary: Hundreds of models & providers
License: MIT
Group: Sciences/Computer science
Url: https://github.com/AlexsJones/llmfit
VCS: https://github.com/AlexsJones/llmfit.git

# Source-url: https://github.com/AlexsJones/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo

%description
One command to find what runs on your hardware.

A terminal tool that right-sizes LLM models to your system's RAM, CPU,
and GPU. Detects your hardware, scores each model across quality, speed,
fit, and context dimensions, and tells you which ones will actually run
well on your machine.

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md API.md
%_bindir/%name

%changelog
* Wed Jun 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.33-alt1
- new version

* Thu Jun 11 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.31-alt1
- new version

* Wed May 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.28-alt1
- new version

* Thu May 21 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.27-alt1
- new version

* Wed May 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.26-alt1
- new version

* Mon May 18 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.25-alt1
- new version

* Wed May 13 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.24-alt1
- new version

* Tue May 12 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.23-alt1
- new version

* Thu Apr 30 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.17-alt1
- new version

* Tue Apr 28 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.16-alt1
- new version

* Mon Apr 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.15-alt1
- new version

* Fri Apr 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.14-alt1
- new version

* Mon Apr 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.11-alt1
- new version

* Wed Apr 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.8-alt1
- new version

* Mon Apr 13 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.5-alt1
- new version

* Fri Apr 10 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.3-alt1
- initial build for ALT Linux

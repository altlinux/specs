%define _unpackaged_files_terminate_build 1

Name:    krunvm
Version: 0.2.7
Release: alt1

Summary: Create microVMs from OCI images
License: Apache-2.0
Group:   Other
Url:     https://github.com/libkrun/krunvm
Vcs:     https://github.com/libkrun/krunvm.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: asciidoctor
BuildRequires: libkrun-devel

Requires: buildah

%description
%summary.

%prep
%setup -a1
%rust_prep

%build
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%check
%rust_test

%files
%doc *.md
%_bindir/*

%changelog
* Thu Sep 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus

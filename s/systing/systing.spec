%define _unpackaged_files_terminate_build 1

Name: systing
Version: 1.4.0
Release: alt1
Summary: A libbpf based tracer to help figure out what an application is doing. 
License: MIT
Group: System/Kernel and hardware
Url: https://github.com/josefbacik/systing

ExcludeArch: i586
Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: libelf-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: clang
BuildRequires: llvm
BuildRequires: bpftool
BuildRequires: kernel-headers-common

Requires: bpftool
Requires: kernel-headers-common

%description
%summary

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build


%install
%rust_install

%check
%rust_test 

%files
%_bindir/%name

%changelog
* Fri Apr 10 2026 Pavel Shilov <zerospirit@altlinux.org> 1.4.0-alt1
- Update to new version 1.4.0.

* Wed Feb 25 2026 Pavel Shilov <zerospirit@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

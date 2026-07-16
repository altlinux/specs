%define _unpackaged_files_terminate_build 1

Name: systing
Version: 1.11.22
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
BuildRequires: libelf-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: clang
BuildRequires: llvm
BuildRequires: bpftool

Requires: bpftool

%description
%summary

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/libbpf/blazesym.git?rev=862c2cf5d424307456322d2c68fe86c591baece2#862c2cf5"]
git = "https://github.com/libbpf/blazesym.git"
rev = "862c2cf5d424307456322d2c68fe86c591baece2"
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
%doc *.md
%_bindir/%name

%changelog
* Thu Jul 16 2026 Pavel Shilov <zerospirit@altlinux.org> 1.11.22-alt1
- Update to new version 1.11.22.

* Fri May 08 2026 Pavel Shilov <zerospirit@altlinux.org> 1.6.0-alt1
- Update to new version 1.6.0.

* Fri Apr 10 2026 Pavel Shilov <zerospirit@altlinux.org> 1.4.0-alt1
- Update to new version 1.4.0.

* Wed Feb 25 2026 Pavel Shilov <zerospirit@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

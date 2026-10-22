%define _unpackaged_files_terminate_build 1
%define rust_llvm_version %(rustc --version --verbose | awk '/^LLVM version:/ { split($3, v, "."); print v[1] "." v[2] }')

Name: bpf-linker
Version: 0.12.0
Release: alt1

Summary: BPF static linker
License: MIT OR Apache-2.0
Group: Development/Other
Url: https://github.com/aya-rs/bpf-linker

# Source-url: https://github.com/aya-rs/bpf-linker/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

ExcludeArch: i586

# bpf-linker must use the same LLVM version as the Rust toolchain.
BuildRequires: llvm%{rust_llvm_version}-devel

Requires: llvm%{rust_llvm_version}-libs

%filter_from_requires /\/usr\/lib\/llvm-%{rust_llvm_version}\/lib\(64\)\?\/libLLVM\.so\.%{rust_llvm_version}/d

%description
bpf-linker statically links BPF object files and performs optimizations
needed to target older kernels.

%prep
%setup -a1

mkdir -p .cargo
cat >.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source."git+https://github.com/Manishearth/compiletest-rs.git"]
git = "https://github.com/Manishearth/compiletest-rs.git"
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
llvm_major=%{rust_llvm_version}
llvm_major=${llvm_major%%.*}
export LLVM_PREFIX=/usr/lib/llvm-%{rust_llvm_version}
%rust_build --no-default-features --features llvm-$llvm_major

%install
install -Dm755 target/release/bpf-linker %buildroot%_bindir/bpf-linker

%files
%doc LICENSE-APACHE LICENSE-MIT README.md
%_bindir/bpf-linker

%changelog
* Wed Oct 21 2026 Boris Yumankulov <boria138@altlinux.org> 0.12.0-alt1
- initial build for ALT Sisyphus

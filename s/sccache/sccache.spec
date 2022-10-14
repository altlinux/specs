Name:    sccache
Version: 0.3.0
Release: alt1

Summary: sccache is ccache with cloud storage
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/mozilla/sccache

ExcludeArch: ppc64le %arm

Source:   %name-%version.tar

# cargo-vendor-filterer --all-features false --offline \
#  --platform x86_64-unknown-linux-gnu --exclude-crate-path zstd-sys#zstd
Source1:  vendor.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)

%description
sccache is a ccache-like compiler caching tool. It is used as a
compiler wrapper and avoids compilation when possible, storing
cached results either on local disk or in one of several cloud
storage backends.

sccache includes support for caching the compilation of C/C++
code, Rust, as well as NVIDIA's CUDA using nvcc.

%prep
%setup
%patch -p1

tar -xf %SOURCE1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%_bindir/*
%doc README.md docs

%changelog
* Wed Oct 12 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


%define _unpackaged_files_terminate_build 1
%define _customdocdir %_docdir/%name

Name:    sccache
Version: 0.8.2
Release: alt1

Summary: sccache is ccache with cloud storage
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/mozilla/sccache


Source:   %name-%version.tar

# cargo vendor-filterer  --all-features \
#   --platform=aarch64-unknown-linux-gnu \
#   --platform=armv7-unknown-linux-gnueabihf \
#   --platform=loongarch64-unknown-linux-gnu \
#   --platform=i686-unknown-linux-gnu \
#   --platform=powerpc64le-unknown-linux-gnu \
#   --platform=riscv64gc-unknown-linux-gnu \
#   --platform=x86_64-unknown-linux-gnu \
#   --exclude-crate-path zstd-sys#zstd \
#   --exclude-crate-path openssl-src#openssl

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

# use system libzstd
sed -ir 's/^zstd = \(.*\)/zstd = { version = \1, features = ["pkg-config"] }/' Cargo.toml

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build \
%if "%_pointer_size" == "32"
    --no-default-features \
%endif
    %nil

%install
%rust_install

%files
%_bindir/*
%doc README.md docs

%changelog
* Sun Oct 20 2024 Ivan A. Melnikov <iv@altlinux.org> 0.8.2-alt1
- 0.8.2
- build with default features on 64-bit platforms
  and in minimal configuration on 32-bit platforms.

* Tue Dec 13 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.3-alt1
- 0.3.3
- Restrict use of s3 feature to selected architectures,
  due to problems with building ring.

* Sun Oct 16 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt2
- Restrict use of gcs feature to build on more architectures

* Wed Oct 12 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


%define _unpackaged_files_terminate_build 1
%define _customdocdir %_docdir/%name

%ifarch x86_64 aarch64 %ix86
%def_with gcs
%def_with s3
%else
# gcs feature depends on ring crate, which is not very portable
%def_without gcs
%def_without s3
%endif

Name:    sccache
Version: 0.3.3
Release: alt1

Summary: sccache is ccache with cloud storage
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/mozilla/sccache


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
features=dist-client,redis,memcached,azure
%if_with gcs
features="$features",gcs
%endif
%if_with s3
features="$features",s3
%endif
%rust_build --no-default-features --features="$features"

%install
%rust_install

%files
%_bindir/*
%doc README.md docs

%changelog
* Tue Dec 13 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.3-alt1
- 0.3.3
- Restrict use of s3 feature to selected architectures,
  due to problems with building ring.

* Sun Oct 16 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt2
- Restrict use of gcs feature to build on more architectures

* Wed Oct 12 2022 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

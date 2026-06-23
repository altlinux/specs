
%define _unpackaged_files_terminate_build 1
%define _customdocdir %_docdir/%name

Name:    sccache
Version: 0.16.0
Release: alt1

Summary: sccache is ccache with cloud storage
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/mozilla/sccache


Source:   %name-%version.tar

# Please use .gear/update-vendor.sh to update the vendored sources
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

%rust_prep

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
* Tue Jun 23 2026 Ivan A. Melnikov <iv@altlinux.org> 0.16.0-alt1
- 0.16.0

* Wed Apr 29 2026 Ivan A. Melnikov <iv@altlinux.org> 0.15.0-alt1
- 0.15.0
- switch to using %%rust_prep to enable debuginfo

* Tue Feb 10 2026 Ivan A. Melnikov <iv@altlinux.org> 0.14.0-alt1
- 0.14.0

* Wed Jan 14 2026 Ivan A. Melnikov <iv@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Nov 24 2025 Ivan A. Melnikov <iv@altlinux.org> 0.12.0-alt1
- 0.12.0

* Fri Mar 28 2025 Ivan A. Melnikov <iv@altlinux.org> 0.10.0-alt1
- 0.10.0

* Fri Jan 24 2025 Ivan A. Melnikov <iv@altlinux.org> 0.9.1-alt1
- 0.9.1

* Wed Dec 11 2024 Ivan A. Melnikov <iv@altlinux.org> 0.9.0-alt1
- 0.9.0

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

%define _unpackaged_files_terminate_build 1

Name: chunkah
Version: 0.6.0
Release: alt1

Summary: An OCI building tool for content-based layers
# Took from https://github.com/coreos/chunkah/blob/da527a4f39d6739d956db33885d6453804fabbf8/packaging/chunkah.spec#L23-L24
License: Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND LGPL-2.1-or-later AND MIT AND Zlib AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)

Group: Other
URL: https://github.com/coreos/chunkah
VCS: https://github.com/coreos/chunkah.git

ExcludeArch: %ix86

Source: %name-%version.tar
Source10: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

%description
An OCI building tool that takes a flat rootfs and outputs a layered OCI image
with content-based layers.

%prep
%setup -a10
%autopatch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc README.md

%changelog
* Wed Jun 10 2026 Vladimir Romanov <rirusha@altlinux.org> 0.6.0-alt1
- Initial build.

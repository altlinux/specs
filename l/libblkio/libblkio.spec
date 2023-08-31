
Name: libblkio
Version: 1.3.0
Release: alt2
Summary: Block device I/O library
Group: System/Libraries
Url: https://gitlab.com/libblkio/libblkio
Source: %name-%version.tar
Patch: %name-%version.patch
License: (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND MIT AND BSD-3-Clause AND Unicode-DFS-2016

BuildRequires(pre): rpm-macros-rust rpm-macros-meson
BuildRequires: rpm-build-rust rust >= 1.56
BuildRequires: meson
BuildRequires: /usr/bin/rst2man

%description
libblkio is a library for high-performance block device I/O with
support for multi-queue devices. A C API is provided so that
applications can use the library from most programming languages.

%package devel
Summary: Development tools for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
This package contains development tools for %name.

%prep
%setup
%patch -p1
mkdir -p .cargo
cat >.cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

sed -e 's/--locked//' -i src/cargo-build.sh

%build
%meson
%meson_build

%install
%meson_install

%files
%_libdir/%name.so.*

%files devel
%doc README.rst LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%_includedir/blkio.h
%_libdir/%name.so
%_pkgconfigdir/blkio.pc
%_man3dir/blkio.3*

%changelog
* Sun Jul 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.3.0-alt2
- Updated dependencies for LoongArch support:
  + libc: v0.2.146

* Fri Apr 28 2023 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- Initial package


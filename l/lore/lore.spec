%define _unpackaged_files_terminate_build 1
# Upstream doesn't support C library versioning.
%define abiversion 0

Name: lore
Version: 0.8.6
Release: alt1

Summary: Lore is a next-generation, open source version control system
License: MIT
Group: Development/Other
Url: https://lore.org
Vcs: https://github.com/EpicGames/lore

ExcludeArch: %ix86 aarch64

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: gcc-c++

%description
Lore is an open source version control system designed for unprecedented
scalability of both data and teams. It is optimized for projects
that combine code with large binary assets, including games and entertainment,
and caters for the needs of developers and artists alike.

%package -n loreserver
Summary: Server component for the Lore version control system
Group: System/Servers

%description -n loreserver
The Lore Server provides the backend service for Lore, a centralized,
content-addressed version control system optimized for projects that
combine code with large binary assets.
Features include content-addressable storage with deduplication,
mutable branch/reference management, distributed locking for
concurrent access, a plugin system for storage backends, and an
extensible hook system for compliance and notifications.

%package -n liblore%abiversion
Summary: Shared library for the Lore version control system
Group: System/Libraries

%description -n liblore%abiversion
Lore is a centralized, content-addressed version control system that
represents repository state as Merkle trees and an immutable revision
chain, optimized for binary-first storage, deduplication, and
sparse/on-demand data hydration at scale.
This package provides the shared C library exposing Lore's full-surface
API, used as the foundation for language bindings (C/C++, C#, Rust, Go,
Python, JavaScript).

%package -n liblore-devel
Summary: Development files for liblore
Group: Development/C

%description -n liblore-devel
Header files and development symlinks for building applications and
language bindings against liblore, the C API for the Lore version
control system.

%prep
%setup -a1
%rust_prep

%build
# Not using rust_build macro: it does export RUSTFLAGS="${RUSTFLAGS} -g"
# RUSTFLAGS as an env var fully replaces build.rustflags
# from .cargo/config.toml  — this breaks --cfg tokio_unstable/uuid_unstable,
# which lore-server needs to compile. --config adds -g while keeping the
# project's own config flags intact.
cargo build --profile release-lto -j%__nprocs --offline
# Cargo doesn’t yet provide a good way to pass specific rustflags to a package.
# Passing -soname is required to generate SONAME header in output library
# as rust doesn't generate it by default.
export RUSTFLAGS="-Clink-arg=-Wl,-soname,liblore.so.%abiversion"
%rust_build -p lore

%install
install -Dm 755 target/release-lto/lore %buildroot%_bindir/lore
install -Dm 755 target/release-lto/loreserver %buildroot%_bindir/loreserver

# Install C library
install -Dm 644 target/release-lto/liblore.so "%buildroot%_libdir/liblore.so.%abiversion"
ln -sr %buildroot%_libdir/liblore.so.%abiversion %buildroot%_libdir/liblore.so

# Install API
install -Dm 644 target/release-lto/lore.h %buildroot%_includedir/lore.h

%check
# Skipping rust_test macro: even export RUSTFLAGS="${RUSTFLAGS}" with no added
# flags still counts as setting the env var, which replaces (not merges)
# build.rustflags from .cargo/config.toml — breaking --cfg tokio_unstable/
# uuid_unstable. No extra flags needed here, so just call cargo directly.
cargo test --profile release-lto -j%__nprocs --no-fail-fast

%files
%doc README.md LICENSE docs/
%_bindir/lore

%files -n loreserver
%doc lore-server/README.md
%_bindir/loreserver

%files -n liblore%abiversion
%_libdir/liblore.so.%abiversion

%files -n liblore-devel
%_includedir/lore.h
%_libdir/liblore.so

%changelog
* Tue Aug 04 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.8.6-alt1
- Initial build for Sisyphus.


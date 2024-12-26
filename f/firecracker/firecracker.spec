%def_disable check
# clib can be musl or gnu
%define clib gnu

Name: firecracker
Version: 1.10.1
Release: alt1
Summary: Virtual Machine Monitor for creating microVMs
License: Apache-2.0
Group: Emulators
Url: https://firecracker-microvm.github.io/
Source: %name-%version.tar
Patch: %name-%version.patch
Patch2: 0001-remove-aws-lc-rs.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: rust-cargo
BuildRequires: rust >= 1.35.0
%if %clib == musl
BuildRequires: musl-devel
%endif
BuildRequires: libfdt-devel
BuildRequires: clang-devel
BuildRequires: /proc

%description
Firecracker is a virtualization technology for creating and managing
multi-tenant container and function-based services.

%prep
%setup
%patch -p1
%patch2 -p1

%build
cargo build \
    --release \
    %{?_smp_mflags} \
    --offline \
    --target %_arch-unknown-linux-%clib \
    --package={cpu-template-helper,firecracker,jailer,rebase-snap,seccompiler,snapshot-editor}


%install
mkdir -p %buildroot%_bindir
install -p -m 755 target/%_arch-unknown-linux-%clib/release/{cpu-template-helper,firecracker,jailer,rebase-snap,seccompiler-bin,snapshot-editor} %buildroot%_bindir/

%check
cargo test \
    --release \
    --no-fail-fast \
    --target %_arch-unknown-linux-%clib

%files
%doc README.md
%_bindir/firecracker
%_bindir/jailer
%_bindir/cpu-template-helper
%_bindir/rebase-snap
%_bindir/seccompiler-bin
%_bindir/snapshot-editor

%changelog
* Thu Dec 26 2024 Alexander Burmatov <thatman@altlinux.org> 1.10.1-alt1
- new version 1.10.1

* Fri Dec 18 2020 Alexey Shabalin <shaba@altlinux.org> 0.23.1-alt1
- new version 0.23.1

* Fri Nov 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.23.0-alt2
- Allow FUTEX_WAIT_BITSET_PRIVATE argument to futex syscall.

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.23.0-alt1
- 0.23.0

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 0.21.0-alt1
- Initial build.

Name: rust-toolchain-common
Version: 0.1.1
Release: alt1

Summary: Common files and directories for any rust toolchain
License: ALT-Public-Domain
Group: Development/Other

Source0: produce-rust-toolchain-common-macros.sh

Requires: rust-toolchain

%description
%summary.

%package -n rpm-macros-%name
Summary: Common RPM macros to build rust toolchains
Group: Development/Other
# Not noarch since usage of _libdir and current arch.

%description -n rpm-macros-%name
%summary.

%define rust_toolchain_home %_libdir/rust-toolchains

# Rust host triple from build arch.
%ifarch %ix86
%define r_arch i686
%endif
%ifarch x86_64
%define r_arch x86_64
%endif
%ifarch aarch64
%define r_arch aarch64
%endif
%ifarch armh
%define r_arch armv7
%endif
%ifarch ppc64le
%define r_arch powerpc64le
%endif
%ifarch loongarch64
%define r_arch loongarch64
%endif
%ifarch riscv64
%define r_arch riscv64gc
%endif

%ifarch armh
%define r_abisuff eabihf
%else
%define r_abisuff %nil
%endif

%define rust_host_triple %r_arch-unknown-linux-gnu%r_abisuff

%install
mkdir -pv %buildroot%rust_toolchain_home
mkdir -pv %buildroot%_rpmmacrosdir

export RUST_TOOLCHAIN_HOME="%rust_toolchain_home"
export RUST_HOST_TRIPLE="%rust_host_triple"
%SOURCE0 > %buildroot%_rpmmacrosdir/rust-toolchain

%files
%rust_toolchain_home

%files -n rpm-macros-%name
%_rpmmacrosdir/rust-toolchain

%changelog
* Thu Mar 26 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.1.1-alt1
- Fix macros subpackage being arch independent.

* Wed Mar 18 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.1.0-alt1
- Initial build.

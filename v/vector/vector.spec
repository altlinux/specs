%global _unpackaged_files_terminate_build 1

Name: vector
Version: 0.55.0
Release: alt1

Summary: A lightweight and ultra-fast tool for building observability pipelines
License: MPL-2.0
Group: Monitoring
Url: https://vector.dev/
Vcs: https://github.com/vectordotdev/vector.git

# https://github.com/briansmith/ring not support ppc64le
# 32bit can not build - (signal: 6, SIGABRT: process abort signal)
ExcludeArch: %ix86 %arm %mips32 ppc ppc64le

Source: %name-%version.tar
Source1: vendor.tar
Source2: vector.sysconfig
Source4: vector.init
Source5: config.toml
Patch: systemd-unit-alt.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust >= 1.80.0
BuildRequires: libclang21
BuildRequires: rpm-build-rust cmake gcc-c++ clang python3 git-core
BuildRequires: libssl-devel libsasl2-devel zlib-devel liblz4-devel libzstd-devel rapidjson
BuildRequires: librdkafka-devel
BuildRequires: perl(Pod/Usage.pm) perl(IPC/Cmd.pm) perl(Time/Piece.pm) protobuf-compiler
BuildRequires: /proc
BuildRequires: cargo-vendor-checksum

%description
Vector is a high-performance, end-to-end (agent & aggregator) observability
data pipeline that puts you in control of your observability data.
Collect, transform, and route all your logs, metrics, and traces to any vendors
you want today and any other vendors you may want tomorrow.
Vector enables dramatic cost reduction, novel data enrichment,
and data security where you need it, not where it is most convenient for your vendors.
Additionally, it is open source and up to 10x faster than every alternative in the space.

%prep
%setup -a1
%autopatch -p1

# This is necessary after updating rust from version 1.80.0 to 1.81.0 to avoid errors.
sed -i '/#!\[deny(warnings)\]/d'\
                      src/lib.rs\
		      lib/file-source/src/lib.rs\
		      lib/vector-config/src/lib.rs\
		      #
cat %SOURCE5 >> %_builddir/%name-%version/.cargo/config.toml

%build
cargo-vendor-checksum --ignore-missing --all

export CFLAGS="-O3 -DPIC -fPIC"
export RUST_BACKTRACE=1
#export CARGO_FEATURE_DYNAMIC_LINKING=1
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=1 -A mismatched_lifetime_syntaxes --cfg rustix_use_libc"
%rust_build

%install
%rust_install

install -Dm 0644 config/vector.yaml %buildroot%_sysconfdir/vector/vector.yaml
install -Dm 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/vector
install -Dm 0644 distribution/systemd/vector.service %buildroot%_unitdir/vector.service
install -Dm 0755 %SOURCE4 %buildroot%_initdir/vector
install -d -m 0770 %buildroot%_sharedstatedir/vector

%pre
groupadd -r -f vector
useradd -M -r -d %_sharedstatedir/vector -s /bin/false \
    -c "Vector observability data router" -g vector vector >/dev/null 2>&1 || :
usermod -a -G systemd-journal vector >/dev/null 2>&1 || :
usermod -a -G systemd-journal-remote vector >/dev/null 2>&1 || :
usermod -a -G adm vector >/dev/null 2>&1 || :

%post
%post_service vector

%preun
%preun_service vector

%files
%doc README.md config/examples
%_bindir/*
%_unitdir/vector.service
%_initdir/vector
%dir %_sysconfdir/vector
%config(noreplace) %_sysconfdir/vector/vector.yaml
%config(noreplace) %_sysconfdir/sysconfig/vector
%dir %attr(0770, root, vector) %_sharedstatedir/vector

%changelog
* Thu May 19 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.55.0-alt1
- New version.

* Sat Mar 28 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.54.0-alt1
- New version.

* Mon Feb 16 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.53.0-alt1
- New version.

* Mon Jan 26 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.52.0-alt1
- New version.

* Sat Oct 18 2025 Ilya Muhamadeev <nicourced@altlinux.org> 0.50.0-alt1
- New version.

* Sat Sep 28 2025 Ilya Muhamadeev <nicourced@altlinux.org> 0.49.0-alt1
- New version.

* Fri Aug 08 2025 Ilya Muhamadeev <nicourced@altlinux.org> 0.48.0-alt1
- New version.
- Get rid of cumulative patch.
- Fix systemd unit (closes: 55217):
  + Add environment variables to command calls.
  + Change EnvironmentFile path.

* Tue Jan 14 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.44.0-alt1
- New version.
- Use an upstream service.

* Sun Nov 17 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.42.0-alt2
- Allow warnings in the vector lib to avoid errors with new rust.
- Transfer to another package build scheme.

* Wed Oct 30 2024 Alexey Shabalin <shaba@altlinux.org> 0.42.0-alt1
- 0.42.0

* Fri Aug 23 2024 Alexey Shabalin <shaba@altlinux.org> 0.40.0-alt1
- 0.40.0

* Fri Aug 23 2024 Alexey Shabalin <shaba@altlinux.org> 0.36.1-alt1
- 0.36.1

* Thu Apr 06 2023 Alexey Shabalin <shaba@altlinux.org> 0.28.1-alt1
- 0.28.1

* Sat Nov 12 2022 Alexey Shabalin <shaba@altlinux.org> 0.25.1-alt1
- 0.25.1.

* Sun Oct 16 2022 Alexey Shabalin <shaba@altlinux.org> 0.24.2-alt1
- 0.24.2.
- Add vector-aggregator systemd unit.

* Fri Dec 10 2021 Alexey Shabalin <shaba@altlinux.org> 0.18.1-alt1
- Initial build.


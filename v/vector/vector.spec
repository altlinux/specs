%global _unpackaged_files_terminate_build 1

Name: vector
Summary: A lightweight and ultra-fast tool for building observability pipelines
Version: 0.25.1
Release: alt1
License: MPL-2.0
Group: Monitoring
Url: https://vector.dev/
Vcs: https://github.com/vectordotdev/vector.git
Source: %name-%version.tar
Source2: vector.sysconfig
Source3: vector.service
Source4: vector.init
Patch: %name-%version.patch

# https://github.com/briansmith/ring not support ppc64le
# 32bit can not build - (signal: 6, SIGABRT: process abort signal)
ExcludeArch: %ix86 %arm %mips32 ppc ppc64le

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust >= 1.64.0
BuildRequires: rpm-build-rust cmake gcc-c++ clang python3
BuildRequires: libssl-devel libsasl2-devel zlib-devel liblz4-devel libzstd-devel rapidjson
BuildRequires: perl(Pod/Usage.pm) protobuf-compiler
BuildRequires: /proc

%description
Vector is a high-performance, end-to-end (agent & aggregator) observability
data pipeline that puts you in control of your observability data.
Collect, transform, and route all your logs, metrics, and traces to any vendors
you want today and any other vendors you may want tomorrow.
Vector enables dramatic cost reduction, novel data enrichment,
and data security where you need it, not where it is most convenient for your vendors.
Additionally, it is open source and up to 10x faster than every alternative in the space.

%prep
%setup
%patch -p1

%build
export CFLAGS="-g0 -O3 -DPIC -fPIC"
export RUST_BACKTRACE=1
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=0 -D warnings"
%rust_build --no-default-features --features default

%install
%rust_install

install -Dm 0644 config/vector.toml %buildroot%_sysconfdir/%name/%name.toml
install -Dm 0644 config/aggregator/vector.yaml %buildroot%_sysconfdir/%name/aggregator/%name.toml
install -Dm 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm 0644 distribution/systemd/vector-aggregator.service %buildroot%_unitdir/%name-aggregator.service
install -Dm 0755 %SOURCE4 %buildroot%_initdir/%name
install -d -m 0770 %buildroot%_sharedstatedir/%name

%pre
groupadd -r -f %name
useradd -M -r -d %_sharedstatedir/%name -s /bin/false \
    -c "Vector observability data router" -g %name %name >/dev/null 2>&1 || :
usermod -a -G systemd-journal %name >/dev/null 2>&1 || :
usermod -a -G systemd-journal-remote %name >/dev/null 2>&1 || :
usermod -a -G adm %name >/dev/null 2>&1 || :

%post
%post_service %name
%post_service %name-aggregator

%preun
%preun_service %name
%preun_service %name-aggregator


%files
%doc README.md config/examples
%_bindir/*
%_unitdir/%name.service
%_unitdir/%name-aggregator.service
%_initdir/%name
%config(noreplace) %_sysconfdir/%name/%name.toml
%config(noreplace) %_sysconfdir/%name/aggregator/%name.toml
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(0770, root, %name) %_sharedstatedir/%name

%changelog
* Sat Nov 12 2022 Alexey Shabalin <shaba@altlinux.org> 0.25.1-alt1
- 0.25.1.

* Sun Oct 16 2022 Alexey Shabalin <shaba@altlinux.org> 0.24.2-alt1
- 0.24.2.
- Add vector-aggregator systemd unit.

* Fri Dec 10 2021 Alexey Shabalin <shaba@altlinux.org> 0.18.1-alt1
- Initial build.


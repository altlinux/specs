%define _unpackaged_files_terminate_build 1

Name: rustfs
Version: 1.0.0
Release: alt2.alpha.60
Summary: High-performance distributed object storage for MinIO alternative
Group: System/Servers
License: Apache-2.0
Url: https://github.com/rustfs/rustfs
ExcludeArch: i586
Source0: %name-%version.tar
Source1: rustfs
Source2: rustfs.service

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%ifarch loongarch64 riscv64
# need to rebuild aws-lc-sys
BuildRequires: cmake rust-bindgen clang-devel
%endif

%description
RustFS is a high-performance distributed object storage software built
using Rust, one of the most popular languages worldwide. Along with MinIO,
it shares a range of advantages such as simplicity, S3 compatibility,
open-source nature, support for data lakes, AI, and big data. Furthermore,
it has a better and more user-friendly open-source license in comparison
to other storage systems, being constructed under the Apache license.
As Rust serves as its foundation, RustFS provides faster speed and safer
distributed features for high-performance object storage.

%prep
%setup
%rust_prep

%build
%rust_build -p %name

%install
%rust_install

mkdir -p -- \
    %buildroot%_sharedstatedir/%name \
    %buildroot%_logdir/%name

install -pD %SOURCE1 %buildroot%_sysconfdir/%name/%name
install -pD -m644 %SOURCE2 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -r -g _%name -M -d %_sharedstatedir/%name -s /dev/null _%name > /dev/null 2>&1 ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc LICENSE
%doc *.md
%config(noreplace) %attr(640, root, _%name) %_sysconfdir/%name/%name
%dir %attr(770, root, _%name) %_sharedstatedir/%name
%dir %attr(770, root, _%name) %_logdir/%name
%_unitdir/%name.service
%_bindir/%name

%changelog
* Tue Sep 30 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.0.0-alt2.alpha.60
- new version

* Fri Sep 12 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt2.alpha.49
- NMU: Fix FTBFS on loongarch64

* Wed Sep 10 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.0.0-alt1.alpha.49
- initial build

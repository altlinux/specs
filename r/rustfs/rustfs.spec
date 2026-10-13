%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: rustfs
Version: 1.0.0
Release: alt3
Summary: Open-source S3-compatible high-performance object storage
Group: System/Servers
License: Apache-2.0
Url: https://rustfs.com
Vcs: https://github.com/rustfs/rustfs.git
ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar
Source2: %name-console.tar
Source3: %name.env
Source4: %name.service

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: protobuf-compiler

%ifarch loongarch64 riscv64
# need to rebuild aws-lc-sys
BuildRequires: cmake rust-bindgen clang-devel
%endif

%description
RustFS is an open-source, S3-compatible high-performance object storage
system supporting migration and coexistence with other S3-compatible
platforms such as MinIO and Ceph.

It has a scalable and fault-tolerant distributed architecture suitable
for large-scale deployments and is optimized for data lakes, AI and big
data workloads.

%prep
%setup -a1
tar -xf %SOURCE2 -C rustfs/static --strip-components=1
%rust_prep

%build
%rust_build -p %name

%install
%rust_install

mkdir -p %buildroot%_sharedstatedir/%name

install -pD %SOURCE3 %buildroot%_sysconfdir/%name/%name
install -pD -m644 %SOURCE4 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name ||:
useradd -r -g _%name -c 'RustFS object storage' \
	-d %_sharedstatedir/%name -s /dev/null _%name >/dev/null 2>&1 ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc LICENSE README.md CHANGELOG.md
%dir %_sysconfdir/%name
%config(noreplace) %attr(640, root, _%name) %_sysconfdir/%name/%name
%dir %attr(770, root, _%name) %_sharedstatedir/%name
%_unitdir/%name.service
%_bindir/%name

%changelog
* Thu Oct 01 2026 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.0.0-alt3
- new version (first stable release)
- update the web console to v0.1.27
- sync the systemd unit with upstream

* Wed Jun 24 2026 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.0.0-alt2.beta.8
- new version

* Tue Sep 30 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.0.0-alt2.alpha.60
- new version

* Fri Sep 12 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt2.alpha.49
- NMU: Fix FTBFS on loongarch64

* Wed Sep 10 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.0.0-alt1.alpha.49
- initial build

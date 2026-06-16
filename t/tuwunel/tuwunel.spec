%define _unpackaged_files_terminate_build 1
%def_disable check

Name:    tuwunel
Version: 1.7.1
Release: alt1
Summary: High Performance Matrix Homeserver in Rust!
License: Apache-2.0
Group:   System/Servers
URL:     https://github.com/matrix-construct/tuwunel
VCS:     https://github.com/matrix-construct/tuwunel.git

ExcludeArch: %ix86

Source:  %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
Patch1:  %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: liburing-devel
BuildRequires: unzip
BuildRequires: glibc-devel
BuildRequires: clang21.1 libclang21
BuildRequires: gcc-c++

%description
Tuwunel is a featureful Matrix homeserver you can use instead of Synapse with
your favorite client, bridge or bot. It is written entirely in Rust
to be a scalable, low-cost, enterprise-ready, community-driven alternative,
fully implementing the Matrix Specification for all but the most niche uses.

%prep
%setup -a1
%patch1 -p1
%rust_prep
cat %SOURCE2 >> .cargo/config.toml
sed 's|/usr/sbin/nologin|/sbin/nologin|' -i rpm/sysusers

%build
%rust_build
# Pre-compile test binaries so %check can run them without recompilation.
%if_enabled check
%rust_test --no-run --workspace --offline
%endif

%install
%rust_install -t %_sbindir
install -Dm 644 rpm/tuwunel.service %buildroot%_unitdir/%name.service
install -Dm 644 rpm/sysusers %buildroot%_sysusersdir/%name.conf
install -Dm 644 %name-example.toml %buildroot%_sysconfdir/%name/%name.toml
mkdir -p %buildroot%_localstatedir/%name

%check
export TUWUNEL_DATABASE_PATH=/tmp/tuwunel-smoketest.db
%rust_test --workspace --exclude tuwunel

%pre
groupadd -r -f %name
useradd -r -g %name -c 'tuwunel Matrix homeserver' -d %_localstatedir/%name -s /sbin/nologin %name >/dev/null 2>&1 ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%_sbindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %attr(640,root,%name) %_sysconfdir/%name/%name.toml
%dir %attr(755,%name,%name) %_localstatedir/%name
%doc LICENSE README.md

%changelog
* Tue Jun 16 2026 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- updated from 1.7.0 to 1.7.1

* Fri May 22 2026 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- updated from 1.6.1 to 1.7.0
- Fix create system user/group in %%pre via groupadd/useradd (ALT #59243).

* Tue May 05 2026 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- 1.6.1.

* Fri Mar 20 2026 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt4
- Add support MAS (PR#342) realy.
- Not add tuwunel user to uucp group.
- Add post scrips for restart service after upgrade.

* Thu Mar 19 2026 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt3
- Removed read access for everyone from the configuration file
  because it may contain secrets.
- Add support MAS (PR#342).

* Wed Mar 18 2026 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt2
- Add execute test in %%check section.
- Change owner of conf dir and file to root.
- Fix build debuginfo package.

* Mon Mar 16 2026 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt1
- Updated from 1.5.0 to 1.5.1 with security fixes.

* Wed Feb 18 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 1.5.0-alt1
- Initial build.

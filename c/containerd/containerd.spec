%global import_path github.com/containerd/containerd

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%global commit      78f51771157abb6c9ed224c22013cdf09962315d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		containerd
Version:	1.6.13
Release:	alt1
Summary:	A daemon to control runC

Group:		Development/Other
License:	Apache-2.0
URL:		https://%import_path

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source2: %name.init
Source3: %name.limits
Source4: config.toml

Patch1: %name-1.6.1-alt-use-vendor-mod-for-man-pages.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: libbtrfs-devel
BuildRequires: libseccomp-devel

Provides: docker-%name = %version-%release
Obsoletes: docker-%name <= 1.0.0

Requires: runc

%description
containerd is a daemon to control runC, built for performance and density.
containerd leverages runC's advanced features such as seccomp and user namespace
support as well as checkpoint and restore for cloning and live migration of containers.

%prep
%setup -q
%autopatch -p1
sed -i 's|/usr/local/bin/containerd|/usr/bin/containerd|g' containerd.service

%build
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$PWD"

mkdir -p src/github.com/containerd
ln -rTsf $PWD src/github.com/containerd/containerd
pushd src/github.com/containerd/containerd
make VERSION=v%version REVISION=%shortcommit binaries man
popd

%install
install -d -m 0755 %buildroot%_bindir
install -p -m 0755 bin/* %buildroot%_bindir/

install -D -p -m 0644 man/containerd.8 %buildroot%_man8dir/containerd.8
install -D -p -m 0644 man/containerd-config.8 %buildroot%_man8dir/containerd-config.8
install -D -p -m 0644 man/ctr.8 %buildroot%_man8dir/ctr.8
install -D -p -m 0644 man/containerd-config.toml.5 %buildroot%_man5dir/containerd-config.toml.5

install -D -p -m 0644 containerd.service %buildroot%_unitdir/%name.service
install -D -p -m 0755 %SOURCE2 %buildroot%_initdir/%name
install -D -p -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/limits.d/%name
install -p -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/%name/config.toml

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %_sysconfdir/%name/config.toml
%_sysconfdir/sysconfig/limits.d/%name
%_bindir/*
%_initdir/%name
%_unitdir/%name.service
%_man5dir/*
%_man8dir/*

%changelog
* Mon Dec 19 2022 Vladimir Didenko <cow@altlinux.org> 1.6.13-alt1
- 1.6.13

* Fri Oct 28 2022 Vladimir Didenko <cow@altlinux.org> 1.6.9-alt1
- 1.6.9

* Mon Sep 12 2022 Vladimir Didenko <cow@altlinux.org> 1.6.8-alt1
- 1.6.8

* Wed Jun 8 2022 Vladimir Didenko <cow@altlinux.org> 1.6.6-alt1
- 1.6.6 (Fixes: CVE-2022-31030)

* Wed Jun 8 2022 Vladimir Didenko <cow@altlinux.org> 1.6.5-alt1
- 1.6.5

* Thu May 12 2022 Vladimir Didenko <cow@altlinux.org> 1.6.4-alt1
- 1.6.4

* Mon Mar 28 2022 Vladimir Didenko <cow@altlinux.org> 1.6.2-alt1
- 1.6.2 (Fixes: CVE-2022-24769)

* Fri Mar 11 2022 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- 1.6.1 (Fixes: CVE-2022-23648)

* Thu Jan 27 2022 Alexey Shabalin <shaba@altlinux.org> 1.5.9-alt1
- 1.5.9. (Fixes: CVE-2021-43816)
- Install upstream systemd unit file.
- Build and install man pages.

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.12-alt2
- Update changelog.

* Wed Dec 1 2021 Vladimir Didenko <cow@altlinux.org> 1.4.12-alt1
- 1.4.12 (Fixes: CVE-2021-41190)

* Wed Oct 6 2021 Vladimir Didenko <cow@altlinux.org> 1.4.11-alt1
- 1.4.11 (Fixes: CVE-2021-41103)

* Thu Aug 5 2021 Vladimir Didenko <cow@altlinux.org> 1.4.9-alt1
- 1.4.9 (Fixes: CVE-2021-32760)

* Fri Jun 18 2021 Vladimir Didenko <cow@altlinux.org> 1.4.6-alt1
- 1.4.6 (Fixes: CVE-2021-30465)

* Thu Mar 11 2021 Vladimir Didenko <cow@altlinux.org> 1.4.4-alt1
- 1.4.4 (Fixes: CVE-2021-21334)

* Sat Feb 20 2021 Vladimir Didenko <cow@altlinux.org> 1.4.3-alt2
- Fix build with golang 1.16

* Fri Jan 22 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.3-alt1
- 1.4.3 (Fixes: CVE-2020-15257)

* Fri Jan 22 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.9-alt1
- 1.3.9 (Fixes: CVE-2020-15257)

* Fri Dec 4 2020 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 1.3.7-alt1
- 1.3.7

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 1.3.6-alt2
- Add previously missed binaries

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 1.3.6-alt1
- 1.3.6

* Fri May 29 2020 Vladimir Didenko <cow@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Feb 18 2020 Vladimir Didenko <cow@altlinux.org> 1.3.3-alt1
- 1.3.3
- Fixes CVE-2019-16884
- Fix license name

* Thu Oct 10 2019 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Sep 12 2019 Vladimir Didenko <cow@altlinux.org> 1.2.9-alt1
- 1.2.9

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 1.2.7-alt1
- 1.2.7

* Sat Mar 16 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.5-alt1
- 1.2.5

* Wed Feb 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.3-alt1
- Snapshot of release/1.2 branch
- Fixes CVE-2019-5736.

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- New version (for docker 18.09.1-ce)

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- New version (for docker 18.09.0-ce)

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- New version (for docker 18.06.0-ce)

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- New version (for docker 18.03.1-ce)

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- New version (for docker 18.03.0-ce)

* Tue Feb 6 2018 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1.1
- Fix provides/obsoletes

* Tue Feb 6 2018 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- New version (for docker 18.02.0-ce)

* Mon Jan 23 2017 Vladimir Didenko <cow@altlinux.org> 0.2.5-alt1.git2a5e70cb
- New version

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.org> 0.2.2-alt1.git0ac3cd1b
- New version

* Mon Apr 25 2016 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1.git0e9e24c6
- First build for ALTLinux.

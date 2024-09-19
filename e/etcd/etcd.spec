%global import_path github.com/etcd-io/etcd

%define etcd_group etcd
%define etcd_user  etcd

%global _unpackaged_files_terminate_build 1

Name:    etcd
Version: 3.5.15
Release: alt1
Summary: A highly-available key value store for shared configuration
Group:   System/Servers

URL:     https://etcd.io/
License: Apache-2.0

Source0: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21

%description
Etcd is a distributed key value store that provides a reliable way to store data
across a cluster of machines. Etcd gracefully handles leader elections during network
partitions and will tolerate machine failure, including the leader.

%prep
%setup -q

for d in contrib etcdctl etcdutl pkg raft hack security; do
mv $d/README.md README-$d.md
done
mv etcdctl/READMEv2.md READMEv2-etcdctl.md
mv client/v2/README.md README-clientv2.md
mv client/v3/README.md README-clientv3.md

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X go.etcd.io/etcd/api/v3/version.GitSHA=%release"

%golang_prepare

cd .build/src/%import_path

%golang_build \
    server \
    etcdctl \
    etcdutl \
    tools/etcd-dump-db \
    tools/etcd-dump-logs \
    tools/etcd-dump-metrics \
#

%install
export BUILDDIR="$PWD/.build"

%golang_install

mkdir -p -- \
    %buildroot%_sbindir \
    %buildroot%_unitdir \
    %buildroot%_sysconfdir/%name \
    %buildroot%_sharedstatedir/%name \
#

mv -f -- %buildroot%_bindir/server %buildroot%_sbindir/%name

sed \
    -e 's,@USER@,%etcd_user,g' \
    -e 's,@STATEDIR@,%_sharedstatedir/%name,g' \
    -e 's,@SYSCONFDIR@,%_sysconfdir/%name,g' \
    -e 's,@BINDIR@,%_sbindir,g' \
    < rpm/etcd.service > %buildroot%_unitdir/%name.service

install -D -p -m 0644 rpm/etcd.conf    %buildroot%_sysconfdir/%name/%name.conf

# remove unused files
rm -rf -- %buildroot/%go_root

%pre
groupadd -r -f %etcd_group
useradd -r -g %etcd_group -d /dev/null -s /dev/null -n %etcd_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md etcd.conf.yml.sample
%doc README-*.md READMEv2-etcdctl.md
%dir %attr(770,%etcd_user,%etcd_group) %_sharedstatedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_bindir/*
%_sbindir/*
%_unitdir/%name.service

%changelog
* Wed Sep 18 2024 Alexander Stepchenko <geochip@altlinux.org> 3.5.15-alt1
- 3.5.12 -> 3.5.15 (Fixes: CVE-2023-45288, CVE-2024-24786)

* Mon Feb 05 2024 Alexey Shabalin <shaba@altlinux.org> 3.5.12-alt1
- 3.5.12

* Sat May 27 2023 Alexey Shabalin <shaba@altlinux.org> 3.5.9-alt1
- 3.5.9 (Fixes: CVE-2023-32082).

* Fri Apr 14 2023 Alexey Shabalin <shaba@altlinux.org> 3.5.8-alt1
- 3.5.8 (Fixes: CVE-2021-28235).

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.1-alt1
- 3.5.1

* Thu Jan 27 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.18-alt1
- 3.4.18

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.15-alt2
- Update changelog.

* Thu Oct 28 2021 Paul Wolneykien <manowar@altlinux.org> 3.4.9-alt1.1
- Fix building on x86_64.

* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.15-alt1
- 3.4.15

* Fri Jan 15 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.14-alt1
- 3.4.14

* Sat Sep 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.13-alt1
- 3.4.13 (Fixes: CVE-2020-15106, CVE-2020-15112, CVE-2020-15113, CVE-2020-15114,
                 CVE-2020-15115, CVE-2020-15136).

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.9-alt1
- 3.4.9.

* Tue Apr 28 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt2
- add post_service and preun_service.

* Sun Apr 26 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt1
- 3.4.7 (Fixes: CVE-2018-1098, CVE-2018-1099, CVE-2018-16886).

* Tue Aug 08 2017 Alexey Gladkov <legion@altlinux.ru> 3.2.5-alt1
- First build for ALTLinux.

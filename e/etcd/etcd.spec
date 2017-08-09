%global import_path github.com/coreos/etcd
%global commit d0d1a87aa96ae14914751d42264262cb69eda170
%global abbrev %(c=%{commit}; echo ${c:0:8})

%define etcd_group etcd
%define etcd_user  etcd

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:    etcd
Version: 3.2.5
Release: alt1
Summary: A highly-available key value store for shared configuration
Group:   System/Servers

URL:     https://coreos.com/etcd/docs/latest/
License: ASL 2.0

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Etcd is a distributed key value store that provides a reliable way to store data
across a cluster of machines. Etcd gracefully handles leader elections during network
partitions and will tolerate machine failure, including the leader.

%prep
%setup -q

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X %import_path/version.GitSHA=%abbrev"

%golang_prepare

cd .build/src/%import_path
%golang_build \
	cmd/etcd \
	cmd/etcdctl \
	cmd/tools/etcd-dump-db \
	cmd/tools/etcd-dump-logs \
#

%install
export BUILDDIR="$PWD/.build"

%golang_install

mkdir -p -- \
	%buildroot/%_sbindir \
	%buildroot/%_unitdir \
	%buildroot/%_sysconfdir/%name \
	%buildroot/%_sharedstatedir/%name \
#

mv -f -- %buildroot/%_bindir/%name %buildroot/%_sbindir/%name

cat > %buildroot/%_bindir/etcdctl3 <<'EOF'
#!/bin/sh -efu
export ETCDCTL_API=3
exec %_bindir/etcdctl ${1:+"$@"}
EOF
chmod +x -- %buildroot/%_bindir/etcdctl3

sed \
	-e 's,@USER@,%etcd_user,g' \
	-e 's,@STATEDIR@,%_sharedstatedir/%name,g' \
	-e 's,@SYSCONFDIR@,%_sysconfdir/%name,g' \
	-e 's,@BINDIR@,%_sbindir,g' \
	< rpm/etcd.service > %buildroot/%_unitdir/%name.service

install -D -p -m 0644 rpm/etcd.conf    %buildroot/%_sysconfdir/%name/%name.conf

# remove unused files
rm -rf -- %buildroot/%_libdir

%pre
/usr/sbin/groupadd -r -f %etcd_group
/usr/sbin/useradd -r -g %etcd_group -d /dev/null -s /dev/null -n %etcd_user >/dev/null 2>&1 ||:

%files
%dir %attr(770,%etcd_user,%etcd_group) %_sharedstatedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_bindir/*
%_sbindir/*
%_unitdir/%name.service

%changelog
* Tue Aug 08 2017 Alexey Gladkov <legion@altlinux.ru> 3.2.5-alt1
- First build for ALTLinux.

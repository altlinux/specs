%global import_path github.com/docker/containerd
%global commit 0e9e24c6470321f134ab2484f921e2c3c9382022
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		containerd
Version:	0.2.0
Release:	alt1.git%abbrev
Summary:	A daemon to control runC

Group:		Development/Other
License:	Apache 2.0
URL:		https://%import_path

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.limits

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
containerd is a daemon to control runC, built for performance and density.
containerd leverages runC's advanced features such as seccomp and user namespace
support as well as checkpoint and restore for cloning and live migration of containers.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare
make

%install
mkdir -p -- \
	%buildroot/%_sbindir \
	%buildroot/%_initdir \
	%buildroot/%_unitdir \
	%buildroot/%_sysconfdir/sysconfig/limits.d

cat > %buildroot/%_sysconfdir/sysconfig/%name<<EOF
# /etc/sysconfig/contrainerd
# Modify these options if you want to change the way the containerd daemon runs
OPTIONS=""
EOF
cp -a -- bin/*    %buildroot/%_sbindir
cp -a -- %SOURCE1 %buildroot/%_unitdir/%name.service
cp -a -- %SOURCE2 %buildroot/%_initdir/%name
cp -a -- %SOURCE3 %buildroot/%_sysconfdir/sysconfig/limits.d/%name

%files
%_sysconfdir/sysconfig/%name
%_sysconfdir/sysconfig/limits.d/%name
%_sbindir/*
%_initdir/%name
%_unitdir/%name.service

%changelog
* Mon Apr 25 2016 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1.git0e9e24c6
- First build for ALTLinux.

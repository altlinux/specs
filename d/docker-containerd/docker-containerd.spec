%global import_path github.com/docker/containerd
%global commit 422e31ce907fd9c3833a38d7b8fdd023e5a76e73
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		docker-containerd
Version:	0.2.3
Release:	alt1.git%abbrev
Summary:	A daemon to control docker-runc.

Group:		Development/Other
License:	Apache 2.0
URL:		https://%import_path

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.limits

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Conflicts: docker-io <= 17.03.0

%description
docker-containerd (docker version of containerd) is a daemon to control
docker-runc (docker version of runc), built for performance and density.
containerd leverages runC's advanced features such as seccomp and user namespace
support as well as checkpoint and restore for cloning and live migration of
containers.

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
	%buildroot/%_bindir \
	%buildroot/%_initdir \
	%buildroot/%_unitdir \
	%buildroot/%_sysconfdir/sysconfig/limits.d

cat > %buildroot/%_sysconfdir/sysconfig/%name<<EOF
# /etc/sysconfig/docker-contrainerd
# Modify these options if you want to change the way the docker-containerd daemon runs
OPTIONS=""
EOF
cp -a -- bin/containerd    %buildroot/%_bindir/docker-containerd
cp -a -- bin/containerd-shim    %buildroot/%_bindir/docker-containerd-shim
cp -a -- bin/ctr    %buildroot/%_bindir/docker-containerd-ctr
cp -a -- %SOURCE1 %buildroot/%_unitdir/%name.service
cp -a -- %SOURCE2 %buildroot/%_initdir/%name
cp -a -- %SOURCE3 %buildroot/%_sysconfdir/sysconfig/limits.d/%name

%post
%post_service docker-containerd

%preun
%preun_service docker-containerd

%files
%_sysconfdir/sysconfig/%name
%_sysconfdir/sysconfig/limits.d/%name
%_bindir/*
%_initdir/%name
%_unitdir/%name.service

%changelog
* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 0.2.3-alt1.git422e31ce
- New version

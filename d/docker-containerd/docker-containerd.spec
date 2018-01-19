%global import_path github.com/containerd/containerd
%global commit 89623f28b87a6004d4b785663257362d1658a729
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		docker-containerd
Version:	1.0.0
Release:	alt2.git%abbrev
Summary:	A daemon to control docker-runc.

Group:		Development/Other
License:	Apache 2.0
URL:		https://%import_path

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.limits
Source4: config.toml
Patch1:  %name-1.0.0-default-paths.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libbtrfs-devel

Conflicts: docker-io <= 17.03.0

%description
docker-containerd (docker version of containerd) is a daemon to control
docker-runc (docker version of runc), built for performance and density.
containerd leverages runC's advanced features such as seccomp and user namespace
support as well as checkpoint and restore for cloning and live migration of
containers.

%prep
%setup -q
%patch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare
# TODO: Looks ugly. Definetly should be fixed.
rm -fr "$BUILDDIR/src/$IMPORT_PATH/vendor"
cp -alv -- vendor/* "$BUILDDIR/src"
make

%install
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%_initdir \
	%buildroot/%_unitdir \
	%buildroot/%_sysconfdir/sysconfig/limits.d

cp -a -- bin/containerd    %buildroot/%_bindir/docker-containerd
cp -a -- bin/containerd-shim    %buildroot/%_bindir/docker-containerd-shim
cp -a -- bin/ctr    %buildroot/%_bindir/docker-containerd-ctr
cp -a -- %SOURCE1 %buildroot/%_unitdir/%name.service
cp -a -- %SOURCE2 %buildroot/%_initdir/%name
cp -a -- %SOURCE3 %buildroot/%_sysconfdir/sysconfig/limits.d/%name
install -p -D -m 644 %SOURCE4 %{buildroot}%{_sysconfdir}/%{name}/config.toml

%post
%post_service docker-containerd

%preun
%preun_service docker-containerd

%files
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%_sysconfdir/sysconfig/limits.d/%name
%_bindir/*
%_initdir/%name
%_unitdir/%name.service

%changelog
* Mon Jan 15 2018 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt2.git89623f28
- New version

* Fri Dec 1 2017 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1.git992280e8
- New version

* Tue May 16 2017 Vladimir Didenko <cow@altlinux.org> 0.2.3-alt2.git9048e5e5
- New version

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 0.2.3-alt1.git422e31ce
- New version

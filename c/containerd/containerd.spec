%global import_path github.com/containerd/containerd
%global commit 9b55aab90508bd389d7654c4baf173a981477d55
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		containerd
Version:	1.0.1
Release:	alt1.1
Summary:	A daemon to control runC

Group:		Development/Other
License:	Apache 2.0
URL:		https://%import_path

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.limits
Source4: config.toml

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libbtrfs-devel

Provides: docker-%name = %version-%release
Obsoletes: docker-%name <= 1.0.0

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

cp -a -- bin/%name    %buildroot/%_bindir/%name
cp -a -- bin/%name-shim    %buildroot/%_bindir/%name-shim
cp -a -- bin/ctr    %buildroot/%_bindir/%name-ctr
cp -a -- %SOURCE1 %buildroot/%_unitdir/%name.service
cp -a -- %SOURCE2 %buildroot/%_initdir/%name
cp -a -- %SOURCE3 %buildroot/%_sysconfdir/sysconfig/limits.d/%name
install -p -D -m 644 %SOURCE4 %{buildroot}%{_sysconfdir}/%{name}/config.toml

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%_sysconfdir/sysconfig/limits.d/%name
%_bindir/*
%_initdir/%name
%_unitdir/%name.service

%changelog
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

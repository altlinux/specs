%global import_path github.com/subuk/vmango
%global commit 63ed62d7c71c31d071f05d3f18d87449483a850b

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Summary: KVM virtual machines management
Name: vmango
Version: 0.7.0
Release: alt1
URL: https://vmango.org
License: GPLv3
Group: Networking/WWW

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64 ppc64le
BuildRequires(pre): rpm-build-golang
BuildRequires: go-bindata
BuildRequires: libvirt-devel >= 1.2.0

%define userid %name
%define groupid %name
%define home_dir %_localstatedir/%name

%description
Web interface and API for KVM virtual machines management

%prep
%setup -q
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux
export GOFLAGS="-mod=vendor"

%make VERSION=$VERSION

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"

mkdir -p %buildroot%_bindir
pushd .gopath/src/%import_path

%makeinstall_std
mkdir -p %buildroot{%_unitdir,%home_dir}
install -p -m 644 rpm/vmango.service %buildroot%_unitdir/vmango.service
popd

#Cleanup
rm -rf -- %buildroot/usr/src

%pre
%_sbindir/groupadd -r -f %groupid
%_sbindir/useradd -M -r -d %home_dir -s /bin/false -c "Vmango user" -g %groupid %userid >/dev/null 2>&1 || :

%files
%_bindir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_unitdir/%name.service
%dir %attr(0770, root, %groupid) %home_dir

%changelog
* Sun Jul 21 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.0-alt1
- Initial build for ALT

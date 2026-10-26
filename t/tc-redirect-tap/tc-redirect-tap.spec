%define _libexecdir /usr/libexec
%define cni_dir %_libexecdir/cni
%global _unpackaged_files_terminate_build 1
%global import_path github.com/awslabs/tc-redirect-tap

Name:    tc-redirect-tap
Version: 0
# echo "alt1.git.$(git rev-list --count origin/master).$(git rev-parse --short origin/master)"
Release: alt1.git.109.34bf829


Summary: CNI plugin that adapts pre-existing CNI plugins/configuration to a tap device
License: Apache-2.0
Group:   System/Configuration/Networking
Url:     https://github.com/awslabs/tc-redirect-tap
Vcs:     https://github.com/awslabs/tc-redirect-tap.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
tc-redirect-tap is a CNI plugin. This plugin allows you to adapt
pre-existing CNI plugins/configuration to a tap device.

The plugin was initially developed as a part of firecracker-go-sdk
and can be used with Firecracker.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
mkdir -p %buildroot%_libexecdir/cni
mv %buildroot%_bindir/%name %buildroot%_libexecdir/cni/%name

%check
go test -mod=vendor ./internal/...

%files
%doc README.md LICENSE NOTICE
%dir %_libexecdir/cni
%_libexecdir/cni/%name

%changelog
* Mon Oct 26 2026 Maxim Slipenko <maks1ms@altlinux.org> 0-alt1.git.109.34bf829
- Initial build.

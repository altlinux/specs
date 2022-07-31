# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%global import_path gvisor.dev/gvisor/runsc
Name: gvisor
Version: 20220718.0
Release: alt1
Summary: An application kernel for containers that provides efficient defense-in-depth anywhere
License: Apache-2.0
Group: System/Base
Url: https://gvisor.dev/
Vcs: https://github.com/google/gvisor
Provides: golang-gvisor

Source: %name-%version.tar

# aarch64 is clained to be supported, but
# [aarch64] starting container: starting root container: starting sandbox: creating process: error loading VDSO: exec format error
ExclusiveArch: x86_64
BuildRequires(pre): rpm-build-golang
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc rpm-build-vm}}

%description
gVisor is an application kernel, written in Go, that implements a
substantial portion of the Linux system surface. It includes an Open
Container Initiative (OCI) runtime called runsc that provides an isolation
boundary between the application and the host kernel. The runsc runtime
integrates with Docker and Kubernetes, making it simple to run sandboxed
containers.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
CGO_ENABLED=0 \
go build -v -o bin/runsc -ldflags "-X main.version=%version" %import_path
go build -v -o bin/containerd-shim-runsc-v1 gvisor.dev/gvisor/shim

%install
cd .build/src/%import_path
install -Dp bin/runsc %buildroot%_bindir/runsc
install -Dp bin/containerd-shim-runsc-v1 %buildroot%_bindir/containerd-shim-runsc-v1

%check
PATH=%buildroot%_bindir:$PATH
runsc --version
containerd-shim-runsc-v1 -v
# Should not have interpreter
! readelf -l %buildroot%_bindir/runsc | grep -e interpreter -e ld-linux
vm-run --kvm=cond runsc --debug --debug-log=/tmp/runsc/ --TESTONLY-unsafe-nonroot do echo 123

%files
%doc AUTHORS LICENSE README.md
%_bindir/runsc
%_bindir/containerd-shim-runsc-v1

%changelog
* Sun Jul 31 2022 Vitaly Chikunov <vt@altlinux.org> 20220718.0-alt1
- Update to release-20220718.0.

* Fri Jun 17 2022 Vitaly Chikunov <vt@altlinux.org> 20220516.0-alt1
- First import release-20220516.0-67-g3ec7b4b61 (2022-05-31).

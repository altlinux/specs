%global _unpackaged_files_terminate_build 1
%global import_path github.com/aquasecurity/kube-bench

Name:    kube-bench
Version: 0.14.0
Release: alt1

Summary: Checks whether Kubernetes is deployed according to the CIS Kubernetes Benchmark
License: Apache-2.0
Group:   System/Configuration/Other
Url:     https://github.com/aquasecurity/kube-bench

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Kube-bench is a tool that checks whether Kubernetes is deployed securely
by running the checks documented in the CIS Kubernetes Benchmark.
Tests are configured with YAML files, making this tool easy to update
as test specifications evolve.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOBIN="$BUILDDIR/bin"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X %import_path/cmd.KubeBenchVersion=%version"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
mkdir -p %buildroot%_sysconfdir/%name
cp -r $BUILDDIR/src/%import_path/cfg/* %buildroot%_sysconfdir/%name/
chmod -R 750 %buildroot%_sysconfdir/%name

%files
%doc *.md
%_bindir/%name
%_sysconfdir/%name/*

%changelog
* Mon Dec 08 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.14.0-alt1
- Initial build for ALTLinux.

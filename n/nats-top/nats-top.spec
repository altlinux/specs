%define _unpackaged_files_terminate_build 1
%define import_path github.com/nats-io/nats-top

Name: nats-top
Version: 0.6.4
Release: alt1

Summary: A top-like tool for monitoring NATS servers
License: MIT
Group: Monitoring
Url: https://nats.io/
Vcs: https://github.com/nats-io/nats-top

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
%summary.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/nats-top

%changelog
* Wed Jul 15 2026 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt1
- Packaged for ALT Sisyphus.

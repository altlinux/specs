%global import_path github.com/LINBIT/k8s-await-election
Name:    k8s-await-election
Version: 0.4.1
Release: alt1

Summary: Ensure that only a single instance of a process is running in your Kubernetes cluster
License: Apache-2.0
Group:   Other
Url:     https://github.com/LINBIT/k8s-await-election

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
It leverages Kubernetes built-in leader election capabilities to coordinate commands
running in different pods and acts as a gatekeeper, only starting the command when
the pod becomes a leader.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.Version=%version"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Thu Nov 06 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.4.1-alt1
- Initial build for ALTLinux.

%define _unpackaged_files_terminate_build 1
%global import_path github.com/eraser-dev/eraser

Name:    eraser
Version: 1.4.1
Release: alt1

Summary: Cleaning up images from Kubernetes nodes
License: Apache-2.0
Group:   Development/Other
Url:     https://eraser-dev.github.io/eraser/docs/
Vcs:     https://github.com/eraser-dev/eraser

Source:  %name-%version.tar
Patch:   %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang rpm-build-golang

%description
Eraser helps Kubernetes admins remove a list of non-running images
from all Kubernetes nodes in a cluster.

%package        manager
Summary:        Eraser's manager
Group:          Development/Other

%description    manager
%summary

%package        collector
Summary:        Eraser's collector
Group:          Development/Other

%description    collector
%summary

%package        remover
Summary:        Eraser's remover
Group:          Development/Other

%description    remover
%summary

%package        trivy-scanner
Summary:        Eraser's trivy-scanner  
Group:          Development/Other

%description    trivy-scanner  
%summary

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/eraser-dev/eraser/pkg/version.eraserVersion=%version"

%golang_prepare

%golang_build .
for pkg in collector remover scanners/trivy; do
	%golang_build pkg/$pkg
done

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

mkdir -p %buildroot%_bindir
install -p -m 0755 $BUILDDIR/bin/%name %buildroot%_bindir/%name-manager
install -p -m 0755 $BUILDDIR/bin/collector %buildroot%_bindir/%name-collector
install -p -m 0755 $BUILDDIR/bin/remover %buildroot%_bindir/%name-remover
install -p -m 0755 $BUILDDIR/bin/trivy %buildroot%_bindir/%name-trivy-scanner

%files manager
%doc *.md
%_bindir/%name-manager

%files collector
%_bindir/%name-collector

%files remover
%_bindir/%name-remover

%files trivy-scanner
%_bindir/%name-trivy-scanner

%changelog
* Thu Mar 12 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus.

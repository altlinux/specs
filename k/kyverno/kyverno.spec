%global import_path github.com/kyverno/kyverno

%global _unpackaged_files_terminate_build 1

# git rev-parse v1.17.1^{commit}
%define git_commit 0fe91382401630df2c26c5525dd9eb9c0df1b0ef

Name: kyverno
Version: 1.17.1
Release: alt1
Summary: Kubernetes policy engine
License: Apache-2.0
Group: System/Configuration/Other
Url: https://kyverno.io
Vcs: https://github.com/kyverno/kyverno

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang

%description
Kyverno is a policy engine designed for Kubernetes.
It allows cluster administrators to manage and enforce policies
as Kubernetes resources.

%package init
Summary: Kyverno init container
Group: System/Configuration/Other
%description init
Kyverno init container used for preflight checks.

%package admission-controller
Summary: Kyverno admission controller
Group: System/Configuration/Other
%description admission-controller
Admission controller component of Kyverno.

%package background-controller
Summary: Kyverno background controller
Group: System/Configuration/Other
%description background-controller
Background controller component of Kyverno.

%package cleanup-controller
Summary: Kyverno cleanup controller
Group: System/Configuration/Other
%description cleanup-controller
Cleanup controller component of Kyverno.

%package reports-controller
Summary: Kyverno reports controller
Group: System/Configuration/Other
%description reports-controller
Reports controller component of Kyverno.

%package readiness-checker
Summary: Kyverno readiness checker
Group: System/Configuration/Other
%description readiness-checker
Readiness checker utility for Kyverno.

%package cli
Summary: Kyverno CLI for kubectl
Group: System/Configuration/Other
%description cli
kubectl plugin for Kyverno.

%prep
%setup

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null || \
            date -u -r "$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null || \
            date -u "$DATE_FMT")

sed -i "/vcs.time/,+5 {s/---/$BUILD_DATE/}" pkg/version/version.go
sed -i "/vcs.revision/,+5 {s/---/%git_commit/}" pkg/version/version.go

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath -mod=vendor"

LDFLAGS="-X %import_path/pkg/version.BuildVersion=%version"

%golang_prepare

pushd $BUILDDIR/src/%import_path

%gobuild -o %name --ldflags "$LDFLAGS" ./cmd/%name
%gobuild -o %{name}pre --ldflags "$LDFLAGS" ./cmd/%name-init
%gobuild -o %name-background-controller --ldflags "$LDFLAGS" ./cmd/background-controller
%gobuild -o %name-cleanup-controller --ldflags "$LDFLAGS" ./cmd/cleanup-controller
%gobuild -o %name-reports-controller --ldflags "$LDFLAGS" ./cmd/reports-controller
%gobuild -o %name-readiness-checker --ldflags "$LDFLAGS" ./cmd/readiness-checker
%gobuild -o kubectl-%name --ldflags "$LDFLAGS" ./cmd/cli/kubectl-%name

%install
export BUILDDIR="$PWD/.gopath"

install -Dm755 $BUILDDIR/src/%import_path/%name %buildroot%_bindir/%name
install -Dm755 $BUILDDIR/src/%import_path/%{name}pre %buildroot%_bindir/%{name}pre
install -Dm755 $BUILDDIR/src/%import_path/%name-background-controller %buildroot%_bindir/%name-background-controller
install -Dm755 $BUILDDIR/src/%import_path/%name-cleanup-controller %buildroot%_bindir/%name-cleanup-controller
install -Dm755 $BUILDDIR/src/%import_path/%name-reports-controller %buildroot%_bindir/%name-reports-controller
install -Dm755 $BUILDDIR/src/%import_path/%name-readiness-checker %buildroot%_bindir/%name-readiness-checker
install -Dm755 $BUILDDIR/src/%import_path/kubectl-%name %buildroot%_bindir/kubectl-%name

%files init
%_bindir/%{name}pre

%files admission-controller
%_bindir/%name

%files background-controller
%_bindir/%name-background-controller

%files cleanup-controller
%_bindir/%name-cleanup-controller

%files reports-controller
%_bindir/%name-reports-controller

%files readiness-checker
%_bindir/%name-readiness-checker

%files cli
%_bindir/kubectl-%name

%changelog
* Tue Mar 10 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.17.1-alt1
- Initial build for sisyphus.


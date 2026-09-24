%global _unpackaged_files_terminate_build 1
%global import_path sigs.k8s.io/cluster-api-operator

%global bname cluster-api-operator

# git rev-parse --short HEAD^{commit}
%global commit 4b0b8da

# git describe --abbrev=0 --tags | sed -E 's/^v([0-9]+)\.([0-9]+).*/\1/'
%global gitMajor 0

# git describe --abbrev=0 --tags | sed -E 's/^v([0-9]+)\.([0-9]+).*/\2/'
%global gitMinor 19

# git describe --abbrev=14 --match "v[0-9]*"
%global gitVersion v0.19.0-1-g4b0b8daffba03a

# git rev-list -n 1 $(git describe --abbrev=0 --tags)
%global gitReleaseCommit 2854bd696c96c66fbdbf5501262e95d2d4d016e8

Name:    cozystack-cluster-api-operator
Version: 0.19.0
Release: alt1

Summary: Home for Cluster API Operator, a subproject of sig-cluster-lifecycle (Cozystack-customized)
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-sigs/cluster-api-operator

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
The Cluster API Operator is a Kubernetes Operator designed to empower cluster
administrators to handle the lifecycle of Cluster API providers within a
management cluster using a declarative approach. It aims to improve user
experience in deploying and managing Cluster API, making it easier to handle
day-to-day tasks and automate workflows with GitOps.

%prep
%setup -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null)

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X '%import_path/version.buildDate=$BUILD_DATE' \
                -X '%import_path/version.gitCommit=%commit' \
                -X '%import_path/version.gitTreeState=clean' \
                -X '%import_path/version.gitMajor=%gitMajor' \
                -X '%import_path/version.gitMinor=%gitMinor' \
                -X '%import_path/version.gitVersion=%gitVersion' \
                -X '%import_path/version.gitReleaseCommit=%gitReleaseCommit'"
%golang_prepare
%gobuild -o bin/%bname ./cmd/main.go

%install
export BUILDDIR="$PWD"
export IGNORE_SOURCES=1
%golang_install

%check
# disable env tests
%gotest -v $(go list ./... | grep -Ev '^%import_path/(controller)|(cmd/plugin/cmd|internal/(controller)|(controller(/healthcheck)|envtest))$')

%files
%doc README.md LICENSE
%_bindir/%bname

%changelog
* Thu Sep 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.19.0-alt1
- Initial build for ALT.


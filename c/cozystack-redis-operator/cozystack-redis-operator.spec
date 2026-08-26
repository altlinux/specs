%global _unpackaged_files_terminate_build 1
%global import_path github.com/spotahome/redis-operator

%global rctag rc1

Name:    cozystack-redis-operator
Version: 1.3.0
Release: alt0.%rctag

Summary: Redis Operator creates/configures/manages redis-failovers atop k8s (Cozystack-customized)
License: Apache-2.0
Group:   Other
Url:     https://spotahome.github.io/redis-operator
Vcs:     https://github.com/spotahome/redis-operator

Source:  %name-%version.tar
Source1: vendor.tar
Patch:   labels.diff

BuildRequires(pre): rpm-build-golang

%description
Redis Operator creates/configures/manages high availability redis with sentinel
automatic failover atop Kubernetes.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X main.Version=%version"

%golang_prepare
%golang_build ./cmd/redisoperator

mv "$BUILDDIR"/bin/redisoperator "$BUILDDIR"/bin/redis-operator

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
%gotest -v ./...

%files
%doc README.md LICENSE
%_bindir/redis-operator

%changelog
* Tue Aug 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.3.0-alt0.rc1
- Initial build for ALT.


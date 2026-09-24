%global _unpackaged_files_terminate_build 1
%global import_path github.com/freshworks/redis-operator

Name:    redis-operator
Version: 3.3.5
Release: alt1

Summary: Redis Operator manages HA Redis/Valkey failover with Sentinel on K8s
License: Apache-2.0
Group:   Other
Url:     https://github.com/freshworks/redis-operator

Source0: %name-%version.tar
Source1: vendor.tar

Conflicts: cozystack-redis-operator

BuildRequires(pre): rpm-build-golang

%description
Redis Operator creates/configures/manages highly available Redis or Valkey
failovers with Sentinel automatic failover atop Kubernetes.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
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
* Thu Sep 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.3.5-alt1
- Initial build for ALT. 


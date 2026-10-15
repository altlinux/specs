%global _unpackaged_files_terminate_build 1
%global import_path github.com/freshworks/redis-operator

Name:    cozystack-redis-operator
Version: 3.3.5
Release: alt1

Summary: Redis Operator creates/configures/manages redis-failovers atop k8s (Cozystack-customized)
License: Apache-2.0
Group:   Other
Url:     https://github.com/freshworks-oss/redis-operator
Vcs:     https://github.com/freshworks-oss/redis-operator

Conflicts: redis-operator

Source:  %name-%version.tar
Source1: vendor.tar

Patch001: 001-labels.diff
Patch002: 002-tls.diff
Patch003: 003-unauthenticated-sentinel.diff
Patch004: 004-valkey-cli-auth.diff

BuildRequires(pre): rpm-build-golang

%description
Redis Operator creates/configures/manages high availability redis with sentinel
automatic failover atop Kubernetes.

%prep
%setup -a 1

# The carried TLS patch is source only: its CRD half ships as the chart
# patch, so the tarball's CRD and chart copies stay at v3.3.5 and the tests
# that read them would fail instead of skipping.
rm -rf manifests charts example .github

%patch001 -p1
%patch002 -p1
%patch003 -p1
%patch004 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

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
* Thu Oct 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.3.5-alt1
- New version 3.3.5.
- Switch upstream to freshworks-oss/redis-operator (spotahome fork).
- Apply new Cozystack patches.
- Set CGO_ENABLED=0.

* Tue Aug 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.3.0-alt0.rc1
- Initial build for ALT.


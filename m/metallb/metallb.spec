%global import_path go.universe.tf/metallb

%define _unpackaged_files_terminate_build 1

# git rev-parse v0.15.2^{commit}
%define git_commit 942c2fe54a75ac6353d3099eeebff33b6b8fe3f0

Name: metallb
Version: 0.15.2
Release: alt2

Summary: A network load-balancer implementation for Kubernetes using standard routing protocols
License: Apache-2.0
Group: Other
Url: https://metallb.io
Vcs: https://github.com/metallb/metallb

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24

%description
Kubernetes does not offer an implementation of network load balancers
(Services of type LoadBalancer) for bare-metal clusters. The implementations
of network load balancers that Kubernetes does ship with are all glue code
that calls out to various IaaS platforms (GCP, AWS, Azure...). If you're not
running on a supported IaaS platform (GCP, AWS, Azure...), LoadBalancers will
remain in the "pending" state indefinitely when created.

Bare-metal cluster operators are left with two lesser tools to bring user
traffic into their clusters, "NodePort" and "externalIPs" services. Both of
these options have significant downsides for production use, which makes
bare-metal clusters second-class citizens in the Kubernetes ecosystem.

MetalLB aims to redress this imbalance by offering a network load balancer
implementation that integrates with standard network equipment, so that
external services on bare-metal clusters also "just work" as much as possible.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

# 0.15.2 -> v0.15
GIT_BRANCH='v%(ver=%version; echo "${ver%.*}")'

export LDFLAGS="-X %import_path/internal/version.gitCommit=%git_commit \
    -X %import_path/internal/version.gitBranch=$GIT_BRANCH"

%golang_prepare

cd .build/src/%import_path
%golang_build \
    ./controller \
    ./speaker \
    ./configmaptocrs \
    ./frr-tools/metrics \
    ./frr-tools/cp-tool \

mv "$BUILDDIR/bin/controller" "$BUILDDIR/bin/metallb-controller"
mv "$BUILDDIR/bin/speaker" "$BUILDDIR/bin/metallb-speaker"
mv "$BUILDDIR/bin/configmaptocrs" "$BUILDDIR/bin/metallb-configmaptocrs"
mv "$BUILDDIR/bin/metrics" "$BUILDDIR/bin/metallb-frr-metrics"
mv "$BUILDDIR/bin/cp-tool" "$BUILDDIR/bin/metallb-cp-tool"

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -pD -m0755 frr-tools/reloader/frr-reloader.sh %buildroot%_bindir/metallb-frr-reloader.sh

%files
%doc *.md
%_bindir/metallb-controller
%_bindir/metallb-speaker
%_bindir/metallb-configmaptocrs
%_bindir/metallb-cp-tool
%_bindir/metallb-frr-metrics
%_bindir/metallb-frr-reloader.sh

%changelog
* Sat Nov 01 2025 Alexander Stepchenko <geochip@altlinux.org> 0.15.2-alt2
- Prefix all the executables with "metallb-".

* Tue Oct 28 2025 Alexander Stepchenko <geochip@altlinux.org> 0.15.2-alt1
- Initial build.

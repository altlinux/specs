%define _unpackaged_files_terminate_build 1
%define import_path github.com/gravitational/teleport

# golang does not work well with lto
%global optflags_lto %nil
%ifarch loongarch64
# avoid "relocation R_LARCH_B26 overflow" error in cgo-compiled object files
%add_optflags -mcmodel=medium
%endif

#Disabling tests due to the need to use the network,
#but it is not available in the build environment.
%def_without check

Name: teleport
Version: 18.9.1
Release: alt1

Summary: The easiest, and most secure way to access and protect all of your infrastructure
License: AGPL-3.0
Group: Networking/File transfer
Url: https://goteleport.com/
Vcs: https://github.com/gravitational/teleport

ExclusiveArch: %go_arches
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: webassets-%version.tar.gz
Source3: %name-%version-vendor-build.assets-tooling.tar
Source4: %name-%version-vendor-tool-fdpass-teleport.tar
Patch0: %name-%version-alt.patch

#sytemd services
Source10: %name-auth.service
Source11: %name-node.service
Source12: %name-proxy.service
Source13: %name.service

Source20: %name.yaml

BuildRequires(pre): rpm-build-golang
BuildRequires: libfido2-devel
BuildRequires: rust-cargo
%if_with check
BuildRequires: helm
%endif

%package server
Summary: Teleport server (auth, proxy, node)
Group: Networking/File transfer

%package client
Summary: Teleport client
Group: Networking/File transfer

%package admin
Summary: Teleport admin tools
Group: Networking/File transfer
Requires: %name-server = %EVR

%package bot
Summary: Teleport Machine ID
Group: Networking/File transfer
Requires: %name-client = %EVR

%description
Teleport includes an identity-aware access proxy, a CA that issues short-lived
certificates, a unified access control system and a tunneling system to access
resources behind the firewall

%description server
The Teleport server package provides the core components for running a Teleport
cluster, including the authentication service (auth), proxy service, and node
service. This package is required for deploying Teleport as an identity-aware
access proxy for SSH, Kubernetes, databases and internal web applications.

%description client
The Teleport client package contains the tsh command-line tool, which provides
SSH-like functionality for accessing Teleport-protected resources. Users can
securely connect to servers, Kubernetes clusters and other infrastructure
through the Teleport proxy using short-lived certificates instead of static
credentials.

%description admin
The Teleport administration package includes the tctl administrative tool for
managing Teleport clusters. It provides functionality for configuring
authentication methods, managing roles and permissions, adding/removing nodes,
and other cluster administration tasks through both CLI and configuration files.

%description bot
The Teleport bot package contains tbot, the Teleport Machine ID service that
enables secure, certificate-based access for automated systems and workloads.
It provides short-lived credentials for CI/CD pipelines, service accounts, and
other non-human access patterns, eliminating the need for long-lived static
credentials in your infrastructure.

%prep
%setup -a1 -a2 -a3 -a4
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_CFLAGS="%optflags"
export CGO_CXXFLAGS="%optflags"
export CGO_LDFLAGS="%optflags"
export RUST_TARGET_ARCH="$(rustc -vV | sed -n 's,host: ,,p')"

%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
RDPCLIENT_SKIP_BUILD=1 with_rdpclient="no" WEBASSETS_SKIP_BUILD=0 FIDO2=dynamic make all
popd

%install
export BUILDDIR="$PWD/.build"
export BINDIR="$BUILDDIR"
export IGNORE_SOURCES=1
%golang_install
for src in %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13}; do
  install -pDm 0644 "$src" "%buildroot%_unitdir/$(basename $src)"
done
install -pDm 0644 %SOURCE20 "%buildroot%_sysconfdir/%name/$(basename %SOURCE20)"

mkdir -p %buildroot%_localstatedir/%name
rm -rfv %buildroot/%_bindir/sessionhelper

%check
make test

%pre server
%_sbindir/groupadd -r -f %name > /dev/null 2>&1 ||:
%_sbindir/useradd -r -g %name -M -d %_localstatedir/%name -s /dev/null -c "Teleport user" %name > /dev/null 2>&1 ||:

%files server
%_bindir/%name
%_bindir/%name-update
%_unitdir/%name-auth.service
%_unitdir/%name-node.service
%_unitdir/%name-proxy.service
%_unitdir/%name.service
%_sysconfdir/%name/
%doc README.md LICENSE
%dir %attr(775,%name,%name) %_localstatedir/%name/

%files client
%_bindir/tsh

%files admin
%_bindir/tctl
%_bindir/fdpass-teleport

%files bot
%_bindir/tbot

%changelog
* Tue Jun 23 2026 Artem Krasovskiy <aibure@altlinux.org> 18.9.1-alt1
- New version 18.9.1.

* Thu Feb 19 2026 Artem Krasovskiy <aibure@altlinux.org> 18.7.0-alt1
- New version 18.7.0.

* Wed Feb 04 2026 Artem Krasovskiy <aibure@altlinux.org> 18.6.6-alt1
- New version 18.6.6.

* Mon Dec 29 2025 Artem Krasovskiy <aibure@altlinux.org> 18.6.1-alt1
- New version 18.6.1.

* Fri Sep 12 2025 Ivan A. Melnikov <iv@altlinux.org> 18.2.0-alt2
- NMU: Fix FTBFS on loongarch64.

* Tue Sep 09 2025 Artem Krasovskiy <aibure@altlinux.org> 18.2.0-alt1
- New version 18.2.0.

* Tue Sep 02 2025 Artem Krasovskiy <aibure@altlinux.org> 18.1.4-alt1
- Initial build for Sisyphus.

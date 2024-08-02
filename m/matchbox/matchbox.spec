%global import_path github.com/poseidon/matchbox

Name: matchbox
Version: 0.11.0
Release: alt1

Summary: Network boot and provision CoreOS and Flatcar Linux clusters
License: Apache-2.0
Group: Networking/Other
Url: https://matchbox.psdn.io
Vcs: https://github.com/poseidon/matchbox.git

Source: %name-%version.tar
Source2: %name.service
Source3: %name.sysconfig
Patch: %name-%version.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.19

%define mdirattr %attr(0750,root,%name) %dir

%description
Matchbox is a service that matches bare-metal machines to profiles
that PXE boot and provision clusters. Machines are matched by labels
like MAC or UUID during PXE and profiles specify a kernel/initrd,
iPXE config, and Ignition config.

Features:
 * Chainload via iPXE and match hardware labels
 * Provision Fedora CoreOS or Flatcar Linux (powered by Ignition)
 * Authenticated gRPC API for clients (e.g. Terraform)

%prep
%setup
%autopatch -p1
# cleanup docs for package
find . -type f -name '.gitignore' -delete
find . -type f -name '.gitkeep' -delete

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-w -X github.com/poseidon/matchbox/matchbox/version.Version=v%version"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build cmd/matchbox

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot{%_unitdir,%_sysconfdir/{sysconfig,%name}}
mkdir -p %buildroot%_sharedstatedir/%name/{assets,profiles,groups,ignition,cloud,generic}

install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0640 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%pre
groupadd -r -f %name > /dev/null 2>&1 ||:
useradd -r -g %name -s /dev/null -c "%name services" -M -d %_sharedstatedir/%name %name > /dev/null 2>&1 ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md LICENSE contrib/dnsmasq examples docs scripts
%_bindir/%name
%_unitdir/%name.service
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/sysconfig/%name
%mdirattr %_sysconfdir/%name
%mdirattr %_sharedstatedir/%name
%mdirattr %_sharedstatedir/%name/assets
%mdirattr %_sharedstatedir/%name/profiles
%mdirattr %_sharedstatedir/%name/groups
%mdirattr %_sharedstatedir/%name/ignition
%mdirattr %_sharedstatedir/%name/cloud
%mdirattr %_sharedstatedir/%name/generic

%changelog
* Fri Aug 02 2024 Alexey Shabalin <shaba@altlinux.org> 0.11.0-alt1
- Initial build.


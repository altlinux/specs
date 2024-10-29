%global import_path github.com/fleetdm/fleet
Name:     fleet
Version:  4.58.0
Release:  alt1

Summary:  Open-source platform for IT, security, and infrastructure teams
License:  MIT
Group:    Other
Url:      https://github.com/fleetdm/fleet

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

ExcludeArch: %ix86 ppc64le

%description
Open-source platform for IT and security teams with thousands of computers.
Designed for APIs, GitOps, webhooks, YAML, and humans.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="$LDFLAGS -X github.com/kolide/kit/version.version=%version"
%golang_build cmd/fleet cmd/fleetctl

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Mon Oct 28 2024 Mikhail Gordeev <obirvalger@altlinux.org> 4.58.0-alt1
- new version 4.58.0 (Fixes: CVE-2022-23600)

* Tue May 14 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.6.0-alt2
- NMU: fixed FTBFS on LoongArch (updated vendored golang.org/x/sys).

* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt1
- Updated to upstream version 3.6.0 (Fixes: CVE-2020-26276).

* Tue Nov 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

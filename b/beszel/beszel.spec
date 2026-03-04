%global _unpackaged_files_terminate_build 1
%global import_path github.com/henrygd/beszel

#Disabling tests due to the need to use the network,
#but it is not available in the build environment.
%def_without check

Name: beszel
Version: 0.18.2
Release: alt1
Summary: Lightweight server monitoring hub
License: MIT
Group: System/Configuration/Networking
Url: https://beszel.dev/
Vcs: https://github.com/henrygd/beszel

ExclusiveArch: %go_arches
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
# Needs for build web-ui
Patch0: %name-0.18.2-alt-add-peers-to-package-lock.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: npm

%description
Lightweight server monitoring hub with historical data, docker stats,
and alerts. Beszel is a lightweight server monitoring platform that
includes Docker statistics, historical data, and alert functions.
It has a friendly web interface, simple configuration, and is ready to
use out of the box. It supports automatic backup, multi-user, OAuth
authentication, and API access.

%prep
%setup -a1 -a2
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
%golang_build $BUILDDIR/src/%import_path/internal/cmd/agent
# Build web-ui
pushd $BUILDDIR/src/%import_path/internal/site
mv ../../node_modules ./node_modules
npm run build
popd
%golang_build $BUILDDIR/src/%import_path/internal/cmd/hub

%install
export BUILDDIR="$PWD/.build"
install -D -m 755 $BUILDDIR/bin/agent %buildroot%_bindir/%name-agent
install -D -m 755 $BUILDDIR/bin/hub %buildroot%_bindir/%name-hub

%check
export GOEXPERIMENT=synctest
go test -tags=testing ./...

%files
%_bindir/%name-agent
%_bindir/%name-hub
%doc LICENSE readme.md

%changelog
* Wed Jan 28 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.18.2-alt1
- Initial built for ALT Sisyphus.

%global import_path github.com/drone/drone
Name:     drone
Version:  0.8.10
Release:  alt1

Summary:  Drone is a Continuous Delivery platform built on Docker
License:  Apache-2.0
Group:    Other
Url:      https://github.com/drone/drone

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Drone is a Continuous Delivery system built on container technology. Drone uses
a simple YAML configuration file, a superset of docker-compose, to define and
execute Pipelines inside Docker containers.

%package agent
Summary:  Drone Continuous Delivery agent
Group:    Other

%description agent
Agent for Drone

%prep
%setup

# Steps to reproduce:
#   1) remove old vendor directory;
#   2) run `go mod init github.com/drone/drone`;
#   3) append "replace github.com/Sirupsen/logrus => github.com/sirupsen/logrus v1.3.0"
#       to file go.mod;
#   4) run `go mod vendor`, it creates new vendor directory;
#   5) move vendor to new_vendor `mv vendor new_vendor`
#   6) get old vendor directory
#   7) copy missed directories from new_vendor to vendor
%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd "$BUILDDIR/src/%import_path"
%golang_build cmd/drone-{agent,server}

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files agent
%_bindir/drone-agent

%files
%_bindir/drone-server
%doc *.md

%changelog
* Wed Feb 06 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus

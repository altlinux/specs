%global import_path github.com/docker/docker-buildx
Name:     docker-buildx
Version:  0.8.2
Release:  alt1

Summary:  Docker CLI plugin for extended build capabilities with BuildKit
License:  Apache-2.0
Group:    Other
Url:      https://github.com/docker/buildx

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
buildx is a Docker CLI plugin for extended build capabilities with BuildKit.

Key features:
- Familiar UI from docker build
- Full BuildKit capabilities with container driver
- Multiple builder instance support
- Multi-node builds for cross-platform images
- Compose build support
- High-level build constructs (bake)
- In-container driver support (both Docker and Kubernetes)

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/buildx

%install
install -D -m 0755 .build/bin/buildx %buildroot/usr/lib/docker/cli-plugins/%name

%files
%doc *.md
/usr/lib/docker/cli-plugins/%name

%changelog
* Mon Aug 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus

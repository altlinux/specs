%global pkg_name github.com/docker/docker-buildx
%global commit   00ed17df6d20f3ca4553d45789264cdb78506e5f

Name:     docker-buildx
Version:  0.10.2
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
export VERSION=%version
export REVISION=%commit
export PKG_NAME=%pkg_name

mkdir -p .build
go build -ldflags "-s -w \
    -X ${PKG_NAME}/version.Version=${VERSION} \
    -X ${PKG_NAME}/version.Revision=${VERSION}" \
    -mod=vendor -o .build/%name cmd/buildx/main.go

%install
install -D -m 0755 .build/%name %buildroot%{_libexecdir}/docker/cli-plugins/%name

%files
%doc *.md
%{_libexecdir}/docker/cli-plugins/%name

%changelog
* Thu Feb 2 2023 Vladimir Didenko <cow@altlinux.org> 0.10.2-alt1
- New version
- Switch to Go modules build type

* Mon Aug 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus

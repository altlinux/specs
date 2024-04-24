%global pkg_name github.com/docker/buildx

Name:     docker-buildx
Version:  0.14.0
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
mkdir -p .build
go build -ldflags "-s -w \
    -X %pkg_name/version.Version=%version \
    -X %pkg_name/version.Revision=" \
    -mod=vendor -o .build/%name cmd/buildx/main.go

%install
install -D -m 0755 .build/%name %buildroot%{_libexecdir}/docker/cli-plugins/%name

%files
%doc *.md
%{_libexecdir}/docker/cli-plugins/%name

%changelog
* Wed Apr 24 2024 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- New version

* Thu Mar 21 2024 Vladimir Didenko <cow@altlinux.org> 0.13.1-alt1
- New version

* Tue Mar 12 2024 Vladimir Didenko <cow@altlinux.org> 0.13.0-alt1
- New version

* Tue Jan 23 2024 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt1
- New version

* Thu Nov 23 2023 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- New version

* Fri Jul 28 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.2-alt2
- Fix version info (Closes: 47052)

* Wed Jul 26 2023 Vladimir Didenko <cow@altlinux.org> 0.11.2-alt1
- New version

* Fri Jul 7 2023 Vladimir Didenko <cow@altlinux.org> 0.11.1-alt1
- New version

* Tue May 23 2023 Vladimir Didenko <cow@altlinux.org> 0.10.5-alt1
- New version

* Tue Apr 4 2023 Vladimir Didenko <cow@altlinux.org> 0.10.4-alt1
- New version

* Thu Feb 2 2023 Vladimir Didenko <cow@altlinux.org> 0.10.2-alt1
- New version
- Switch to Go modules build type

* Mon Aug 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus

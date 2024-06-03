%global import_path github.com/oras-project/oras
Name:    oras
Version: 1.2.0
Release: alt1

Summary: OCI registry client - managing content like artifacts, images, packages
License: Apache-2.0
Group:   Other
Url:     https://github.com/oras-project/oras

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="-X oras.land/oras/internal/version.BuildMetadata="
%golang_build cmd/oras

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Fri May 31 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Thu Sep 07 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Mon Aug 14 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Mon May 29 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

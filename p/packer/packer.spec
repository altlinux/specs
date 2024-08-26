%global import_path github.com/hashicorp/packer
Name:     packer
Version:  1.11.2
Release:  alt1

Summary:  Packer is a tool for creating identical machine images for multiple platforms from a single source configuration
License:  MPL-2.0
Group:    Other
Url:      https://github.com/hashicorp/packer

Packager: Mikhail Gordeev <obirvalger@altlinux.org>


Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Packer is a tool for building identical machine images for multiple platforms
from a single source configuration.

Packer is lightweight, runs on every major operating system, and is highly
performant, creating machine images for multiple platforms in parallel. Packer
comes out of the box with support for many platforms, the full list of which
can be found at https://www.packer.io/docs/builders/index.html.

Support for other platforms can be added via plugins.

The images that Packer creates can easily be turned into Vagrant boxes.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 644 contrib/zsh-completion/_%name %buildroot%_datadir/zsh/site-functions/_%name

%files
%_bindir/*
%_datadir/zsh/site-functions/_%name
%doc *.md

%changelog
* Sat Aug 24 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.2-alt1
- new version 1.11.2

* Wed Jul 17 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.1-alt1
- new version 1.11.1

* Tue May 28 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.10.3-alt1
- new version 1.10.3

* Sat Nov 18 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.4-alt1
- new version 1.9.4 (Closes: 48478)

* Thu Apr 02 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.5-alt1
- new version 1.5.5

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.5-alt1
- new version 1.3.5

* Fri Sep 21 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

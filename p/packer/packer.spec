%global import_path github.com/hashicorp/packer
Name:     packer
Version:  1.5.5
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

%files
%_bindir/*
%doc *.md

%changelog
* Thu Apr 02 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.5-alt1
- new version 1.5.5

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.5-alt1
- new version 1.3.5

* Fri Sep 21 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

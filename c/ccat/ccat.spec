%global import_path github.com/jingweno/ccat
Name:     ccat
Version:  1.1.0
Release:  alt1

Summary:  Colorizing cat
License:  MIT
Group:    Other
Url:      https://github.com/jingweno/ccat

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
It works similar to cat but displays content with syntax highlighting.

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

%changelog
* Mon Jan 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

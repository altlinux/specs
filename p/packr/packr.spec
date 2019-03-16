%global import_path github.com/gobuffalo/packr
Name:     packr
Version:  2.0.6
Release:  alt1

Summary:  The simple and easy way to embed static files into Go binaries.
License:  MIT
Group:    Other
Url:      https://github.com/gobuffalo/packr

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build packr

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.6-alt1
- Initial build for Sisyphus

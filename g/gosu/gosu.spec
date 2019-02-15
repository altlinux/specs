%global import_path github.com/tianon/gosu
Name:     gosu
Version:  1.11
Release:  alt1

Summary:  Simple Go-based setuid+setgid+setgroups+exec
License:  GPL-3.0
Group:    Other
Url:      https://github.com/tianon/gosu

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

# Get dependencies from vendor directory
# To update vendor directory run:
# $ go mod init github.com/tianon/gosu
# $ go mod vendor && rm go.{mod,sum}
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
* Fri Feb 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.11-alt1
- Initial build for Sisyphus

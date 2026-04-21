%define _unpackaged_files_terminate_build 1

%define import_path github.com/peco/peco

Name:    peco
Version: 0.6.0
Release: alt1

Summary: Simplistic interactive filtering tool
License: MIT
Group:   Development/Tools
Url:     https://github.com/peco/peco

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
peco (pronounced peh-koh) is based on a python tool, percol. percol
was darn useful, but I wanted a tool that was a single binary, and
forget about python. peco is written in Go, and therefore you can
just grab the binary releases and drop it in your $PATH.

peco can be a great tool to filter stuff like logs, process stats,
find files, because unlike grep, you can type as you think and
look through the current results.

%prep
%setup -a 1

%build
export GO111MODULE=off
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path
go build cmd/peco/peco.go

%install
mkdir -p %buildroot%_bindir
install -m 0755 .gopath/src/%import_path/%name %buildroot%_bindir/%name

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Tue Apr 21 2026 Nikita Shmatko <nash@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Mon Nov 24 2025 Nikita Shmatko <nash@altlinux.org> 0.5.11-alt1
- Initial build for Sisyphus.

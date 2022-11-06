%define _unpackaged_files_terminate_build 1

%global import_path golang.org/x/tools/gopls

Name: gopls
Version: 0.10.1
Release: alt1

Summary: The Go language server
License: BSD-3-Clause
Group: Development/Other
Url: https://pkg.go.dev/golang.org/x/tools/gopls

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

Requires: golang

%description
Gopls (pronounced "go please") is an LSP server for Go. The Language
Server Protocol allows any text editor to be extended with IDE-like
features; see https://langserver.org/ for details.

See https://github.com/golang/tools/blob/master/gopls/README.md for
the most up-to-date documentation.

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
* Sun Nov 06 2022 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt1
- update to 0.10.1

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt3
- add golang dependency

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt2
- fix description after copy-paste

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt1
- initial build for Sisyphus


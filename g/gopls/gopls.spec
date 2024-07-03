%define _unpackaged_files_terminate_build 1
%define import_path golang.org/x/tools/gopls

Name: gopls
Version: 0.16.1
Release: alt1

Summary: The Go language server
License: BSD-3-Clause
Group: Development/Other
Url: https://pkg.go.dev/golang.org/x/tools/gopls
Vcs: https://cs.opensource.google/go/x/tools

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

Requires: golang

BuildRequires(pre): rpm-build-golang

%description
Gopls (pronounced "go please") is an LSP server for Go. The Language
Server Protocol allows any text editor to be extended with IDE-like
features; see https://langserver.org/ for details.

See https://github.com/golang/tools/blob/master/gopls/README.md for
the most up-to-date documentation.

%prep
%setup -a1
%autopatch -p1

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
* Wed Jul 03 2024 Anton Zhukharev <ancieg@altlinux.org> 0.16.1-alt1
- Updated to 0.16.1.

* Wed May 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.15.3-alt1
- Updated to 0.15.3.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.15.2-alt1
- Updated to 0.15.2.

* Fri Nov 17 2023 Anton Zhukharev <ancieg@altlinux.org> 0.14.2-alt1
- Updated to 0.14.2.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.14.1-alt1
- Updated to 0.14.1.

* Tue Aug 15 2023 Anton Zhukharev <ancieg@altlinux.org> 0.13.2-alt1
- Updated to 0.13.2.

* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.13.1-alt1
- Updated to 0.13.1.

* Wed Jun 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.12.2-alt1
- New version.

* Wed May 31 2023 Anton Zhukharev <ancieg@altlinux.org> 0.12.0-alt1
- New version.

* Thu Dec 15 2022 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- update to 0.11.0

* Sun Nov 06 2022 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt1
- update to 0.10.1

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt3
- add golang dependency

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt2
- fix description after copy-paste

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt1
- initial build for Sisyphus


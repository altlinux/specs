%define _unpackaged_files_terminate_build 1
%define import_path github.com/golangci/golangci-lint

Name: golangci-lint
Version: 1.58.2
Release: alt1

Summary: Fast linters Runner for Go
License: GPL-3.0
Group: Development/Tools
Url: https://golangci-lint.run
Vcs: https://github.com/golangci/golangci-lint

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
golangci-lint is a fast Go linters runner. It runs linters in parallel,
uses caching, supports yaml config, has integrations with all major IDE
and has dozens of linters included.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/*

%changelog
* Mon May 20 2024 Anton Zhukharev <ancieg@altlinux.org> 1.58.2-alt1
- Updated to 1.58.2.

* Wed May 15 2024 Anton Zhukharev <ancieg@altlinux.org> 1.58.1-alt1
- Updated to 1.58.1.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 1.57.2-alt1
- Updated to 1.57.2.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 1.55.2-alt1
- Updated to 1.55.2.

* Mon Aug 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.54.2-alt1
- Updated to 1.54.2.

* Fri Aug 18 2023 Anton Zhukharev <ancieg@altlinux.org> 1.54.1-alt1
- Updated to 1.54.1.

* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.53.3-alt1
- Updated to 1.53.3.

* Sat Jun 03 2023 Anton Zhukharev <ancieg@altlinux.org> 1.53.2-alt1
- New version.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.52.2-alt1
- New version.

* Mon Nov 14 2022 Anton Zhukharev <ancieg@altlinux.org> 1.50.1-alt1
- initial build for Sisyphus


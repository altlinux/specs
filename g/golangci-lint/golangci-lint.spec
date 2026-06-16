%define _unpackaged_files_terminate_build 1
%define import_path github.com/golangci/golangci-lint

Name: golangci-lint
Version: 2.12.2
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
%_bindir/golangci-lint

%changelog
* Thu Jun 11 2026 Artem Krasovskiy <aibure@altlinux.org> 2.12.2-alt1
- Updated to 2.12.2.

* Fri Apr 10 2026 Artem Krasovskiy <aibure@altlinux.org> 2.11.4-alt1
- Updated to 2.11.4.

* Wed Feb 18 2026 Artem Krasovskiy <aibure@altlinux.org> 2.10.1-alt1
- Updated to 2.10.1.

* Tue Jan 13 2026 Artem Krasovskiy <aibure@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Fri Dec 12 2025 Artem Krasovskiy <aibure@altlinux.org> 2.7.2-alt1
- Updated to 2.7.2.

* Fri Oct 24 2025 Artem Krasovskiy <aibure@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.

* Wed Mar 26 2025 Anton Zhukharev <ancieg@altlinux.org> 2.0.2-alt1
- Updated to 2.0.2.

* Tue Mar 25 2025 Anton Zhukharev <ancieg@altlinux.org> 2.0.1-alt1
- Updated to 2.0.1.

* Fri Mar 21 2025 Anton Zhukharev <ancieg@altlinux.org> 1.64.8-alt1
- Updated to 1.64.8.

* Fri Mar 14 2025 Anton Zhukharev <ancieg@altlinux.org> 1.64.7-alt1
- Updated to 1.64.7.

* Sun Mar 09 2025 Anton Zhukharev <ancieg@altlinux.org> 1.64.6-alt1
- Updated to 1.64.6.

* Tue Feb 25 2025 Anton Zhukharev <ancieg@altlinux.org> 1.64.5-alt1
- Updated to 1.64.5.

* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 1.61.0-alt1
- Updated to 1.61.0.

* Wed Jul 03 2024 Anton Zhukharev <ancieg@altlinux.org> 1.59.1-alt1
- Updated to 1.59.1.

* Mon May 27 2024 Anton Zhukharev <ancieg@altlinux.org> 1.59.0-alt1
- Updated to 1.59.0.

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


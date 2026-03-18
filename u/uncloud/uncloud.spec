%define _unpackaged_files_terminate_build 1
%global import_path github.com/psviderski/uncloud

Name: uncloud
Version: 0.17.1
Release: alt1
Summary: A lightweight tool for deploying and managing containerised applications across a network of Docker hosts.
License: Apache-2.0
Group: Archiving/Backup
Url: https://github.com/psviderski/uncloud

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Thu Mar 12 2026 Pavel Shilov <zerospirit@altlinux.org> 0.17.1-alt1
- 0.16.0 -> 0.17.1

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 0.16.0-alt1
- 0.15.1 -> 0.16.0

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 0.15.1-alt1
- 0.13.2 -> 0.15.1

* Tue Oct 21 2025 Pavel Shilov <zerospirit@altlinux.org> 0.13.2-alt1
- 0.12.2 -> 0.13.2

* Mon Sep 29 2025 Pavel Shilov <zerospirit@altlinux.org> 0.12.2-alt1
- 0.12.0 -> 0.12.2

* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.12.0-alt1
- 0.11.1 -> 0.12.0

* Wed Aug 20 2025 Pavel Shilov <zerospirit@altlinux.org> 0.11.1-alt1
- 0.9.0 -> 0.11.1

* Sun Jul 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.9.0-alt1
- Initian build for Sisyphus.

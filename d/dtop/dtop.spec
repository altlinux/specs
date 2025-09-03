%define _unpackaged_files_terminate_build 1
%global import_path github.com/amir20/dtop

Name: dtop
Version: 0.0.43
Release: alt1
Summary: Terminal dashboard for Docker monitoring across multiple hosts with Dozzle integration.
License: MIT
Group: System/Configuration/Other
Url: https://github.com/amir20/dtop

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.43-alt1
- 0.0.40 -> 0.0.43

* Wed Aug 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.40-alt1
- 0.0.38 -> 0.0.40

* Mon Aug 18 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.38-alt1
- 0.0.36 -> 0.0.38

* Mon Jul 21 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.36-alt1
- Initial build for Sisyphys.

%define _unpackaged_files_terminate_build 1
%global import_path github.com/byawitz/ggh

Name: ggh
Version: 0.1.5
Release: alt1
Summary: Recall your SSH sessions (also search your SSH config file)
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/byawitz/ggh

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.

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
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot%_datadir/%name
%golang_install

%files
%doc readme.md
%_bindir/%name

%changelog
* Thu Sep 25 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5

* Tue May 06 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus.

%define _unpackaged_files_terminate_build 1
%global import_path github.com/alebeck/boring

Name: boring
Version: 0.11.5
Release: alt1
Summary: The boring SSH tunnel manager.
License: MIT
Group: Networking/Other
Url: https://github.com/alebeck/boring

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

%golang_build cmd/%name/

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc *.md 
%_bindir/%name

%changelog
* Sat Jul 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.11.5-alt1
- Initial build for Sisyphus.

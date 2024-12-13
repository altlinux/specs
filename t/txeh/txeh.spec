%define _unpackaged_files_terminate_build 1
%global import_path github.com/github.com/txn2/txeh

Name: txeh
Version: 1.5.4
Release: alt1
Summary: Go library and CLI utility for /etc/hosts management
License:  Apache-2.0
Group: Networking/Remote access
Url: https://github.com/txn2/txeh

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
It is easy to open your /etc/hosts file in text editor and add or remove
entries.
However, if you make heavy use of /etc/hosts for software development or DevOps
purposes, it can sometimes be difficult to automate and validate large numbers
of host entries.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build %name/

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
* Fri Dec 13 2024 Pavel Shilov <zerospirit@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus

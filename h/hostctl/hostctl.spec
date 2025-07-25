%define _unpackaged_files_terminate_build 1
%global import_path github.com/guumaster/hostctl

Name: hostctl
Version: 1.1.4
Release: alt1.1
Summary: Your dev tool to manage /etc/hosts like a pro!
License: MIT
Group: Networking/Remote access
Url: https://github.com/guumaster/hostctl

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
This tool gives you more control over the use of your hosts file.
You can have multiple profiles and switch them on/off as you need.

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/*

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
* Thu Jul 24 2025 Pavel Shilov <zerospirit@altlinux.org> 1.1.4-alt1.1
- Update based on upstream.

* Tue Jul 30 2024 Pavel Shilov <zerospirit@altlinux.org> 1.1.4-alt1
- initial build for Sisyphus

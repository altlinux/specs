%define _unpackaged_files_terminate_build 1
%global import_path github.com/ax-i-om/bitcrook

Name: bitcrook
Version: 2.3.2
Release: alt1
Summary: Open-Source Intelligence Apparatus
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/ax-i-om/bitcrook

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Bitcrook is an open-source intelligence apparatus that aims to centralize
all of the tools necessary to carry out an investigation.

%prep
%setup -q

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
* Tue Aug 20 2024 Pavel Shilov <zerospirit@altlinux.org> 2.3.2-alt1
- initial build for Sisyphus

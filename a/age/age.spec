%define _unpackaged_files_terminate_build 1

%global import_path filippo.io/age

Name: age
Version: 1.1.1
Release: alt1

Summary: simple, modern and secure file encryption tool
License: BSD-3-Clause
Group: Text tools
Url: https://github.com/FiloSottile/age

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
A simple, modern and secure encryption tool (and Go library) with small
explicit keys, no config options, and UNIX-style composability.

%prep
%setup

%build
export GO111MODULE=off
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

cp -r LICENSE README.md doc %_builddir/
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

install -pD -m0644 doc/age.1 %buildroot%_man1dir/age.1
install -pD -m0644 doc/age-keygen.1 %buildroot%_man1dir/age-keygen.1

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*

%changelog
* Thu Dec 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Jul 26 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt3
- add go vendor modules into source tree instead of using patch

* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt2
- switch to traditional golang building instructions

* Wed May 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

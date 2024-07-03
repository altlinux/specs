%define _unpackaged_files_terminate_build 1
%define import_path filippo.io/age

Name: age
Version: 1.2.0
Release: alt1

Summary: A simple, modern and secure file encryption tool
License: BSD-3-Clause
Group: Text tools
Url: https://pkg.go.dev/filippo.io/age
Vcs: https://github.com/FiloSottile/age

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
A simple, modern and secure encryption tool (and Go library) with small
explicit keys, no config options, and UNIX-style composability.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export LDFLAGS="-X main.Version=%version"
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
* Wed Jul 03 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Dec 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Jul 26 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt3
- add go vendor modules into source tree instead of using patch

* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt2
- switch to traditional golang building instructions

* Wed May 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

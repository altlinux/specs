%define _unpackaged_files_terminate_build 1

Name: age
Version: 1.0.0
Release: alt1

Summary: simple, modern and secure file encryption tool
License: BSD-3-Clause
Group: Text tools
Url: https://github.com/FiloSottile/age

Source: %name-%version.tar
Patch0: go_mod_vendor.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
A simple, modern and secure encryption tool (and Go library) with small
explicit keys, no config options, and UNIX-style composability.

%prep
%setup
%patch0 -p1

%build
%gobuild -o %_builddir/ ./cmd/*
cp -r LICENSE README.md doc %_builddir/

%install
mkdir -p %buildroot

cd %_builddir

install -pD -m0644 doc/age.1 %buildroot/%_man1dir/age.1
install -pD -m0644 doc/age-keygen.1 %buildroot/%_man1dir/age-keygen.1

install -pD age %buildroot%_bindir/age
install -pD age-keygen %buildroot%_bindir/age-keygen

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*

%changelog
* Wed May 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

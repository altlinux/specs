%global provider        github
%global provider_tld    com
%global project         cpuguy83
%global repo            go-md2man
# https://github.com/cpuguy83/go-md2man
%global provider_prefix %provider.%provider_tld/%project/%repo
%global import_path     %provider_prefix
%global commit          20f5889cbdc3c73dbd2862796665e7c465ade7d1
%global shortcommit     %(c=%commit; echo ${c:0:7})

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: golang-%provider-%project-%repo
Version: 1.0.8
Release: alt1
Summary: Process markdown into manpages
Group: Development/Other
License: MIT
Url: https://%import_path
Source: %name-%version.tar
ExclusiveArch: %go_arches
Provides: %repo = %version-%release

BuildRequires(pre): rpm-build-golang

%description
%repo is a golang tool using blackfriday to process markdown into
manpages.

%package devel
Group: Development/Other
Summary: A golang registry for global request variables
BuildArch: noarch

Requires: golang(github.com/russross/blackfriday)
Provides: golang(%import_path/md2man) = %version-%release
Provides: golang(%import_path) = %version-%release

%description devel
%repo is a golang tool using blackfriday to process markdown into
manpages.

This package contains library source intended for building other packages
which use %project/%repo.

%package unit-test
Group: Development/Other
Summary: Unit tests for %name package

%description unit-test
%summary

This package contains unit tests for project
providing packages with %import_path prefix.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
pushd .build/src/%import_path
%gobuild -o bin/go-md2man %import_path
popd

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
pushd .build/src/%import_path
mkdir -p %buildroot%_bindir
install -p -m 755 bin/%repo %buildroot%_bindir
# generate man page
mkdir -p %buildroot%_man1dir
bin/go-md2man -in=go-md2man.1.md -out=go-md2man.1
install -p -m 644 go-md2man.1 %buildroot%_man1dir
# cleanup
rm -rf bin
popd

%golang_install

%files
%doc LICENSE.md
%doc README.md
%_bindir/%repo
%_man1dir/*

%files devel
%doc LICENSE.md
%doc README.md
%go_path/src/*

%changelog
* Fri Sep 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.0.8-alt1
- 1.0.8
- cleanup spec

* Fri Mar 30 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.7-alt0.M80P.1
- Backport to p8

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_1
- new version

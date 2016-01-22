%global import_path golang.org/x/tools
%global commit f3a63969dd29f8cfa913fdaea22f30c1ed537cb3
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_tooldir/*

Name:		golang-tools
Version:	0
Release:	alt4.git%abbrev
Summary:	Supplementary tools and packages for Go

Group:		Development/Other
License:	BSD
URL:		https://go.googlesource.com/tools

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

Requires:	golang

%description
The collection of developer tools.


%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch
Requires: golang

%description devel
%summary

This package contains library source intended for building other packages
which use the supplementary Go tools libraries with golang.org/x/ imports.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

rm -rf -- .build/src/%import_path/cmd/html2article
rm -rf -- .build/src/%import_path/cmd/present
rm -rf -- .build/src/%import_path/cmd/cover
rm -rf -- .build/src/%import_path/cmd/vet

cd .build/src/%import_path
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files
%_bindir/*

%files devel
%go_path/src/*

%changelog
* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt4.gitf3a63969
- New snapshot.

* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt3.gitd02228d1
- Use rpm-build-golang

* Sat Sep 26 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt2.gitd02228d1
- New snapshot.
- The vet and cover tools have been moved to golang.

* Mon Jul 06 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git7e09e072
- First build for ALTLinux.

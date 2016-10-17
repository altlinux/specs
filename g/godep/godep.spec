%global import_path github.com/tools/godep
%global commit 3c0ccb9a2415fbda40b982b622735906bcd1760f
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_tooldir/*

Name:		godep
Version:	74
Release:	alt1
Summary:	Utility to track dependencies

Group:		Development/Other
License:	BSD
URL:		https://github.com/golang/lint

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar

ExclusiveArch:	%go_arches
AutoReq:	nocpp

BuildRequires(pre): rpm-build-golang

BuildRequires:	golang

%description
Godep helps build packages reproducibly by fixing their dependencies.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*

%changelog
* Tue Oct 18 2016 Alexey Gladkov <legion@altlinux.ru> 74-alt1
- New shapshot.

* Thu May 05 2016 Alexey Gladkov <legion@altlinux.ru> 63-alt1
- First build for ALTLinux.

%global import_path github.com/kisielk/errcheck
%global commit 1cd10f9f7824cdbedd5175a6cea0da9763bbeece
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_tooldir/*

Name:		errcheck
Version:	0
Release:	alt2.git%abbrev
Summary:	Error checker for Go programs

Group:		Development/Other
License:	BSD
URL:		https://github.com/kisielk/errcheck

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: golang
BuildRequires: golang(github.com/kisielk/gotool)
BuildRequires: golang(golang.org/x/tools/go/loader)


%description
%{summary}

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

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
* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt2.git1cd10f9f
- New shapshot.

* Thu Nov 19 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git12fd1ab9
- First build for ALTLinux.

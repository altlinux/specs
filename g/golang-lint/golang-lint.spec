%global import_path github.com/golang/lint
%global commit cb00e5669539f047b2f4c53a421a01b0c8e172c6
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_tooldir/*

Name:		golang-lint
Version:	0
Release:	alt3.git%abbrev
Summary:	Linter for Go source code

Group:		Development/Other
License:	BSD
URL:		https://github.com/golang/lint

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	golang-lint-%version.tar

ExclusiveArch:	%go_arches
AutoReq:	nocpp

BuildRequires(pre): rpm-build-golang

BuildRequires:	golang
BuildRequires:	golang-tools-devel

%description
%{summary}

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path/golint
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*

%changelog
* Sat Apr 08 2017 Alexey Gladkov <legion@altlinux.ru> 0-alt3.gitcb00e566
- New snapshot.

* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt2.git32a87160
- New snapshot.
- Use rpm-build-golang.

* Mon Jul 06 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git7b7f4364
- First build for ALTLinux.

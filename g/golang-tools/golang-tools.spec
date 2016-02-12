%global import_path golang.org/x/tools
%global commit 789265387ff52550e7d48b4e6f4c6bce831c1248
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_root/bin/* %go_tooldir/*

Name:		golang-tools
Version:	0
Release:	alt5.git%abbrev
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

mkdir -p -- %buildroot/%go_root/bin
for f in %buildroot/%_bindir/*; do
	[ -x "$f" ] || continue
	f="${f##*/}"
	what="$(relative %_bindir/$f %go_root/bin/$f)"
	ln -s -- "$what" %buildroot/%go_root/bin/$f
done

# upstream commit 734737930440fc305a816e577cab457fbbc807c1 (rename oracle to guru)
rm -f -- %buildroot/%_bindir/oracle
ln -s -- guru %buildroot/%_bindir/oracle


%files
%_bindir/*
%go_root/bin/*

%files devel
%go_path/src/*

%changelog
* Fri Feb 12 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt5.git78926538
- New snapshot.

* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt4.gitf3a63969
- New snapshot.

* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 0-alt3.gitd02228d1
- Use rpm-build-golang

* Sat Sep 26 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt2.gitd02228d1
- New snapshot.
- The vet and cover tools have been moved to golang.

* Mon Jul 06 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git7e09e072
- First build for ALTLinux.

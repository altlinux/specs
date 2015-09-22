%global abbrev d02228d1

# build ids are not currently generated:
# https://code.google.com/p/go/issues/detail?id=5238
#
# also, debuginfo extraction currently fails with
# "Failed to write file: invalid section alignment"
%global __find_debuginfo_files %nil

# we are shipping the full contents of src in the data subpackage, which
# contains binary-like things (ELF data for tests, etc)
%global _unpackaged_files_terminate_build 1

%global go_arches %ix86 x86_64 %arm

%ifarch x86_64
%global gohostarch  amd64
%endif
%ifarch %{ix86}
%global gohostarch  386
%endif
%ifarch %{arm}
%global gohostarch  arm
%endif

%global go_version 1.5.1
%global go_path    %_libdir/golang
%global go_root    %_libdir/golang
%global go_tooldir %_libdir/golang/pkg/tool/linux_%gohostarch

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_tooldir/*

%def_disable check

Name:		golang-tools
Version:	0
Release:	alt2.git%abbrev
Summary:	Supplementary tools and packages for Go

Group:		Development/Other
License:	BSD
URL:		https://go.googlesource.com/tools

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	golang-tools-%version.tar

ExclusiveArch:	%go_arches
AutoReq:	nocpp

BuildRequires:	golang >= %go_version
Requires:	golang >= %go_version

%description
The collection of developer tools.


%package devel
Summary:	Libraries of supplementary Go tools
Group:		Development/Other
ExclusiveArch:	%go_arches
Requires:	golang >= %go_version

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go tools libraries with golang.org/x/ imports.


%prep
%setup -q

%build
export GOPATH="$PWD/.build:%go_path"

mkdir -p \
	.build/bin \
	.build/src/golang.org/x

ln -s $PWD .build/src/golang.org/x/tools

rm -rf -- .build/src/golang.org/x/tools/cmd/html2article
rm -rf -- .build/src/golang.org/x/tools/cmd/present
rm -rf -- .build/src/golang.org/x/tools/cmd/cover
rm -rf -- .build/src/golang.org/x/tools/cmd/vet

cd .build/bin
for d in ../src/golang.org/x/tools/cmd/*; do
	go build -a -v "$d"
done

%install
rm -rf -- rpm

mkdir -p -- %buildroot/%_bindir
mv -f -- .build/bin/* %buildroot/%_bindir/

mkdir -p -- %buildroot/%go_path/src/golang.org/x/tools
cp -av * %buildroot/%go_path/src/golang.org/x/tools/

# Cleanup
find %buildroot/%go_path/src \
	\( \
		\( -type d -name 'testdata'  \) -o \
		\( -type f -name 'Makefile'  \) -o \
		\( -type f -name '*_test.go' \) -o \
		\( -type f -name 'test_*'    \) -o \
		\( -type f -name 'test.'     \) \
	\) \
		-print0 |
	xargs -0 rm -rfv --

%files
%_bindir/*

%files devel
%go_path/src/golang.org/x/tools

%changelog
* Sat Sep 26 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt2.gitd02228d1
- New snapshot.
- The vet and cover tools have been moved to golang.

* Mon Jul 06 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git7e09e072
- First build for ALTLinux.

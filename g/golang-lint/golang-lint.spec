%global project_url github.com/golang/lint
%global abbrev 7b7f4364

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

%global go_path    %_libdir/golang
%global go_root    %_libdir/golang
%global go_tooldir %_libdir/golang/pkg/tool/linux_%gohostarch

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_tooldir/*

%def_disable check

Name:		golang-lint
Version:	0
Release:	alt1.git%abbrev
Summary:	Linter for Go source code

Group:		Development/Other
License:	BSD
URL:		https://github.com/golang/lint

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	golang-lint-%version.tar

ExclusiveArch:	%go_arches
AutoReq:	nocpp

BuildRequires:	golang >= 1.4.2
BuildRequires:	golang-tools-devel

%description
%{summary}


%package devel
Summary:	Libraries of linter for Go source code
Group:		Development/Other
ExclusiveArch:	%go_arches
Requires:	golang >= 1.4.2

%description devel
%{summary}


%prep
%setup -q


%build
export GOPATH="$PWD/.build:%go_path"

dirname="%project_url"
dirname="${dirname%%/*}"

mkdir -p \
	.build/bin \
	.build/src/$dirname

ln -s -- "$PWD" .build/src/%project_url

cd .build/bin
for d in ../src/%project_url/golint; do
	go build -a -v "$d"
done


%install
rm -rf -- rpm

mkdir -p -- %buildroot/%_bindir
mv -f -- .build/bin/* %buildroot/%_bindir/

mkdir -p -- %buildroot/%go_path/src/%project_url
cp -av * %buildroot/%go_path/src/%project_url

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
%go_path/src/%project_url

%changelog
* Mon Jul 06 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git7b7f4364
- First build for ALTLinux.

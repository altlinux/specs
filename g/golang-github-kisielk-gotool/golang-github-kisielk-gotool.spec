%global import_path github.com/kisielk/gotool
%global commit 58a7a198f2ec6ea7af221fd216e7f559d663ce02
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global _unpackaged_files_terminate_build 1

Name:		golang-github-kisielk-gotool
Version:	0
Release:	alt1.git%abbrev
Summary:	A library of some of the utility functions provided by (but not exported) by cmd/go
Group:		Development/Other
License:	MIT
URL:		https://%import_path
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-golang

%description
%summary

%package devel
Summary: %summary
Group: Development/Other
Requires: golang

%description devel
%summary

This package contains library source intended for building other
packages which use %import_path.

%prep
%setup -q

%build

%install
install -d -p %buildroot/%go_path/src/%import_path
cp -arv -- * %buildroot/%go_path/src/%import_path
rm -f -- %buildroot/%go_path/src/%import_path/{LEGAL,LICENSE,README.md}

(
	cd %buildroot
	find .%go_path/src -mindepth 1 -type d              -printf '%%%%dir %%%%attr(755,root,root) %%p\n'
	find .%go_path/src -mindepth 1 -type f -name '*.go' -printf '%%%%attr(644,root,root) %%p\n'
) | sed -e 's, \./, /,' >devel.file-list

%files devel -f devel.file-list

%changelog
* Thu Nov 19 2015 Alexey Gladkov <legion@altlinux.ru> 0-alt1.git58a7a198
- First build for ALTLinux.

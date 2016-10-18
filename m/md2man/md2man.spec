%global import_path github.com/legionus/md2man
Name: md2man
Version: 1.0
Release: alt1

Summary: md2man creates simple man pages from the markdown file
License: GPLv3+
Group: Development/Other
Url: https://github.com/legionus/md2man

Source: md2man-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Utility converts markdown to man page.

%prep
%setup

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
* Mon Oct 17 2016 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- First release.

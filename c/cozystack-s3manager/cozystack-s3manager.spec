%global import_path github.com/cloudlena/s3manager 
%define _unpackaged_files_terminate_build 1

%define git_rev 9a7c8e4
%define bname s3manager

Name:    cozystack-s3manager
Version: 0.5.0
Release: alt1.%git_rev

Summary: A Web GUI for your S3 buckets (Cozystack-customized)
License: Apache-2.0
Group:   Other
Url:     https://github.com/cloudlena/s3manager
Vcs:     https://github.com/cloudlena/s3manager.git

Conflicts: s3manager

Source:  %name-%version.tar
Source1: vendor.tar
Patch1:  %name-%version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
A Web GUI written in Go to manage S3 buckets from any provider.

%prep
%setup -a 1
%patch1 -p1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s"
export GOFLAGS="-trimpath"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
%gotest ./...

%files
%doc README.md LICENSE
%_bindir/%bname

%changelog
* Tue Jul 21 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.5.0-alt1.9a7c8e4
- Initial build for ALT.



%define _unpackaged_files_terminate_build 1
%global import_path github.com/dutchcoders/transfer.sh

Name:    transfer.sh
Version: 1.6.1
Release: alt1

Summary: Easy and fast file sharing from the command-line.
License: MIT
Group:   Other
Url:     https://github.com/dutchcoders/transfer.sh

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Easy and fast file sharing from the command-line. This code contains the server with everything you need to create your own instance.
Transfer.sh currently supports the s3 (Amazon S3), gdrive (Google Drive), storj (Storj) providers, and local file system (local).
Disclaimer
%prep
%setup -a1

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
%doc *.md
%_bindir/*

%changelog
* Tue Jan 28 2025 Artem Semenov <savoptik@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus

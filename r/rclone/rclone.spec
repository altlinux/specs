%global import_path github.com/ncw/rclone
Name:     rclone
Version:  1.46.0
Release:  alt1

Summary:  "rsync for cloud storage" - Google Drive, Amazon Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Cloudfiles, Google Cloud Storage, Yandex Files
License:  MIT
Group:    Other
Url:      https://github.com/ncw/rclone

Packager: Vitaly Chikunov <vt@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

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
%doc *.md

%changelog
* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.46.0-alt1
- Initial build for Sisyphus

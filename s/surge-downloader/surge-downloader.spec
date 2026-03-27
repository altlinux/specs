%define _unpackaged_files_terminate_build 1
%define upstream_name surge
%global import_path github.com/surge-downloader/surge

Name: surge-downloader
Version: 0.7.5
Release: alt1
Summary: Blazing fast TUI download manager built in Go for power users
License: MIT
Group: Networking/File transfer
Url: https://github.com/surge-downloader/Surge
Vcs: https://github.com/surge-downloader/Surge

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Surge is designed for power users who prefer a keyboard-driven workflow. It
features a beautiful Terminal User Interface (TUI), as well as a background
Headless Server and a CLI tool for automation.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/torrent.Version=%version"

%golang_prepare

cd .gopath/src/%import_path

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/%upstream_name

%changelog
* Fri Mar 27 2026 Vladislav Glinkin <smasher@altlinux.org> 0.7.5-alt1
- Initial build for ALT


%define _unpackaged_files_terminate_build 1
%define upstream_name surge
%global import_path github.com/surge-downloader/surge

Name: surge-downloader
Version: 0.8.7
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
%golang_prepare
cd $BUILDDIR/src/$IMPORT_PATH
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1

# lowercasing binary name
mv $BUILDDIR/bin/Surge $BUILDDIR/bin/surge
%golang_install

%files
%doc LICENSE README.md
%_bindir/%upstream_name

%changelog
* Fri Jun 05 2026 Vladislav Glinkin <smasher@altlinux.org> 0.8.7-alt1
- New version

* Fri Mar 27 2026 Vladislav Glinkin <smasher@altlinux.org> 0.7.5-alt1
- Initial build for ALT


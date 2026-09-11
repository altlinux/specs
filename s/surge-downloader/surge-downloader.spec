%define _unpackaged_files_terminate_build 1
%define import_path github.com/SurgeDM/Surge

Name: surge-downloader
Version: 0.12.1
Release: alt1

Summary: Blazing fast TUI download manager built in Go for power users
License: MIT
Group: Networking/File transfer
Url: https://github.com/SurgeDM/Surge
Vcs: https://github.com/SurgeDM/Surge.git

Source: %name-%version.tar
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

cd "$BUILDDIR/src/$IMPORT_PATH"
mkdir -p "$BUILDDIR/bin"

CGO_ENABLED=0 go build \
    -mod=vendor \
    -ldflags "-X %import_path/cmd.Version=%version" \
    -o "$BUILDDIR/bin/surge" \
    .

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1

%golang_install

%check
./.gopath/bin/surge --version | grep -F "%version"

%files
%doc LICENSE README.md
%_bindir/surge

%changelog
* Fri Sep 11 2026 Vladislav Glinkin <smasher@altlinux.org> 0.12.1-alt1
- New version 0.12.1.

* Fri Jun 05 2026 Vladislav Glinkin <smasher@altlinux.org> 0.8.7-alt1
- New version 0.8.7.

* Fri Mar 27 2026 Vladislav Glinkin <smasher@altlinux.org> 0.7.5-alt1
- Initial build for ALT
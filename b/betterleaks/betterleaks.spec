%define _unpackaged_files_terminate_build 1

%global import_path github.com/betterleaks/betterleaks

Name: betterleaks
Version: 1.3.1
Release: alt1
Summary: A Better Secrets Scanner built for configurability and speed
License: MIT
Group: Monitoring
Url: https://betterleaks.com/
Vcs: https://github.com/betterleaks/betterleaks

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Betterleaks is a tool for detecting secrets like passwords, API keys, and tokens
in git repos, files, and whatever else you wanna throw at it via stdin.

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
%_bindir/%name

%changelog
* Thu May 28 2026 Vladislav Glinkin <smasher@altlinux.org> 1.3.1-alt1
- New version

* Tue Mar 24 2026 Vladislav Glinkin <smasher@altlinux.org> 1.1.1-alt1
- Initial build for ALT


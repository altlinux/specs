%define _unpackaged_files_terminate_build 1

%global import_path github.com/gobuffalo/cli

Name: gobuffalo-cli
Version: 0.18.14
Release: alt1

Summary: The Buffalo CLI
License: Unlicense
Group: Development/Other
Url: https://gobuffalo.io
Vcs: https://github.com/gobuffalo/cli

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
A tool to develop, test and deploy your Buffalo applications.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/buffalo

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/*

%changelog
* Fri May 19 2023 Anton Zhukharev <ancieg@altlinux.org> 0.18.14-alt1
- Initial build for ALT Sisyphus.

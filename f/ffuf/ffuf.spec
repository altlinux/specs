%define _unpackaged_files_terminate_build 1

%global import_path github.com/ffuf/ffuf/v2

Name: ffuf
Version: 2.0.0
Release: alt1

Summary: Fast web fuzzer written in Go
License: MIT
Group: Networking/Other
Url: https://github.com/ffuf/ffuf
Vcs: https://github.com/ffuf/ffuf

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
%summary.

%prep
%setup

%build
export GO111MODULE=off
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

# fix installation name
mv %buildroot%_bindir/{v2,%name}

%files
%doc LICENSE README.md CHANGELOG.md ffufrc.example
%_bindir/%name

%changelog
* Thu Apr 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1
- Initial build for ALT Sisyphus.


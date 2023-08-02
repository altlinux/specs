%define _unpackaged_files_terminate_build 1

%global import_path github.com/exercism/cli

Name: exercism-cli
Version: 3.2.0
Release: alt1

Summary: A Go based command line tool for exercism.org
License: MIT
Group: Education
Url: https://github.com/exercism/cli

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
The CLI is the link between the Exercism website and your local work
environment. It lets you download exercises and submit your solution
to the site.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build exercism

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc LICENSE CHANGELOG.md README.md
%_bindir/*

%changelog
* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.0-alt1
- Updated to 3.2.0.

* Sun May 14 2023 Anton Zhukharev <ancieg@altlinux.org> 3.1.0-alt1
- Initial build for ALT Sisyphus.

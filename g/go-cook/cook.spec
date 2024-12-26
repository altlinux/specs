%define _unpackaged_files_terminate_build 1
%define import_path github.com/glitchedgitz/cook

Name: go-cook
Version: 2.2.1
Release: alt1

Summary: A wordlist framework to fullfill your kinks with your wordlists. For security researchers, bug bounty and hackers
License: MIT
Group: File tools
Url: https://github.com/glitchedgitz/cook
Vcs: https://github.com/glitchedgitz/cook
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
An overpower wordlist generator, splitter, merger, finder, saver, create words
permutation and combinations, apply different encoding/decoding and everything
you need.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH/v2
%golang_build cmd/cook
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/cook
%doc README.md LICENSE

%changelog
* Thu Dec 26 2024 Artem Krasovskiy <aibure@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus


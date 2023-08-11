%define _unpackaged_files_terminate_build 1

%global import_path github.com/chriswalz/bit

Name: bit
Version: 1.1.2
Release: alt1

Summary: Bit is a modern Git CLI
License: Apache-2.0
Group: Development/Other
Url: https://pkg.go.dev/github.com/chriswalz/bit
Vcs: https://github.com/chriswalz/bit
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

Requires: git

BuildRequires(pre): rpm-build-golang

%description
bit is an experimental modernized git CLI built on top of git that provides
happy defaults and other niceties:

* command and flag suggestions to help you navigate the plethora of options
git provides you
* autocompletion for files and branch names when using bit add or bit checkout
* automatic fetch and branch fast-forwarding reducing the likelihood of merge
conflicts
* suggestions work with git aliases
* new commands like bit sync that vastly simplify your workflow
* commands from git-extras such as bit release & bit info
* fully compatible with git allowing you to fallback to git if need be.
* get insight into how bit works using bit --debug.

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
%doc LICENSE README.md
%_bindir/%name

%changelog
* Wed Aug 09 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus


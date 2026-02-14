%define _unpackaged_files_terminate_build 1
%define import_path github.com/antonmedv/fx/%version

Name: fx
Version: 39.2.0
Release: alt1

Summary: Terminal JSON viewer & processor
License: MIT
Group: Text tools
Url: https://fx.wtf
Vcs: https://github.com/antonmedv/fx.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Fx is a CLI for JSON: it shows JSON interactively in your terminal, and lets you
transform JSON with JavaScript.

%prep
%setup -a1

%build
export GOROOT=/usr/lib/golang
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X '%import_path/config.Vendor=%vendor'"
%golang_build  .
popd

%install
export GOROOT=%_libexecdir/golang
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md LICENSE
%_bindir/fx

%changelog
* Wed Jan 22 2026 Grant Makyan <karonus@altlinux.org> 39.2.0-alt1
- First build for ALT.

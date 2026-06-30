%define _unpackaged_files_terminate_build 1

%define import_path github.com/arduino/arduino-language-server
%define version_package %import_path/version

Name: arduino-language-server
Version: 0.7.7
Release: alt1

Summary: Arduino Language Server
License: AGPL-3.0
Group: Development/Tools
Url: https://github.com/arduino/arduino-language-server
Vcs: https://github.com/arduino/arduino-language-server.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Arduino Language Server provides Language Server Protocol support for Arduino
sketches. It powers autocompletion and language features in Arduino IDE and can
be used by other editors that support LSP.

%prep
%setup -a1

%build
export GOROOT=%_libexecdir/golang
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd "$BUILDDIR/src/$IMPORT_PATH"
%golang_build .
popd

%install
export GOROOT=%_libexecdir/golang
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE.txt README.md
%_bindir/arduino-language-server

%changelog
* Mon Jun 29 2026 Grant Makyan <karonus@altlinux.org> 0.7.7-alt1
- Initial build for ALT.

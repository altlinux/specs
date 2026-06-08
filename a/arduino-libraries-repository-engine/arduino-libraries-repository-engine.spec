%define _unpackaged_files_terminate_build 1
%define import_path github.com/arduino/libraries-repository-engine

Name: arduino-libraries-repository-engine
Version: 1.2.2
Release: alt1

Summary: Arduino Library Manager index generator
License: GPLv3+
Group: Development/Tools
Url: https://github.com/arduino/libraries-repository-engine
Vcs: https://github.com/arduino/libraries-repository-engine.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
This is a CLI tool used to generate and maintain the
Arduino Library Manager index.

It processes the registered library repositories, extracts library metadata,
updates the library database, and produces the JSON index consumed by Arduino
tools.

%prep
%setup -a1

%build
export GOROOT=/usr/lib/golang
export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path

%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X '%import_path/config.Vendor=%vendor'"
%golang_build  .
popd

%install
export GOROOT=/usr/lib/golang
export BUILDDIR=$PWD/.build
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE.txt
%_bindir/libraries-repository-engine

%changelog
* Fri Jun 05 2026 Grant Makyan <karonus@altlinux.org> 1.2.2-alt1
- First build for ALT.

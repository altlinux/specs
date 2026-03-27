%define _unpackaged_files_terminate_build 1
%global import_path github.com/google/pprof

Name: pprof
Version: 0.0.0.gita15ffb7
Release: alt1
Summary: CLI tool for visualization and analysis of profiling data.
License: Apache-2.0
Group: Development/Other
Url: https://github.com/google/pprof

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%name is a tool for visualization and analysis of profiling data.

%name reads a collection of profiling samples in profile.proto 
format and generates reports to visualize and help analyze the data. 
It can generate both text and graphical reports (through the use of 
the dot visualization package).

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot%_datadir/%name
%golang_install

%files
%doc README.md CONTRIBUTORS CONTRIBUTING.md AUTHORS
%_bindir/%name


%changelog
* Fri Mar 27 2026 Pavel Shilov <zerospirit@altlinux.org> 0.0.0.gita15ffb7-alt1
- Initial build for Sisyphus.


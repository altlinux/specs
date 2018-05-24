%define _unpackaged_files_terminate_build 1
%define import_path github.com/evilsocket/ftrace


Name: golang-ftrace
Version: 1.2.0
Release: alt1%ubt
Summary: Go library to trace Linux syscalls using the FTRACE kernel framework.
License: GPLv3
Group: Development/Other
Url: https://github.com/evilsocket/ftrace

# https://github.com/evilsocket/ftrace.git
Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: golang-tools-devel

%description
ftrace utilizes the FTRACE kernel framework
in order to trace system calls and kernel events from user space.

%package devel
Summary: Go library to trace Linux syscalls using the FTRACE kernel framework.
Group: Development/Other
BuildArch: noarch
Requires: golang

%description devel
ftrace utilizes the FTRACE kernel framework
in order to trace system calls and kernel events from user space.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

find .build/src/%import_path -type f ! -name '*.go' -delete

pushd .build/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files devel
%doc LICENSE README.md
%go_path/src/*

%changelog
* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1%ubt
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%global import_path github.com/bazelbuild/bazelisk
Name:    bazelisk
Version: 1.26.0
Release: alt1

Summary: A user-friendly launcher for Bazel.
License: Apache-2.0
Group:   Other
URL:     https://bazel.build/
VCS:     https://github.com/bazelbuild/bazelisk

Source: %name-%version.tar
Source1: vendor.tar
Patch0: go-version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Bazelisk is a wrapper for Bazel written in Go.

It automatically picks a good version of Bazel given your
current working directory, downloads it from the official
server (if required) and then transparently passes through
all command-line arguments to the real Bazel binary.

You can call it just like you would call Bazel.


%prep
%setup
%patch0 -p1
tar -xf %SOURCE1

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
%doc *.md
%_bindir/*

%changelog
* Tue Aug 12 2025 Artem Semenov <savoptik@altlinux.org> 1.26.0-alt1
- Initial build for Sisyphus

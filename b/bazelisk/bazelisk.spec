%define _unpackaged_files_terminate_build 1

%global import_path github.com/bazelbuild/bazelisk
Name: bazelisk
Version: 1.29.0
Release: alt1

Summary: A user-friendly launcher for Bazel
License: Apache-2.0
Group: Other
Url: https://bazel.build/
VCS: https://github.com/bazelbuild/bazelisk.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Bazelisk is a wrapper for Bazel written in Go.

It automatically picks a good version of Bazel given your current
working directory, downloads it from the official server (if required)
and then transparently passes through all command-line arguments to the
real Bazel binary.

You can call it just like you would call Bazel.

%prep
%setup
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
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/*

%changelog
* Wed May 13 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.29.0-alt1
- Updated to 1.29.0

* Tue Aug 12 2025 Artem Semenov <savoptik@altlinux.org> 1.26.0-alt1
- Initial build for Sisyphus

%define _unpackaged_files_terminate_build 1
%define compat_version 2.22.5
%define compat_dir bazel-lib-compat-%compat_version

Name: bazel-lib
Version: 3.8.0
Release: alt1
%global main_version %version

Summary: Starlark rules and native file utilities for Bazel
License: Apache-2.0 AND BSD-3-Clause AND MIT
Group: Development/Other
URL: https://github.com/bazel-contrib/bazel-lib
VCS: https://github.com/bazel-contrib/bazel-lib.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %compat_dir.tar
Source3: upstream-tests.tar
Source4: compat-tests.tar
Source5: compat-smoke.tar
Patch0: go_dev_dep.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: rpm-build-python3

%description
Starlark rules and utility APIs for working with files, directories, strings,
runfiles and build actions. Provides the genuine bazel_lib module and original
sources. Native file-copy, template and process helpers are compiled offline
from the original Go sources with their vendored upstream dependencies.

%package -n bazel-aspect-lib
Version: %compat_version
Summary: Genuine aspect_bazel_lib compatibility APIs for Bazel
Group: Development/Other
BuildArch: noarch

%description -n bazel-aspect-lib
Original aspect_bazel_lib 2.22.5 sources and Starlark APIs from the
same upstream project, for existing consumers of the older module name.

%prep
%setup -a1 -a2
%autopatch -p1
patch -d %compat_dir -p1 < %compat_dir/.bcr/patches/go_dev_dep.patch
sed -i '/name = "bazel_lib",/a\    version = "%main_version",' \
    MODULE.bazel
sed -i '/name = "aspect_bazel_lib",/a\    version = "%compat_version",' \
    %compat_dir/MODULE.bazel
# Restore genuine upstream files omitted by git archive export-ignore.
tar -xf %SOURCE3 -C .
tar -xf %SOURCE4 -C %compat_dir
tar -xf %SOURCE5 -C %compat_dir

%build
export BUILDDIR="$PWD/.build"
export GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local GOMAXPROCS=2
export GOFLAGS="-p=2 -trimpath -buildmode=pie"
%golang_build tools/copy_directory tools/copy_to_directory \
    tools/expand_template tools/spawn_binary

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export RPM_BINDIR=%_libexecdir/%name
%golang_install

mkdir -p licenses/rules_go licenses/doublestar licenses/x-exp licenses/x-sys
cp -a vendor/github.com/bazelbuild/rules_go/LICENSE.txt \
    vendor/github.com/bazelbuild/rules_go/AUTHORS \
    vendor/github.com/bazelbuild/rules_go/CONTRIBUTORS licenses/rules_go/
cp -a vendor/github.com/bmatcuk/doublestar/v4/LICENSE licenses/doublestar/
cp -a vendor/golang.org/x/exp/LICENSE vendor/golang.org/x/exp/PATENTS \
    licenses/x-exp/
cp -a vendor/golang.org/x/sys/LICENSE vendor/golang.org/x/sys/PATENTS \
    licenses/x-sys/

install -d %buildroot%_datadir/bazel/rules/bazel_lib
cp -a BUILD.bazel MODULE.bazel bzl_library.bzl deps.bzl lib tools \
    go.mod go.sum %buildroot%_datadir/bazel/rules/bazel_lib/

install -d %buildroot%_datadir/bazel/rules/aspect_bazel_lib
cp -a %compat_dir/BUILD.bazel %compat_dir/MODULE.bazel \
    %compat_dir/WORKSPACE.bazel %compat_dir/bzl_library.bzl \
    %compat_dir/deps.bzl %compat_dir/lib %compat_dir/tools \
    %compat_dir/go.mod %compat_dir/go.sum \
    %buildroot%_datadir/bazel/rules/aspect_bazel_lib/

%check
export GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local GOMAXPROCS=2
export GOFLAGS="-mod=vendor -p=2"
export RUNFILES_DIR="$PWD/.runfiles"
mkdir -p .runfiles
ln -s "$PWD" .runfiles/_main
%gotest ./tools/common ./tools/spawn_binary
%gotest ./tools/copy_to_directory -args \
    -copy-tool=%buildroot%_libexecdir/%name/copy_to_directory

%files
%dir %_libexecdir/%name
%_libexecdir/%name/copy_directory
%_libexecdir/%name/copy_to_directory
%_libexecdir/%name/expand_template
%_libexecdir/%name/spawn_binary
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/bazel_lib
%doc LICENSE licenses

%files -n bazel-aspect-lib
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/aspect_bazel_lib

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 3.8.0-alt1
- Initial build for ALT.

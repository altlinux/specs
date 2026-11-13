%define _unpackaged_files_terminate_build 1
%define module_name diff.bzl

Name: bazel-diff-bzl
Version: 0.6.1
Release: alt1

Summary: Diffutils rules and toolchain definitions for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/kormide/diff.bzl
VCS: https://github.com/kormide/diff.bzl.git
BuildArch: noarch

Source0: %name-%version.tar

%description
Genuine diff.bzl Starlark rules and repository/toolchain interfaces.
The complete upstream source is preserved. Execution tools are supplied
separately; this package does not contain prebuilt SDK or formatter binaries.

%prep
%setup
sed -i '/module(name =/c\module(name = "diff.bzl", version = "%version")' \
    MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/%module_name
cp -a BUILD.bazel MODULE.bazel REPO.bazel LICENSE diff.bzl diff \
    %buildroot%_datadir/bazel/rules/%module_name/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/%module_name
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.6.1-alt1
- Initial build for ALT.

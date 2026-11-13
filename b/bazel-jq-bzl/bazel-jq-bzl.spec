%define _unpackaged_files_terminate_build 1
%define module_name jq.bzl

Name: bazel-jq-bzl
Version: 0.7.2
Release: alt1

Summary: Jq rules and toolchain definitions for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/jq.bzl
VCS: https://github.com/bazel-contrib/jq.bzl.git
BuildArch: noarch

Source0: %name-%version.tar

%description
Genuine jq.bzl Starlark rules and repository/toolchain interfaces.
The complete upstream source is preserved. Execution tools are supplied
separately; this package does not contain prebuilt SDK or formatter binaries.

%prep
%setup
sed -i '/name = "jq.bzl",/a\    version = "%version",' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/%module_name
cp -a BUILD.bazel MODULE.bazel REPO.bazel jq.bzl jq \
    %buildroot%_datadir/bazel/rules/%module_name/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/%module_name
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.7.2-alt1
- Initial build for ALT.

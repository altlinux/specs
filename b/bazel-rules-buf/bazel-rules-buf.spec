%define _unpackaged_files_terminate_build 1
%define module_name rules_buf

Name: bazel-rules-buf
Version: 0.6.1
Release: alt1

Summary: Buf protocol buffer rules and toolchain interfaces for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bufbuild/rules_buf
VCS: https://github.com/bufbuild/rules_buf.git
BuildArch: noarch

Source0: %name-%version.tar

%description
Genuine rules_buf Starlark rules and repository/toolchain interfaces.
The complete upstream source is preserved. Execution tools are supplied
separately; this package does not contain prebuilt SDK or formatter binaries.

%prep
%setup
sed -i 's/version = "0.0.0"/version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/%module_name
cp -a BUILD.bazel MODULE.bazel WORKSPACE repositories.bzl go.mod go.sum \
    buf tools gazelle \
    %buildroot%_datadir/bazel/rules/%module_name/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/%module_name
%doc LICENSE

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 0.6.1-alt1
- Initial build for ALT.

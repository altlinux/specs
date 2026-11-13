%define _unpackaged_files_terminate_build 1

Name: bazel-toml
Version: 0.5.0
Release: alt1

Summary: TOML parsing and serialization for Bazel Starlark
License: Apache-2.0
Group: Development/Other
URL: https://github.com/jvolkman/toml.bzl
VCS: https://github.com/jvolkman/toml.bzl.git
BuildArch: noarch

Source0: %name-%version.tar
%description
Pure Starlark TOML parser and serializer for Bazel. Provides the genuine
toml.bzl module, including datetime support and native module metadata.

%prep
%setup
sed -i '/compatibility_level = 1,/a\    version = "%version",' MODULE.bazel

%install
install -d %buildroot%_datadir/bazel/rules/toml.bzl
cp -a MODULE.bazel REPO.bazel BUILD.bazel WORKSPACE.bazel toml.bzl toml \
    %buildroot%_datadir/bazel/rules/toml.bzl/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/toml.bzl
%doc LICENSE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.5.0-alt1
- Initial build for ALT.

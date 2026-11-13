%define _unpackaged_files_terminate_build 1

Name: bazel-with-cfg
Version: 1.1.0
Release: alt1

Summary: Bazel Starlark rule variants with configuration transitions
License: Apache-2.0
Group: Development/Other
URL: https://github.com/fmeum/with_cfg.bzl
VCS: https://github.com/fmeum/with_cfg.bzl.git
BuildArch: noarch

Source0: %name-%version.tar
%description
The genuine with_cfg.bzl Starlark module creates variants of existing Bazel
rules with configuration transitions. Its builder supports setting and
extending options, cloning configurations and resetting selected dependencies.

%prep
%setup
sed -i '0,/version = "0.0.0"/s//version = "%version"/' MODULE.bazel

%install
install -d %buildroot%_datadir/bazel/rules/with_cfg.bzl
cp -a BUILD.bazel MODULE.bazel WORKSPACE.bazel WORKSPACE.bzlmod \
    with_cfg.bzl with_cfg %buildroot%_datadir/bazel/rules/with_cfg.bzl/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/with_cfg.bzl
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

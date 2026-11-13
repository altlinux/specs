%define _unpackaged_files_terminate_build 1

Name: bazel-rules-multirun
Version: 0.14.0
Release: alt1

Summary: Bazel command composition rules and Python runner
License: Apache-2.0
Group: Development/Other
URL: https://github.com/keith/rules_multirun
VCS: https://github.com/keith/rules_multirun.git
BuildArch: noarch

Source0: %name-%version.tar

Requires: python3-module-bazel-runfiles

BuildRequires: python3
BuildRequires: python3-module-bazel-runfiles

BuildRequires: rpm-build-python3

%description
Genuine rules_multirun Starlark rules compose Bazel commands and pass their
arguments, environment and runfiles to a Python controller. Supports serial
or parallel execution, buffered output, stdin forwarding and failure handling.

%prep
%setup
sed -i '0,/version = "0"/s//version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/rules_multirun
cp -a BUILD MODULE.bazel WORKSPACE WORKSPACE.bzlmod *.bzl internal tests \
    %buildroot%_datadir/bazel/rules/rules_multirun/


# Keep upstream documentation in SOURCE; do not install README files.
find %buildroot%_datadir/bazel -iname 'README*' -delete

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_multirun
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.14.0-alt1
- Initial build for ALT.

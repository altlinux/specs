%define _unpackaged_files_terminate_build 1

Name: bazel-rules-swift
Version: 4.2.2
Release: alt1

Summary: Swift rules and provider APIs for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazelbuild/rules_swift
VCS: https://github.com/bazelbuild/rules_swift.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: module_dot_bazel_version.patch

BuildRequires: python3
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-perl

# This diagnostic rejects Linux and is retained only as upstream source data.
%add_findreq_skiplist %_datadir/bazel/rules/rules_swift/tools/dump_toolchains/dump_toolchains.sh

%description
Bazel Starlark rules, provider APIs and original tool sources for Swift.
Provides the genuine rules_swift module, including SwiftInfo propagation
and Swift/C/C++ interoperation metadata.

%prep
%setup
%autopatch -p1

%build

%install
install -d %buildroot%_datadir/bazel/rules/rules_swift
cp -a BUILD MODULE.bazel LICENSE AUTHORS swift proto mixed_language \
    toolchains tools third_party \
    %buildroot%_datadir/bazel/rules/rules_swift/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_swift
%doc LICENSE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 4.2.2-alt1
- Initial build for ALT.

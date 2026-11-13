%define _unpackaged_files_terminate_build 1

Name: bazel-xml-bzl
Version: 0.2.3
Release: alt1

Summary: Pure Starlark XML parser, DOM and builder for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/scottpledger/xml.bzl
VCS: https://github.com/scottpledger/xml.bzl.git
BuildArch: noarch

Source0: %name-%version.tar

%description
The genuine xml.bzl module parses and builds XML documents in Starlark.
It provides DOM navigation, entity decoding, serialization and strict or
lenient error handling for Bazel configuration consumers.

%prep
%setup
sed -i '0,/version = ""/s//version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/xml.bzl
cp -a BUILD.bazel MODULE.bazel REPO.bazel WORKSPACE.bazel LICENSE \
    xml.bzl private tests %buildroot%_datadir/bazel/rules/xml.bzl/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/xml.bzl
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.2.3-alt1
- Initial build for ALT.

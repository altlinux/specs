%define _unpackaged_files_terminate_build 1

Name: bazel-features
Version: 1.54.1
Release: alt1

Summary: Bazel feature detection Starlark library
License: Apache-2.0
Group: Development/Other
Url: https://github.com/bazel-contrib/bazel_features
VCS: https://github.com/bazel-contrib/bazel_features.git

Source0: %name-%version.tar
Patch0: %name-%version-alt-module-version.patch
BuildArch: noarch

%description
Starlark feature detection for Bazel versions, including repository extensions
that expose the features and native globals available in the running Bazel.
The source module is installed for use with a local_path_override. Consumers
provide Bazel and transitive modules separately for offline builds.

%prep
%setup
%autopatch -p1

%build
# Starlark source data is evaluated by the consuming Bazel process.

%install
install -d %buildroot%_datadir/bazel/rules/bazel_features
cp -a BUILD.bazel MODULE.bazel WORKSPACE.bazel WORKSPACE.bzlmod \
    LICENSE deps.bzl features.bzl private test \
    %buildroot%_datadir/bazel/rules/bazel_features/
find %buildroot%_datadir/bazel/rules/bazel_features -type d -exec chmod 755 {} +
find %buildroot%_datadir/bazel/rules/bazel_features -type f -exec chmod 644 {} +

# Upstream loading tests are run against the installed module with the shared
# offline Bazel fixture; their dependency closure is not part of this RPM.

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

%files
%doc LICENSE CONTRIBUTING.md
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/bazel_features/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.54.1-alt1
- Initial build for ALT.

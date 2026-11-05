%define _unpackaged_files_terminate_build 1

%define skylib_tests %_datadir/bazel/rules/bazel_skylib/tests

%add_findreq_skiplist %skylib_tests/analysis_test_test.sh
%add_findreq_skiplist %skylib_tests/common_settings_test.sh
%add_findreq_skiplist %skylib_tests/diff_test/diff_test_tests.sh
%add_findreq_skiplist %skylib_tests/unittest_test.sh

Name: bazel-skylib
Version: 1.9.2
Release: alt1

Summary: Common Starlark libraries and rules for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazelbuild/bazel-skylib
VCS: https://github.com/bazelbuild/bazel-skylib.git

Source0: %name-%version.tar

BuildArch: noarch

%description
Common Starlark functions, build rules and test support for Bazel.
The source module is installed for local_path_override consumers. Bazel
and external modules are supplied separately by the consuming build.

%prep
%setup

%build
# Starlark sources are evaluated by the consuming Bazel instance.

%install
install -d %buildroot%_datadir/bazel/rules/bazel_skylib
cp -a AUTHORS BUILD CHANGELOG.md CODEOWNERS CONTRIBUTORS LICENSE \
    MODULE.bazel MODULE.bazel-remove-override.patch README.md \
    WORKSPACE WORKSPACE.bzlmod *.bzl lib rules tests toolchains \
    gazelle distribution docs \
    %buildroot%_datadir/bazel/rules/bazel_skylib/
chmod -R u+rwX,go+rX,go-w %buildroot%_datadir/bazel/rules/bazel_skylib

# Installed-module upstream tests use the separately prepared offline Bazel
# dependency fixture and are recorded in the package verification report.

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

%files
%doc LICENSE AUTHORS CONTRIBUTORS CHANGELOG.md
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/bazel_skylib/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.9.2-alt1
- Initial build for ALT.

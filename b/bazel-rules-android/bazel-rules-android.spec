%define _unpackaged_files_terminate_build 1

Name: bazel-rules-android
Version: 0.8.1
Release: alt1

Summary: Android rules and provider APIs for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazelbuild/rules_android
VCS: https://github.com/bazelbuild/rules_android.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: python3
BuildRequires: python3-module-absl-py
BuildRequires: rpm-build-python3

%description
Bazel Starlark rules, provider APIs and original tool sources for Android.
Provides the genuine rules_android module and Python tools for AAR/JAR
resource extraction and archive processing.

%prep
%setup

%build

%install
install -d %buildroot%_datadir/bazel/rules/rules_android
cp -a BUILD MODULE.bazel LICENSE AUTHORS CONTRIBUTORS WORKSPACE \
    WORKSPACE.bzlmod go.mod go.sum *_install.json \
    android_persistent_workers.bazelrc robolectric-bazel.patch \
    defs.bzl defs_dev.bzl prereqs.bzl android bzlmod_extensions contrib \
    flags groups mobile_install providers py_support rules src third_party \
    toolchains tools %buildroot%_datadir/bazel/rules/rules_android/

# Preserve upstream documentation in SOURCE.
find %buildroot%_datadir/bazel -iname 'README*' -delete

%check
# junction_test requires Bazel-intrinsic src.test.py.bazel.test_base.
for suite in \
    tools.android.aar_embedded_jars_extractor_test \
    tools.android.aar_embedded_proguard_extractor_test \
    tools.android.aar_native_libs_zip_creator_test \
    tools.android.aar_resources_extractor_test \
    tools.android.jar_embedded_proguard_extractor_test
do
    export TEST_TMPDIR="$PWD/.test-tmp/$suite"
    mkdir -p "$TEST_TMPDIR"
    python3 -m unittest -v "$suite"
done

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_android
%doc LICENSE

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 0.8.1-alt1
- Initial build for ALT.

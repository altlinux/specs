%define _unpackaged_files_terminate_build 1

Name: bazel-rules-cc
Version: 0.2.27
Release: alt1

Summary: C and C++ rules and runfiles sources for Bazel
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/bazelbuild/rules_cc
VCS: https://github.com/bazelbuild/rules_cc.git

Source0: %name-%version.tar
Patch0: %name-%version-module-version.patch

BuildArch: noarch
AutoReqProv: no

BuildRequires: gcc-c++ libgtest-devel

%description
The complete upstream rules_cc module supplies C and C++ rules, toolchain
configuration and the C++ runfiles source library for offline Bazel builds.
Consumers provide Bazel, compilers and transitive modules separately.
The runfiles library sources may also be compiled by native consumers.

%prep
%setup
%autopatch -p1

%build
# Source data is evaluated and compiled by consuming builds.

%install
install -d %buildroot%_datadir/bazel/rules/rules_cc
cp -a . %buildroot%_datadir/bazel/rules/rules_cc/
find %buildroot%_datadir/bazel/rules/rules_cc \
    -type f -iname '*readme*' -delete
rm %buildroot%_datadir/bazel/rules/rules_cc/LICENSE
ln -s %_defaultdocdir/%name-%version/LICENSE \
    %buildroot%_datadir/bazel/rules/rules_cc/LICENSE

%check
grep -q 'name = "rules_cc"' MODULE.bazel
grep -q 'version = "%version"' MODULE.bazel
# Preserve the actual public include prefix without changing upstream code.
mkdir -p runfiles-test-include runfiles-test-tmp
ln -s "$PWD" runfiles-test-include/rules_cc
g++ %optflags -std=c++17 -Irunfiles-test-include \
    cc/runfiles/runfiles.cc tests/runfiles/runfiles_test.cc \
    -lgtest_main -lgtest -pthread -o runfiles-test
TEST_TMPDIR="$PWD/runfiles-test-tmp" ./runfiles-test
test "$(readlink %buildroot%_datadir/bazel/rules/rules_cc/LICENSE)" = \
    "%_defaultdocdir/%name-%version/LICENSE"

%files
%doc LICENSE
%_datadir/bazel/rules/rules_cc

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.2.27-alt1
- Initial build for ALT.

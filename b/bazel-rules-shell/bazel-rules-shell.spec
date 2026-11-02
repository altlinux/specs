%define _unpackaged_files_terminate_build 1

Name: bazel-rules-shell
Version: 0.8.0
Release: alt1

Summary: Shell rules and runfiles library for Bazel
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/bazelbuild/rules_shell
VCS: https://github.com/bazelbuild/rules_shell.git

Source0: %name-%version.tar
Patch0: %name-%version-module-version.patch

BuildArch: noarch
AutoReqProv: no

%description
The complete upstream rules_shell module provides shell binary, library and
test rules, local shell toolchain discovery and the Bash runfiles library.
It is installed as a real versioned module for offline Bazel integration.
Bazel and transitive modules are supplied separately by consumers.

%prep
%setup
%autopatch -p1

%build
# Starlark and shell sources are evaluated by the consuming Bazel process.

%install
install -d %buildroot%_datadir/bazel/rules/rules_shell
cp -a . %buildroot%_datadir/bazel/rules/rules_shell/
find %buildroot%_datadir/bazel/rules/rules_shell \
    -type f -iname '*readme*' -delete
rm %buildroot%_datadir/bazel/rules/rules_shell/LICENSE
ln -s %_defaultdocdir/%name-%version/LICENSE \
    %buildroot%_datadir/bazel/rules/rules_shell/LICENSE

%check
grep -q 'name = "rules_shell"' MODULE.bazel
grep -q 'version = "%version"' MODULE.bazel
test -s shell/runfiles/runfiles.bash
test -s shell/sh_binary.bzl
test -s shell/sh_test.bzl
test -s tests/runfiles/runfiles_test.bash
test "$(readlink %buildroot%_datadir/bazel/rules/rules_shell/LICENSE)" = \
    "%_defaultdocdir/%name-%version/LICENSE"
# The original Bazel tests run separately against the installed RPM.

%files
%doc LICENSE
%_datadir/bazel/rules/rules_shell

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.8.0-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

Name: bazel-rules-license
Version: 1.0.0
Release: alt1

Summary: Official license and package metadata rules for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazelbuild/rules_license
VCS: https://github.com/bazelbuild/rules_license.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: rpm-build-python3

# Consumers provide Bazel; this script only checks upstream source archives.
%add_findreq_skiplist %_datadir/bazel/rules/rules_license/distro/check_build.sh

%description
Complete source of the official rules_license module, including SPDX license
definitions, license and package providers, examples, tools and tests.
Consumers supply Bazel and any additional toolchains needed by their targets.

This is the stable rules_license API used by existing Bazel modules. Active
development moved to bazel-contrib/supply-chain, whose modified rules_license
module has a separate compatibility contract.

%prep
%setup

%build
# These Starlark sources are evaluated by the consuming Bazel process.

%install
install -d %buildroot%_datadir/bazel/rules/rules_license
cp -a . %buildroot%_datadir/bazel/rules/rules_license/
find %buildroot%_datadir/bazel/rules/rules_license -type d -exec chmod 755 {} +
find %buildroot%_datadir/bazel/rules/rules_license -type f \
    -exec chmod u+rw,go+r,go-w {} +
find %buildroot%_datadir/bazel/rules/rules_license \
    \( -type f -o -type l \) -iname '*readme*' -delete
# Preserve the build-input path while storing this license text only in docs.
rm %buildroot%_datadir/bazel/rules/rules_license/LICENSE
ln -s %_defaultdocdir/%name-%version/LICENSE \
    %buildroot%_datadir/bazel/rules/rules_license/LICENSE

%files
%doc LICENSE
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_license/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- Initial build for ALT.

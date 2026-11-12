%define _unpackaged_files_terminate_build 1

Name: bazel-package-metadata
Version: 0.0.15
Release: alt1

Summary: Package and license metadata rules for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/supply-chain
VCS: https://github.com/bazel-contrib/supply-chain.git

Source0: %name-%version.tar

BuildArch: noarch

%description
Starlark modules and tools for collecting Bazel package and license metadata,
including package URLs, license rules, metadata extensions and supply-chain
utilities. The primary module keeps its established path; sibling modules are
installed together under the supply-chain source tree.

%prep
%setup

%build
# Bazel evaluates these source rules in the consuming build.

%install
install -d %buildroot%_datadir/bazel/rules/package_metadata \
    %buildroot%_datadir/bazel/rules/supply-chain
cp -a metadata/. %buildroot%_datadir/bazel/rules/package_metadata/
cp -a LICENSE README.md docs examples lib metadata-extensions rules_license \
    tests tools %buildroot%_datadir/bazel/rules/supply-chain/
ln -s ../package_metadata \
    %buildroot%_datadir/bazel/rules/supply-chain/metadata
chmod -R u+rwX,go+rX,go-w \
    %buildroot%_datadir/bazel/rules/package_metadata \
    %buildroot%_datadir/bazel/rules/supply-chain

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

# Preserve the source-provider license path without a second installed copy.
rm %buildroot%_datadir/bazel/rules/supply-chain/LICENSE
ln -s %_defaultdocdir/%name-%version/LICENSE \
    %buildroot%_datadir/bazel/rules/supply-chain/LICENSE

%files
%doc LICENSE
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/package_metadata/
%_datadir/bazel/rules/supply-chain/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.0.15-alt1
- Initial build for ALT.

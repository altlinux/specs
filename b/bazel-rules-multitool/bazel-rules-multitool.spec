%define _unpackaged_files_terminate_build 1
%define module_name rules_multitool

Name: bazel-rules-multitool
Version: 1.11.1
Release: alt1

Summary: Bazel tool hub repository and lockfile rules
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/rules_multitool
VCS: https://github.com/bazel-contrib/rules_multitool.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: development-buildifier.patch

%description
Genuine rules_multitool Starlark rules and repository/toolchain interfaces.
The complete upstream source is preserved. Execution tools are supplied
separately; this package does not contain prebuilt SDK or formatter binaries.

%prep
%setup
%autopatch -p1
sed -i 's/version = "0.0.0"/version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/%module_name
cp -a BUILD.bazel MODULE.bazel WORKSPACE.bazel lockfile.schema.json multitool \
    %buildroot%_datadir/bazel/rules/%module_name/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/%module_name
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 1.11.1-alt1
- Initial build for ALT.

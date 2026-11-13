%define _unpackaged_files_terminate_build 1
%define module_name buildifier_prebuilt

Name: bazel-buildifier-prebuilt
Version: 10.1.0
Release: alt1

Summary: Buildifier and buildozer Starlark rules for Bazel
License: MIT
Group: Development/Other
URL: https://github.com/keith/buildifier-prebuilt
VCS: https://github.com/keith/buildifier-prebuilt.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: upstream-tests.tar
Source2: upstream-examples.tar

BuildRequires: python3

BuildRequires: rpm-build-python3

%description
Original Starlark rules, providers and repository/toolchain interfaces.
The complete genuine upstream source and original tests are preserved.
Native tool executables are supplied separately.

%prep
%setup
tar -xf %SOURCE1 -C .
tar -xf %SOURCE2 -C .
sed -i 's/version = "0"/version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/%module_name
tar --exclude='README*' -cf - BUILD MODULE.bazel WORKSPACE defs.bzl \
    deps.bzl rules.bzl toolchain.bzl buildtools.bzl runner.bash.template \
    runner.bat.template binary_runner.bash.template \
    binary_runner.bat.template buildifier buildozer LICENSE | \
    tar -xf - -C %buildroot%_datadir/bazel/rules/%module_name


%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%dir %_datadir/bazel/rules/%module_name
%_datadir/bazel/rules/%module_name/BUILD
%_datadir/bazel/rules/%module_name/MODULE.bazel
%_datadir/bazel/rules/%module_name/WORKSPACE
%_datadir/bazel/rules/%module_name/defs.bzl
%_datadir/bazel/rules/%module_name/deps.bzl
%_datadir/bazel/rules/%module_name/rules.bzl
%_datadir/bazel/rules/%module_name/toolchain.bzl
%_datadir/bazel/rules/%module_name/buildtools.bzl
%_datadir/bazel/rules/%module_name/runner.bash.template
%_datadir/bazel/rules/%module_name/runner.bat.template
%_datadir/bazel/rules/%module_name/binary_runner.bash.template
%_datadir/bazel/rules/%module_name/binary_runner.bat.template
%_datadir/bazel/rules/%module_name/buildifier
%_datadir/bazel/rules/%module_name/buildozer
%doc %_datadir/bazel/rules/%module_name/LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 10.1.0-alt1
- Initial build for ALT.

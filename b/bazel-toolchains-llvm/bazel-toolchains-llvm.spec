%define _unpackaged_files_terminate_build 1
%define llvm_rules_dir %_datadir/bazel/rules/toolchains_llvm

Name: bazel-toolchains-llvm
Version: 1.13.0
Release: alt1

Summary: LLVM toolchain rules and configuration APIs for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/toolchains_llvm
VCS: https://github.com/bazel-contrib/toolchains_llvm.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: bazel-lib-module.patch

# Darwin-only template; otool is not a Linux runtime dependency.
%add_findreq_skiplist %llvm_rules_dir/toolchain/osx_cc_wrapper.sh.tpl

BuildRequires: rpm-build-python3
BuildRequires(pre): rpm-macros-python3
BuildRequires: python3
BuildRequires: jq

%description
Bazel Starlark rules and configuration templates for LLVM and Clang toolchains.
Includes platform constraints, distribution and version selection metadata,
compiler wrappers and the genuine toolchains_llvm module. LLVM binaries are
provided separately by the system.

%prep
%setup
%autopatch -p1
sed -i '/name = "toolchains_llvm",/a\\    version = "%version",' MODULE.bazel

%build

%install
install -d %buildroot%llvm_rules_dir
cp -a MODULE.bazel WORKSPACE WORKSPACE.bzlmod toolchain platforms \
    %buildroot%llvm_rules_dir/

%check
%__python3 -B -m unittest discover -s utils -p '*_test.py'
%__python3 -B -m unittest discover -s tests -p '*_test.py'

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%llvm_rules_dir
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 1.13.0-alt1
- Initial build for ALT.

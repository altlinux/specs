%define _unpackaged_files_terminate_build 1

Name: bazel-hermetic-llvm
Version: 0.8.26
Release: alt1

Summary: Bazel LLVM compiler, runtime and toolchain source rules
License: Apache-2.0
Group: Development/Other
URL: https://github.com/hermeticbuild/hermetic-llvm
VCS: https://github.com/hermeticbuild/hermetic-llvm.git
BuildArch: noarch

Source0: %name-%version.tar
Source4: upstream-gazelle.tar
Source5: upstream-internal-tools.tar
Source6: upstream-e2e.tar
Source7: upstream-examples.tar
Source8: upstream-tests.tar
Source9: upstream-gcc-tests.tar
Source10: upstream-libstdcxx-tests.tar

BuildRequires: rpm-build-python3

%description
The genuine llvm Bazel module provides compiler and runtime source rules,
platform constraints, build settings and toolchain definitions.
LLVM compilers, SDKs and target runtime binaries are not included.

%prep
%setup -a4 -a5 -a6 -a7 -a8 -a9 -a10
sed -i '0,/version = "0.0.0"/s//version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/llvm
cp -a BUILD.bazel MODULE.bazel *.bzl *.json .buildifier.json \
    3rd_party config constraints extensions gazelle internal_tools kernel \
    platforms prebuilt private runtimes sanitizers toolchain tools \
    %buildroot%_datadir/bazel/rules/llvm/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/llvm
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.8.26-alt1
- Initial build for ALT.

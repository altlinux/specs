%define _unpackaged_files_terminate_build 1

Name: bazel-rules-go
Version: 0.65.0
Release: alt1

Summary: Go rules and toolchain APIs for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/rules_go
VCS: https://github.com/bazel-contrib/rules_go.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: module_dot_bazel_version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: python3

BuildRequires: rpm-build-python3

%description
Bazel Starlark rules for Go libraries, binaries, tests, runfiles and compiler
SDK toolchains. Provides the genuine rules_go module and original tool sources.

%prep
%setup
%autopatch -p1

%build

%install
install -d %buildroot%_datadir/bazel/rules/rules_go
cp -a BUILD.bazel MODULE.bazel WORKSPACE go.mod go.sum AUTHORS CONTRIBUTORS \
    LICENSE.txt extras go internal proto third_party tools \
    %buildroot%_datadir/bazel/rules/rules_go/

# Workspace launchers are not part of the rules_go module.
rm %buildroot%_datadir/bazel/rules/rules_go/go/tools/bazel_benchmark/bazel_benchmark.sh \
    %buildroot%_datadir/bazel/rules/rules_go/tools/gopackagesdriver.sh

# Keep upstream documentation in SOURCE; do not install README files.
find %buildroot%_datadir/bazel -iname 'README*' -delete

%check
export GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local
export GOFLAGS="-mod=readonly"
# Standalone upstream helper tests; Bazel integration needs its full graph.
%gotest ./go/tools/internal/txtar ./go/tools/bzltestutil

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_go
%doc %_datadir/bazel/rules/rules_go/LICENSE.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.65.0-alt1
- Initial build for ALT.

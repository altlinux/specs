%define _unpackaged_files_terminate_build 1

Name: bazel-tar-bzl
Version: 0.10.9
Release: alt1

Summary: Bazel archive rules, mtree and BSD tar toolchain interfaces
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/tar.bzl
VCS: https://github.com/bazel-contrib/tar.bzl.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: mtree-path-encoding.patch

%description
Bazel Starlark archive rules, BSD tar toolchain interfaces and mtree manifest
generation and mutation helpers. Provides the genuine tar.bzl module.
Native archive tools are supplied by the system.

%prep
%setup
%autopatch -p1
sed -i '/name = "tar.bzl",/a\\    version = "%version",' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/tar.bzl
cp -a BUILD MODULE.bazel tar.bzl tar \
    %buildroot%_datadir/bazel/rules/tar.bzl/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/tar.bzl
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.10.9-alt1
- Initial build for ALT.

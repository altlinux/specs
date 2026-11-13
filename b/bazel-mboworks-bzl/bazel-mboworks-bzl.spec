%define _unpackaged_files_terminate_build 1

Name: bazel-mboworks-bzl
Version: 0.8.0
Release: alt1

Summary: Starlark path, version and runfiles utility APIs for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/mboworks/bzl
VCS: https://github.com/mboworks/bzl.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires(pre): rpm-macros-python3
BuildRequires: python3
BuildRequires: git-core

%description
Starlark libraries for portable paths, semantic versions, PEP 440 version
requirements, version selection and Bazel runfiles lookup keys. Provides
the genuine mboworks_bzl module and its complete library APIs.

%prep
%setup

%build

%install
install -d %buildroot%_datadir/bazel/rules/mboworks_bzl
cp -a BUILD.bazel MODULE.bazel bzl \
    %buildroot%_datadir/bazel/rules/mboworks_bzl/

%check
%__python3 -B -m unittest discover -s tools -p '*_test.py'

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/mboworks_bzl
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.8.0-alt1
- Initial build for ALT.

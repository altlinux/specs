%define _unpackaged_files_terminate_build 1

Name: bazel-rules-lint
Version: 2.9.1
Release: alt1

Summary: Bazel formatter composition rules and lint aspects
License: Apache-2.0
Group: Development/Other
URL: https://github.com/aspect-build/rules_lint
VCS: https://github.com/aspect-build/rules_lint.git
BuildArch: noarch

Source0: %name-%version.tar
Source5: upstream-examples.tar
Source6: upstream-rules-rust.tar
Source7: upstream-rust.tar
Patch0: format-gnu-time.patch

BuildRequires: rpm-build-python3

%description
Genuine aspect_rules_lint Starlark formatter composition and language lint
interfaces. The formatter controller uses ordinary system tools. Individual
formatter tools and compiled language helpers are supplied separately.

%prep
%setup -a5 -a6 -a7
%autopatch -p1
sed -i '/name = "aspect_rules_lint",/a\    version = "%version",' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/aspect_rules_lint
cp -a BUILD.bazel MODULE.bazel LICENSE go.mod go.sum format lint tools \
    %buildroot%_datadir/bazel/rules/aspect_rules_lint/

%check
bash -n \
    %buildroot%_datadir/bazel/rules/aspect_rules_lint/format/private/format.sh

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/aspect_rules_lint
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 2.9.1-alt1
- Initial build for ALT.

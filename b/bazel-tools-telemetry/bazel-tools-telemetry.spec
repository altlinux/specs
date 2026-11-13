%define _unpackaged_files_terminate_build 1

Name: bazel-tools-telemetry
Version: 0.5.2
Release: alt1

Summary: Aspect telemetry module for Bazel rules
License: Apache-2.0
Group: Development/Other
URL: https://github.com/aspect-archives/tools_telemetry
VCS: https://github.com/aspect-archives/tools_telemetry.git
BuildArch: noarch

Source0: %name-%version.tar

%description
Aspect's genuine Starlark telemetry extension and collectors. The module
supports the upstream DO_NOT_TRACK opt-out for offline and local builds.

%prep
%setup
sed -i 's/version = "0.0.0"/version = "%version"/' MODULE.bazel

%build

%install
install -d %buildroot%_datadir/bazel/rules/aspect_tools_telemetry
cp -a BUILD.bazel MODULE.bazel *.bzl report.json collectors test \
    %buildroot%_datadir/bazel/rules/aspect_tools_telemetry/

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/aspect_tools_telemetry
%doc LICENSE

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.5.2-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

Name: bazel-platforms
Version: 1.1.0
Release: alt1

Summary: Standard platform constraints for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazelbuild/platforms
VCS: https://github.com/bazelbuild/platforms.git

Source0: %name-%version.tar

BuildArch: noarch

%description
Standard CPU, operating system and distribution constraints for Bazel,
including host platform detection. The source module is installed for
local_path_override consumers. External Bazel modules are supplied separately.

%prep
%setup

%build
# Bazel evaluates the Starlark source module in the consuming build.

%install
install -d %buildroot%_datadir/bazel/rules/platforms
cp -a AUTHORS BUILD LICENSE MODULE.bazel README.md WORKSPACE WORKSPACE.bzlmod \
    version.bzl cpu distro host os tests \
    %buildroot%_datadir/bazel/rules/platforms/
chmod -R u+rwX,go+rX,go-w %buildroot%_datadir/bazel/rules/platforms

# Installed upstream and constraint-selection checks use the separately
# prepared offline Bazel dependency fixture.

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

%files
%doc LICENSE AUTHORS
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/platforms/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

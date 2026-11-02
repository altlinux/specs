%define _unpackaged_files_terminate_build 1

%set_cleanup_method skip

Name: bazel-rules-pkg
Version: 1.3
Release: alt1

Summary: Packaging rules sources for Bazel
License: Apache-2.0
Group: Development/Other
Url: https://github.com/bazelbuild/rules_pkg
VCS: https://github.com/bazelbuild/rules_pkg.git
BuildArch: noarch
# Upstream scripts are source data for Bazel actions.
AutoReqProv: no

Source0: %name-%version.tar
Source1: upstream-files.sha256
Source2: README.ALT
Patch0: %name-%version-alt.patch

BuildRequires: python3

%description
Bazel packaging rules for archives, Debian packages and RPM packages.
The complete upstream source tree is installed in
%_datadir/bazel/rules/rules_pkg for offline local repository integration.
Bazel and transitive module and toolchain dependencies are supplied separately.

%prep
%setup
%autopatch -p1

%build
# Source data only.

%install
install -d %buildroot%_datadir/bazel/rules/rules_pkg
cp -a . %buildroot%_datadir/bazel/rules/rules_pkg/
find %buildroot%_datadir/bazel/rules/rules_pkg -type d -exec chmod 755 {} +
find %buildroot%_datadir/bazel/rules/rules_pkg -type f -exec chmod u+rw,go+r,go-w {} +
cp -p %SOURCE1 %SOURCE2 .

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

%check
python3 -m unittest discover -s tests -p helpers_test.py -v
python3 -m unittest discover -s tests/deb -p control_field_test.py -v
python3 -m unittest discover -s pkg/releasing -p release_tools_test.py -v
python3 -m unittest discover -s tests -p path_test.py -v
cd %buildroot%_datadir/bazel/rules/rules_pkg
# README documentation is intentionally absent from the installed tree.
awk 'tolower($2) !~ /(^|\/)readme[^\/]*$/ { print }' %SOURCE1 \
    | sha256sum -c -
test -s MODULE.bazel
test -s pkg/tar.bzl
test -s pkg/private/tar/build_tar.py
# Upstream Bazel tests require separate transitive modules and toolchains.

%files
%doc LICENSE AUTHORS upstream-files.sha256
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_pkg

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.3-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

Name: bats-support
Version: 0.3.0
Release: alt2

Summary: Supporting library for Bats test helpers
License: CC0
Group: Development/Other
Url: https://github.com/bats-core/bats-support

BuildArch: noarch
Source: %name-%version.tar
Requires: bash bats

%description
bats-support is a supporting library providing common functions to test helper
libraries written for Bats.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/bats-support
cp -pr src %buildroot%_datadir/bats-support
cp -pr load.bash %buildroot%_datadir/bats-support

%files
%doc LICENSE README.md CHANGELOG.md
%_datadir/bats-support

%changelog
* Tue Sep 12 2023 Obidin Oleg <nofex@altlinux.org> 0.3.0-alt2
- Merge with upstream git history

* Wed Mar 29 2023 Obidin Oleg <nofex@altlinux.org> 0.3.0-alt1
- First build for ALT

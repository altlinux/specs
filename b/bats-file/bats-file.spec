%define _unpackaged_files_terminate_build 1

Name: bats-file
Version: 0.3.0
Release: alt1

Summary: Common filesystem assertions for Bats
License: CC0
Group: Development/Other
Url: https://github.com/bats-core/bats-file

BuildArch: noarch
Source: %name-%version.tar
Requires: bats bats-support

%description
bats-file is a helper library providing common filesystem related assertions and helpers for Bats.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/bats-file
cp -pr src %buildroot%_datadir/bats-file
cp -pr load.bash %buildroot%_datadir/bats-file

%files
%doc LICENSE
%_datadir/bats-file

%changelog
* Wed Mar 31 2023 Obidin Oleg <nofex@altlinux.org> 0.3.0-alt1
- First build for ALT

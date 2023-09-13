%define _unpackaged_files_terminate_build 1

Name: bats-assert
Version: 2.1.0
Release: alt2

Summary: Common assertions for Bats
License: CC0
Group: Development/Other
Url: https://github.com/bats-core/bats-assert

BuildArch: noarch
Source: %name-%version.tar
Requires: bats bats-support

%description
bats-assert is a helper library providing common assertions for Bats.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/bats-assert
cp -pr src %buildroot%_datadir/bats-assert
cp -pr load.bash %buildroot%_datadir/bats-assert

%files
%doc LICENSE README.md
%_datadir/bats-assert

%changelog
* Tue Sep 12 2023 Obidin Oleg <nofex@altlinux.org> 2.1.0-alt2
- Merge with upstream git history

* Wed Mar 30 2023 Obidin Oleg <nofex@altlinux.org> 2.1.0-alt1
- First build for ALT

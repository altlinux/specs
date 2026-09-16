%define _unpackaged_files_terminate_build 1

Name: has
Version: 1.6.0
Release: alt1
Summary: checks presence of various command line tools and their versions on the path
License: MIT 
Group: Other
Url: https://github.com/kdabir/has
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: alt-test-disable.patch

BuildRequires: bats

%description
has checks presence of various command line tools on the
PATH and reports their installed version.

%prep
%setup
%autopatch -p1
sed -i 's|/usr/local|%prefix|g' Makefile
sed -i 's|.hastest.bats|%_datadir/bats-core|g' Makefile

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%files
%_bindir/%name
%doc README.md

%changelog
* Wed Sep 16 2026 Pavel Shilov <zerospirit@altlinux.org> 1.6.0-alt1
- updated from 1.5.2 to 1.6.0

* Sun Aug 03 2025 Pavel Shilov <zerospirit@altlinux.org> 1.5.2-alt1
- 1.5.0 -> 1.5.2

* Thu Jul 24 2025 Pavel Shilov <zerospirit@altlinux.org> 1.5.0-alt1.1
- Update based on upstream data.

* Wed Feb 28 2024 Pavel Shilov <zerospirit@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

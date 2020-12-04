Name: libgit-devel
Version: 2.29.2
Release: alt2

Summary: Conflicts with libruby-devel
License: GPLv2
Group: Development/Other
BuildArch: noarch
Conflicts: git-core libruby-devel
Provides: i586-%name = %EVR

%description
This package conflicts with libruby-devel.
The sole purpose of this package is to make it absolutely clear that
there is no rationale whatsoever for libruby-devel to require libgit-devel.

%files

%changelog
* Sat Dec 05 2020 Dmitry V. Levin <ldv@altlinux.org> 2.29.2-alt2
- This package conflicts with libruby-devel.
- The sole purpose of this package is to make it absolutely clear that
  there is no rationale whatsoever for libruby-devel to require libgit-devel.

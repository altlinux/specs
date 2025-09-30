Name: gap-aclib
Version: 1.3.3
Release: alt2
Summary: GAP: Almost Crystallographic Groups
License: Artistic-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/aclib/
Vcs: https://github.com/gap-packages/aclib

# Source-url: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/aclib-%version.tar.bz2
Source: aclib-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-macros-gap
Requires: gap >= 4.7
Requires: gap-polycyclic >= 1.0
#Suggests:       gap-crystcat >= 1.1

%description
The AClib package contains a library of almost crystallographic
groups and a some algorithms to compute with these groups. A group is
called almost crystallographic if it is finitely generated
nilpotent-by-finite and has no non-trivial finite normal subgroups.

%prep
%setup -n aclib
%patch -p1

%build
%install
%gappkg_simple_install

%files -f %name.files
%gap_sitearch/aclib/

%changelog
* Tue Sep 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.3-alt2
- Moved files from aclib-version to aclib.

* Fri Sep 26 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.3-alt1
- New version 1.3.3.
- Added VCS tag.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.2-alt1
- New version (1.3.2) with rpmgs script.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.1-alt1
- Initial build for ALT Sisyphus (thankes opensuse for the spec).

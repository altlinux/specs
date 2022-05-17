Name: gap-aclib
Version: 1.3.2
Release: alt1
Summary: GAP: Almost Crystallographic Groups
License: Artistic-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/aclib/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/aclib-%version.tar.bz2

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
%setup -n aclib-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitearch/aclib-%version/
%gap_sitearch/aclib-%version/*

%changelog
* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.2-alt1
- New version (1.3.2) with rpmgs script.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.1-alt1
- Initial build for ALT Sisyphus (thankes opensuse for the spec).

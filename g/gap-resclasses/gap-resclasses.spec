%define repo resclasses

Name: gap-resclasses
Version: 4.7.3
Release: alt1
Summary: GAP: Set-Theoretic Computations with Residue Classes
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/resclasses/

Source: https://github.com/gap-packages/resclasses/releases/download/v%version/%repo-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.8.7
Requires: gap-gapdoc >= 1.5.1
Requires: gap-polycyclic >= 2.11
Requires: gap-utils >= 0.40
#Suggests:       gap-io >= 4.4.5

%description
ResClasses is a package for set-theoretic computations with residue
classes of the integers and a couple of other rings. The class of
sets which ResClasses can deal with includes the open and the closed
sets in the topo- logy on the respective ring which is induced by
taking the set of all residue classes as a basis, as far as the usual
restrictions imposed by the finite- ness of computing resources
permit this.

%prep
%setup -n resclasses-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Mar 02 2023 Leontiy Volodin <lvol@altlinux.org> 4.7.3-alt1
- New version (4.7.3).

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 4.7.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

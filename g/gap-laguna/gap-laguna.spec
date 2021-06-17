%define repo laguna

Name: gap-laguna
Version: 3.9.0
Release: alt1
Summary: GAP: Lie AlGebras and UNits of group Algebras
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: http://www.cs.st-andrews.ac.uk/~alexk/laguna.htm

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/laguna-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-macros-gap
Requires: gap >= 4.8
Requires: gap-gapdoc >= 1.5.1
#Suggests:       gap-sophus >= 1.2

%description
LAGUNA extends GAP functionality for computations in group rings.
Besides computing some general properties and attributes of group
rings and their elements, LAGUNA is able to perform two main kinds of
computations. Namely, it can verify whether a group algebra of a
finite group satisfies certain Lie properties; and it can calculate
the structure of the normalized unit group of a group algebra of a
finite p-group over the field of p elements.

%prep
%setup -n laguna-%version

%build
%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.9.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

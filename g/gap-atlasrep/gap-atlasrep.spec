%define repo atlasrep

Name: gap-atlasrep
Version: 1.5.1
Release: alt1
Summary: GAP: Interface to the Atlas of Group Representations
License: GPL-3.0+
Group: Sciences/Mathematics
Url: http://nickerson.org.uk/groups

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/atlasrep1r5p1.tar.bz2

BuildArch: noarch
BuildPreReq: fdupes
BuildPreReq: rpm-macros-gap
Requires: gap >= 4.5
Requires: gap-gapdoc >= 1.5
#Suggests:       gap-browse >= 1.4
#Suggests:       gap-ctbllib >= 1.2
#Suggests:       gap-io >= 3.3
#Suggests:       gap-tomlib >= 1.2.1

%description
AtlasRep provides an interface between GAP and the Atlas of Group
Representations, a database that comprises representations of many
almost simple groups and information about their maximal subgroups.

%prep
%setup -n atlasrep

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.5.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

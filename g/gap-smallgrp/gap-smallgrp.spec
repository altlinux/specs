%define repo SmallGrp

Name: gap-smallgrp
Version: 1.3
Release: alt1
Summary: GAP: Small Groups Library
License: Artistic-2.0
Group: Sciences/Mathematics
Url: http://www.math.rwth-aachen.de/~Greg.Gamble/ACE/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/SmallGrp-%version.tar.bz2

BuildArch: noarch
BuildRequires: rpm-macros-gap
Requires: gap >= 4.9
Requires: gap-gapdoc >= 1.5

%description
The SmallGrp package provides the library of groups of certain
"small" orders. The groups are sorted by their orders and they are
listed up to isomorphism; that is, for each of the available orders a
complete and irredundant list of isomorphism type representatives of
groups is given.

%prep
%setup -n SmallGrp-%version

%build
find . -type f -name "*.g" -exec chmod a-x "{}" "+"
perl -i -pe 's{#!%_bindir/env }{#!/bin/}' scripts/* doc/clean

%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

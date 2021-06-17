%define repo grape

Name: gap-grape
Version: 4.8.1
Release: alt1
Summary: GAP: GRaph Algorithms using PErmutation groups
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://www.maths.qmul.ac.uk/~leonard/grape/

#DL-URL:        https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/grape-4.8.1.tar.bz2
# Original tarball has bundled third-party code with a Non-Commercial clause

Source: grape-%version.tar.xz
Source8: sanitize_source.sh

BuildArch: noarch
BuildPreReq: rpm-macros-gap
BuildPreReq: xz
Requires: bliss
Requires: gap >= 4.9
Requires: nauty

%description
GRAPE is a package for computing with graphs and groups, and is
primarily designed for constructing and analysing graphs related to
groups, finite geometries, and designs.

%prep
%setup -n grape-%version

%build
%install
rm -Rf scripts doc/.Rhistory
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 4.8.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

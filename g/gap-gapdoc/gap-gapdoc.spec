%define repo GAPDoc

Name: gap-gapdoc
Version: 1.6.2
Release: alt1
Summary: GAP: package for GAP Documentation
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: http://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/GAPDoc-%version.tar.bz2

BuildArch: noarch
BuildRequires: fdupes
BuildRequires: rpm-macros-gap
Requires: gap >= 4.7.6
#Suggests:       gap-io >= 2.3

%description
This package contains a definition of a structure for GAP (package)
documentation, based on XML. It also contains conversion programs for
producing text, PDF or HTML versions of such documents, with
hyperlinks, if possible.

%prep
%setup -n GAPDoc-%version

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

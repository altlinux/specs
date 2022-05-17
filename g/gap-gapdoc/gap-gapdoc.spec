%define repo GAPDoc

Name: gap-gapdoc
Version: 1.6.5
Release: alt1
Summary: GAP: package for GAP Documentation
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://www.gap-system.org/Packages/gapdoc.html

Source: https://github.com/frankluebeck/GAPDoc/archive/%version/%repo-relv%version.tar.gz

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
%setup -n GAPDoc-relv%version

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo-relv%version/
%gap_sitelib/%repo-relv%version/*

%changelog
* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.6.5-alt1
- 1.6.5.
- Changed url tag.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

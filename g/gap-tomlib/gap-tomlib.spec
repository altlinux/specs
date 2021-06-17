%define repo tomlib

Name: gap-tomlib
Summary: GAP: tables of marks
Version: 1.2.9
Release: alt1
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/tomlib/

Source: https://github.com/gap-packages/tomlib/releases/download/v%version/%repo-%version.tar.gz
BuildArch: noarch

BuildPreReq: fdupes
BuildPreReq: rpm-macros-gap
Requires: gap >= 4.4

%description
The GAP Library of Tables of Marks.

%prep
%setup -n %repo-%version

%build
%install
%gappkg_simple_install
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.2.9-alt1
- Initial build for ALT Sisyphus.

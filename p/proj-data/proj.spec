Name: proj-data
Version: 1.17
Release: alt1

Summary: Data package for libproj
Group: Sciences/Geosciences
License: permissive licenses
Url: https://proj4.org/
Source: %name-%version.tar
BuildArch: noarch
Requires: libproj

%description
This package contains datum grids for libproj

%prep
%setup

%install
mkdir -p %buildroot%_datadir/proj
cp * %buildroot%_datadir/proj/

%files
%_datadir/proj/*

%changelog
* Tue Apr 30 2024 Vladislav Zavjalov <slazav@altlinux.org> 1.17-alt1
- v.1.17

* Mon Dec 18 2023 Vladislav Zavjalov <slazav@altlinux.org> 1.16-alt1
- v.1.16

* Mon Sep 25 2023 Vladislav Zavjalov <slazav@altlinux.org> 1.15-alt1
- v.1.15

* Sat Jul 15 2023 Vladislav Zavjalov <slazav@altlinux.org> 1.14-alt1
- v.1.14

* Wed Oct 19 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.11-alt1
- v.1.11



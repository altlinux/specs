Name: proj-datumgrid
Version: 1.8
Release: alt1

Summary: Datum grids for libproj
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
* Sun Feb 17 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- v 1.8, first build for Altlinux


%define _unpackaged_files_terminate_build 1
%define mname gdex

Name: python3-module-%mname
Version: 4.12
Release: alt2
Summary: GDEX (Good Dictionary Examples) is a Bonito module for sorting concordances according to their suitability as dictionary examples. 
License: GPLv3
Group: Text tools
Url: https://nlp.fi.muni.cz/trac/noske/wiki#gdex
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%py3_provides %mname

%description
GDEX (Good Dictionary Examples) is a Bonito module for sorting concordances
according to their suitability as dictionary examples.

%prep
%setup
%patch -p1
# https://nlp.fi.muni.cz/trac/noske/wiki#gdex1
sed -i "s/<version>/%version/g" setup.py

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buldroot/%_bindir
cp add_gdex %buildroot/%_bindir

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%{pyproject_distinfo %mname}/
%_bindir/add_gdex

%changelog
* Wed Feb 08 2023 Stanislav Levin <slev@altlinux.org> 4.12-alt2
- Fixed FTBFS (setuptools 66).

* Fri Jan 06 2023 Kirill Maslinsky <kirill@altlinux.org> 4.12-alt1
- 4.12

* Sun Mar 15 2020 Kirill Maslinsky <kirill@altlinux.org> 3.12-alt1
- initial build as a separate package


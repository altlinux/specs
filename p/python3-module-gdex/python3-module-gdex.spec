%define mname gdex

Name: python3-module-%mname
Version: 3.12
Release: alt1
Summary: GDEX (Good Dictionary Examples) is a Bonito module for sorting concordances according to their suitability as dictionary examples. 
License: GPLv3
Group: Text tools
Url: http://nlp.fi.muni.cz/trac/noske/wiki/Downloads
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
GDEX (Good Dictionary Examples) is a Bonito module for sorting concordances
according to their suitability as dictionary examples.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info
%_bindir/add_gdex

%changelog
* Sun Mar 15 2020 Kirill Maslinsky <kirill@altlinux.org> 3.12-alt1
- initial build as a separate package


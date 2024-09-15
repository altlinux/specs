Packager: Egor Boyko <nit@altlinux.org>
Name:     verify-checksums
Version:  1.0.11
Release:  alt1
Summary: A utility for verify checksums in files
License: GPL-2.0-only
Group:   System/Configuration/Other
BuildArch: 	noarch
Source:  %name.tar.xz

BuildRequires: python3
BuildRequires: rpm-build-python3 
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-wheel
Requires: gostsum
Provides: verifychecksums
Obsoletes: verifychecksums

%description
Reads files containing hashes of rpm files and checks them.

%prep
%setup -n verify-checksums

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/verify-checksums
%python3_sitelibdir/*
%doc README.md

%changelog
* Mon Sep 09 2024 Egor Boyko <nit@altlinux.org> 1.0.11-alt1
- Add the ability to use a different rpm database for package verification

* Sun Sep 08 2024 Egor Boyko <nit@altlinux.org> 1.0.10-alt1
- Add the ability to pass more than one directory for verification 

* Mon Aug 26 2024 Egor Boyko <nit@altlinux.org> 1.0.9-alt1
- Version 1.0.9

* Fri Aug 16 2024 Egor Boyko <nit@altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Sat Jun 01 2024 Egor Boyko <nit@altlinux.org> 1.0.7-alt1
- Add localization

* Mon May 20 2024 Egor Boyko <nit@altlinux.org> 1.0.6-alt1
- Fix output information in log

* Sun May 19 2024 Egor Boyko <nit@altlinux.org> 1.0.5-alt1
- Fix information in README.md

* Fri May 17 2024 Egor Boyko <nit@altlinux.org> 1.0.4-alt1
- Fix algorithm of verifying packages

* Thu May 16 2024 Egor Boyko <nit@altlinux.org> 1.0.3-alt1
- Add input data validation
- Update README.md

* Thu May 16 2024 Egor Boyko <nit@altlinux.org> 1.0.2-alt1
- Add possibility to select hash algorithm and correct program work output
- Add a program log
- Add output files with a broken hash

* Fri Apr 26 2024 Egor Boyko <nit@altlinux.org> 1.0.1-alt1
- Initial build

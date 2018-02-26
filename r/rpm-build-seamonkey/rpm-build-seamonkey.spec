# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*-

Name:	 	rpm-build-seamonkey
Version:	1.0.6
Release:	alt2
Summary: 	RPM helper macros to rebuild seamonkey packages

Group:		Development/Other
License:	GPL
BuildArch:	noarch
Source0:	rpm.macros.seamonkey
Source1:	rpm.macros.mozilla
Packager:	Damir Shayhutdinov <damir@altlinux.ru>

Conflicts:	seamonkey-devel <= 1:1.0.6-alt1

%description
These helper macros provide possibility to rebuild
seamonkey packages by some Alt Linux Team Policy compatible way.

%install
mkdir -p %buildroot/%_rpmmacrosdir
cp %SOURCE0 %buildroot/%_rpmmacrosdir/seamonkey
cp %SOURCE1 %buildroot/%_rpmmacrosdir/mozilla

%files
%_rpmmacrosdir/seamonkey
%_rpmmacrosdir/mozilla

%changelog
* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.0.6-alt2
- Moved macros to new %%_rpmmacrosdir dir.

* Tue Nov 28 2006 Damir Shayhutdinov <damir@altlinux.ru> 1.0.6-alt1
- Initial build for ALT Linux (based on rpm-build-firefox package))


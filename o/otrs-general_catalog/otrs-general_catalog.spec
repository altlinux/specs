%define installdir %_datadir/otrs

Name: otrs-general_catalog
Version: 1.3.2
Release: alt1

Summary: GeneralCatalog package for OTRS
Group: Networking/WWW
License: AGPLv3
Url: http://www.otrs.org/

Packager: Pavel Zilke <zidex at altlinux dot org>

BuildArch: noarch

Requires: otrs

Source0: GeneralCatalog-1.3.2.opm

%description
GeneralCatalog package for OTRS

%install
install -pD -m0644 %_sourcedir/GeneralCatalog-1.3.2.opm %buildroot%installdir/GeneralCatalog-1.3.2.opm

%files
%defattr(-,root, root)
%installdir

%changelog
* Sun Jan 17 2010 Pavel Zilke <zidex at altlinux dot org> 1.3.2-alt1
- Initial buid for ALT Linux


%define installdir %_datadir/otrs

Name: otrs-import_export
Version: 1.3.2
Release: alt1

Summary: ImportExport package for OTRS
Group: Networking/WWW
License: AGPLv3
Url: http://www.otrs.org/

Packager: Pavel Zilke <zidex at altlinux dot org>

BuildArch: noarch

Requires: otrs

Source0: ImportExport-1.3.2.opm

%description
ImportExport package for OTRS

%install
install -pD -m0644 %_sourcedir/ImportExport-1.3.2.opm %buildroot%installdir/ImportExport-1.3.2.opm

%files
%defattr(-,root, root)
%installdir

%changelog
* Sun Jan 17 2010 Pavel Zilke <zidex at altlinux dot org> 1.3.2-alt1
- Initial build for ALT Linux


%define installdir %_datadir/otrs/itsm

Name: otrs-itsm
Version: 1.3.2
Release: alt1

Summary: ITSM packages for OTRS
Group: Networking/WWW
License: AGPLv3
Url: http://www.otrs.org/

Packager: Pavel Zilke <zidex at altlinux dot org>

BuildArch: noarch

Requires: otrs, otrs-import_export = %version, otrs-general_catalog = %version

Source0: ITSMConfigurationManagement-1.3.2.opm
Source1: ITSMCore-1.3.2.opm
Source2: ITSMIncidentProblemManagement-1.3.2.opm
Source3: ITSMServiceLevelManagement-1.3.2.opm
Source4: otrs_itsm_book_en.pdf

%description
ITSM packages for OTRS

%package doc-en-pdf
Summary: OTRS::ITSM manual (En)
Group: Networking/WWW
%description doc-en-pdf
%name OTRS::ITSM manual (En)

%install
#install packages
install -pD -m0644 %_sourcedir/ITSMConfigurationManagement-1.3.2.opm %buildroot%installdir/ITSMConfigurationManagement-1.3.2.opm
install -pD -m0644 %_sourcedir/ITSMCore-1.3.2.opm %buildroot%installdir/ITSMCore-1.3.2.opm
install -pD -m0644 %_sourcedir/ITSMIncidentProblemManagement-1.3.2.opm %buildroot%installdir/ITSMIncidentProblemManagement-1.3.2.opm
install -pD -m0644 %_sourcedir/ITSMServiceLevelManagement-1.3.2.opm %buildroot%installdir/ITSMServiceLevelManagement-1.3.2.opm
#install docs
install -pD -m0644 %_sourcedir/otrs_itsm_book_en.pdf otrs_itsm_book_en.pdf

%files
%defattr(-,root, root)
%dir %installdir
%installdir/*.opm

%files doc-en-pdf
%doc otrs_itsm_book_en.pdf

%changelog
* Sun Jan 17 2010 Pavel Zilke <zidex at altlinux dot org> 1.3.2-alt1
- Initial build for ALT Linux

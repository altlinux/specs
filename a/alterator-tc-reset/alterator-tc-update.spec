%define _altdata_dir %_datadir/alterator

Name: alterator-tc-reset
Version: 0.0.2
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for reset configuration of thin station to factory defaults
Packager: Packager: Andriy Stepanov <stanv@altlinux.ru>
Source: %name-%version.tar

Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: alterator-l10n >= 2.7-alt10
BuildPreReq: alterator >= 4.10-alt8
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for reset configuration of thin station to factory defaults

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1
- Do not show this html module in alterator-browser-qt (ALT #32622)

* Tue Jul 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.0.1-alt2
- Rebuild by cas@

* Wed Feb 29 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build

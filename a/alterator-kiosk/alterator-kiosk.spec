Name: alterator-kiosk
Version: 1.2
Release: alt1

Source: %name-%version.tar

Summary: alterator module for managing kiosk mode
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: alterator
Requires: kiosk

%description
alterator module for managing kiosk mode

%prep
%setup -q

%install
%makeinstall

%files
%_sysconfdir/alterator/kiosk/
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*

%changelog
* Fri Jun 19 2020 Oleg Solovyov <mcpain@altlinux.org> 1.2-alt1
- remove system restrictions

* Wed Mar 25 2020 Oleg Solovyov <mcpain@altlinux.org> 1.1-alt1
- remove altha from error message

* Mon Jan 27 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- init



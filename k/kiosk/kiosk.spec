Name: kiosk
Version: 0.1
Release: alt1

Source: %name-%version.tar

Summary: Utility for managing kiosk mode
License: GPLv2+
Group: System/Configuration/Other

BuildRequires: libnl-devel

%description
Utility for managing kiosk mode

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/kiosk

%changelog
* Wed Feb 05 2020 Oleg Solovyov <mcpain@altlinux.org> 0.1-alt1
- initial build for ALT


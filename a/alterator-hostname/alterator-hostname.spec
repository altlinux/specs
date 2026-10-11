Name: alterator-hostname
Version: 1.1
Release: alt1

Summary: alterator module for set hostname
License: GPL-3.0-or-later
Group: System/Configuration/Other

Source:%name-%version.tar

BuildArch: noarch
Requires: alterator
Requires: alterator-sh-functions
Requires: alterator-l10n >= 2.7-alt3

BuildPreReq: alterator >= 4.6-alt3

%description
alterator module for set hostname.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/steps/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Sun Oct 11 2026 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- backend3/hostname: fix write hostname (Closes: 60872).

* Tue Jan 14 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt2
- Do not run hostnamectl or hostname

* Sun Dec 15 2024 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build

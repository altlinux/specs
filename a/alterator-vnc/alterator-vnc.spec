Name: alterator-vnc
Version: 1.0
Release: alt3

Source:%name-%version.tar

Packager: Nikita Ermakov <arei@altlinux.org>

Summary: alterator module to edit VNC server password.
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator >= 4.6-alt3 alterator-sh-functions >= 0.13-alt2
Requires: shadow-utils passwdqc-utils
Requires: alterator-l10n >= 2.7-alt3
Conflicts: alterator-lookout < 2.2-alt1
Conflicts: alterator-fbi < 5.25-alt4
Conflicts: alterator-users < 8.1

BuildPreReq: alterator >= 4.6-alt3

%description
%summary

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*
%attr(700,root,root) %dir %_libexecdir/alterator/hooks/vnc.d

%changelog
* Mon Sep 23 2024 Lenar Shakirov <snejok@altlinux.org> 1.0-alt3
- fix ajax.scm: Generate checkbox didn't work
- index.html cleaned: ssh-key buttons left over from a-root
- desktop file moved from X-Alterator-Users to System
- fix little typo

* Mon Aug 26 2019 Nikita Ermakov <arei@altlinux.org> 1.0-alt2
- Fix quotation in the backend3.

* Fri Aug 23 2019 Nikita Ermakov <arei@altlinux.org> 1.0-alt1
- Initial release for ALT Sisyphus.

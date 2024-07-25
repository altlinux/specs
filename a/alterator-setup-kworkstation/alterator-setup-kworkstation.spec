Name: alterator-setup-kworkstation
Version: 0.0.6
Release: alt1

Summary: Perform initial setup of an OEM installation
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: alterator

Requires: alterator-setup
Requires: alterator-setup-welcome
Requires: alterator-l10n
Requires: alterator-notes
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-root
Requires: alterator-users
Requires: alterator-net-eth
Requires: alterator-net-wifi
Requires: NetworkManager-daemon


%description
%summary

%prep
%setup

%install
%makeinstall
install -pD -m755 custom.steps %buildroot%_sysconfdir/%name/custom.steps
cp -a steps %buildroot%_sysconfdir/%name/
install -pD -m755 93-remove-package.sh %buildroot%_libexecdir/alterator/hooks/setup-postinstall.d/93-remove-package.sh

%files
%_sysconfdir/%name/custom.steps
%_sysconfdir/%name/steps/*
%_libexecdir/alterator/hooks/setup-postinstall.d/93-remove-package.sh
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*

%post
cat %_sysconfdir/%name/custom.steps > %_sysconfdir/alterator-setup/steps
cp -r -u %_sysconfdir/%name/steps %_datadir/alterator/

%postun
> /root/.bash_history

%changelog
* Thu Jul 25 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.0.6-alt1
- center the user selection area
- set the correct module icon

* Tue Dec 21 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.5-alt1
- change the order of steps
- fix Icon in setup-welcome.desktop file
- fix new line in setup-kworkstation.desktop

* Tue Nov 30 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.4-alt1
- move translation to alterator-l10n module
- add help
- add setup-welcome step

* Wed Dec 23 2020 Ivan Razzhivin <underwit@altlinux.org> 0.0.3-alt1
- change the procedure for deleting users

* Wed Dec 23 2020 Ivan Razzhivin <underwit@altlinux.org> 0.0.2-alt1
- fix hook script
- small fix spec file
- cleanup the history after uninstall package
- add translation
- fix text
- remove users
- remove 70-copy-connections.sh

* Fri Nov 06 2020 Ivan Razzhivin <underwit@altlinux.org> 0.0.1-alt1
- init

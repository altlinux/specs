Name: alterator-multiseat
Version: 0.0.8
Release: alt1

Source: %name-%version.tar

Summary: alterator module for setup multiseat configuration
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator

BuildArch: noarch

%description
alterator module for setup multiseat configuration

%prep
%setup -q

%build


%install
%makeinstall 


%files
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*

%changelog
* Thu Nov 25 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.8-alt1
- fix saving configuration

* Tue Nov 09 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.7-alt1
- integration with setup-multiseat-pulse
- add sound cards to device list
- attach frame buffer
- improve device management

* Wed Sep 29 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.6-alt1
- change pop-up message (closes: #40205)
- update translation

* Mon May 31 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.5-alt1
- refactoring get_device_name function (closes: #40097)
- add the ability to save and restore the config
- remove device_flush call from cache_seat_rm_all and cache_seat_remove (closes: #40098)
- mark a seat when it is active

* Fri May 14 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.4-alt1
- fix list-seats (closes: #39917, #39964)
- reboot when activate
- show drm/card0
- small fixes
- change message for pop-up dialog

* Fri Apr 16 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.3-alt1
- disable saving configuration
- hide /drm/card0
- fix popup message (closes: #39916)
- fix help

* Tue Apr 13 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.2-alt1
- disable test activation (closes: #39911)
- add multiple selection in the device list (closes: #39915)
- show a message box when activated (closes: #39916)
- flush-devices when remove seat (closes: #39913)
- rename buttons (closes: #39918, #39912)
- update help (closes: #39910, #39914)

* Wed Mar 10 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.1-alt1
- init

Name: setup-multiseat-pulse
Version: 0.1.5
Release: alt1

Summary: Setup pulseaudio to use proper HDMI audio output
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://altlinux.org/multiseat
Source: 90-multiseat-pulse.sh
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%define script %_sysconfdir/X11/xinit.d/90-multiseat-pulse.sh

%description
%summary
by figuring out the HDMI part of the videocard
this particular X session is running on (if any);
quite useful for multiseat.

This implementation has been tested on Elbrus 801-PC
triple-seat system with Radeon R7 240 cards
but should be useful more generally.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%script

%files
%config(noreplace) %script

%changelog
* Thu Oct 14 2021 Ivan Razzhivin <underwit@altlinux.org> 0.1.5-alt1
- integration with alterator-multiseat

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 0.1.4-alt1
- exponential backoff to cope with PA races

* Fri Dec 20 2019 Michael Shigorin <mike@altlinux.org> 0.1.3-alt1
- *wait* for pulseaudio to actually start

* Fri Dec 20 2019 Michael Shigorin <mike@altlinux.org> 0.1.2-alt1
- wait for pulseaudio to *actually* start

* Fri Dec 20 2019 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- wait for pulseaudio to actually start

* Tue Dec 17 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release


Name: asterisk1.8-full
Summary: Asterisk 1.8 -- full package
BuildArch: noarch
Version: 4.0.1
Release: alt2
License: GPL
Group: System/Servers

Conflicts: asterisk-full < %version-%release

Requires: appliance-asterisk-office

Requires: asterisk1.8-complete
Requires: asterisk1.8-devel-doc
Requires: asterisk1.8-sources
Requires: asterisk1.8-chan_dongle
Requires: asterisk1.8-chan_ss7
Requires: asterisk1.8-app_konference

# appliance-hw-dahdi
#Requires: appliance-hw-dahdi

%description
%summary

%files

%changelog
* Sun Nov 11 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add requires to app_konference, chan_dongle, chan_ss7, devel-doc

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


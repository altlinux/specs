Name: asterisk1.8-full
Summary: Asterisk 1.8 -- full package
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Servers

Conflicts: asterisk-full < %version-%release

Requires: appliance-asterisk-office

#Requires: asterisk1.6-devel-doc
Requires: asterisk1.8-sources

# builded from asterisk SRPM
# All this packages requires one asterisk version
Requires: asterisk1.8-complete

#Requires: asterisk1.8-chan_ss7
#Requires: asterisk1.8-app_konference
#Requires: asterisk1.8-addons
#Requires: asterisk1.8-chan_datacard

# appliance-hw-dahdi
#Requires: appliance-hw-dahdi

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


Name: asterisk11-full
Summary: Asterisk 11 -- full package
BuildArch: noarch
Version: 1.0
Release: alt1
License: GPL
Group: System/Servers

Conflicts: asterisk-full < %version-%release

Requires: appliance-asterisk-office

#Requires: asterisk1.6-devel-doc
Requires: asterisk11-sources

# builded from asterisk SRPM
# All this packages requires one asterisk version
Requires: asterisk11-complete

#Requires: asterisk11-chan_ss7
#Requires: asterisk11-app_konference
#Requires: asterisk11-addons
#Requires: asterisk11-chan_datacard

# appliance-hw-dahdi
#Requires: appliance-hw-dahdi

%description
%summary

%files

%changelog
* Wed Nov 07 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build for Sisyphus

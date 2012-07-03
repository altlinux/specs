Name: ve-asterisk1.8
Summary: virtual package for Asterisk PBX appliance
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: appliance-ve-minimal
Requires: appliance-base-sshd

#debug packages
Requires: elinks
Requires: strace

# DAHDI
Requires: appliance-pbx-hardware

# Asterisk server
Requires: asterisk1.8-full
Requires: asterisk-core-sounds-en-alaw
Requires: asterisk-core-sounds-ru-alaw
Requires: pbx-music

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


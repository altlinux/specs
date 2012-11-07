Name: ve-asterisk11
Summary: virtual package for Asterisk PBX appliance
BuildArch: noarch
Version: 1.0
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
Requires: asterisk11-full
Requires: asterisk-core-sounds-en-alaw
Requires: asterisk-core-sounds-ru-alaw
Requires: pbx-music

%description
%summary

%files

%changelog
* Wed Nov 07 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build for Sisyphus

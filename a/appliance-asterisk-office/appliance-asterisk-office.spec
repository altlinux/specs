Name: appliance-asterisk-office
Summary: Asterisk in office packages
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: asterisk-core-sounds-en-alaw
Requires: asterisk-core-sounds-ru-alaw

# Versions before this has critical security bug
Requires: astmanproxy >= 20061015:1.22-alt1.pre.20061015

# Versions before this not compatible with Asterisk 1.4
Requires: asterisk-op_panel >= 0.27-alt1

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


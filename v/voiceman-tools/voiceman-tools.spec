Name: voiceman-tools
Version: 20101220
Release: alt1
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildArch: noarch

Summary: The set of scripts to manipulate voiceman outputs
Group: System/Configuration/Other
License: GPL

Requires: tts-base voiceman-server

Source: %name.tar.gz

%description
This package contains the set of scripts to manipulate voiceman outputs.
List of available commands:
- voiceman-available - list all available voiceman outputs;
- voiceman-enabled <name> - check if <name> output is enabled (by exit code)
- voiceman-enable <name> - enable <name> output for voiceman;
- voiceman-disable <name> - disable <name> output for voiceman;
- voiceman-list - list all currently enabled outputs;
- voiceman-clear - disable all enabled outputs'.

%prep
%setup -q -n %name
%build

%install
%__install -pD -m755 voiceman-available %buildroot%_bindir/voiceman-available
%__install -pD -m755 voiceman-enable %buildroot%_bindir/voiceman-enable
%__install -pD -m755 voiceman-enabled %buildroot%_bindir/voiceman-enabled
%__install -pD -m755 voiceman-disable %buildroot%_bindir/voiceman-disable
%__install -pD -m755 voiceman-list %buildroot%_bindir/voiceman-list
%__install -pD -m755 voiceman-clear %buildroot%_bindir/voiceman-clear

%files
%_bindir/*

%changelog
* Mon Dec 20 2010 Michael Pozhidaev <msp@altlinux.ru> 20101220-alt1
- Various minor fixes
- Added voiceman-enabled output

* Sat Sep 06 2008 Michael Pozhidaev <msp@altlinux.ru> 20080906-alt1
- Initial RPM


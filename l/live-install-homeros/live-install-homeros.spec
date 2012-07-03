Name: live-install-homeros
Version: 20120113
Release: alt1
Summary: The set of scripts for live-install package to clone ALT Linux Homeros from LiveCD to a hard disk
Group: System/Configuration/Other
License: GPL
BuildArch: noarch
Packager: Michael Pozhidaev <msp@altlinux.ru>

Requires: live-install

Source: %name-%version.tar.gz

%description
The set of scripts for live-install package to clone ALT Linux Homeros from LiveCD to a hard disk

%prep
%setup -q
%build
%install
%__install -pD -m 755 homeros-install %buildroot%_sbindir/homeros-install
%__install -d -m 755 %buildroot/%_datadir/live-install/scripts.d
%__install -pD -m 755 ./scripts/* %buildroot/%_datadir/live-install/scripts.d

%files
%_sbindir/*
%_datadir/live-install/scripts.d/*

%changelog
* Fri Jan 13 2012 Michael Pozhidaev <msp@altlinux.ru> 20120113-alt1
- Fixed --no-lilo command line processing

* Sun Jan 08 2012 Michael Pozhidaev <msp@altlinux.ru> 20120108-alt1
- Initial package


Name: xorg-96dpi
Version: 0.1
Release: alt1
Summary: Fix X11 resolution when using non-standard displays
License: GPL
Group: System/X11

BuildArch: noarch

%description
%summary

%install
mkdir -p %buildroot%_datadir/X11/xorg.conf.d
cat << __EOF__ > %buildroot%_datadir/X11/xorg.conf.d/00-96dpi.conf
Section "ServerFlags"
	Option "DontForce96DPI" "false"
EndSection
__EOF__

%files
%_datadir/X11/xorg.conf.d/00-96dpi.conf

%changelog
* Tue Oct 31 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release


Name: xorg-conf-noblank
Version: 0.1
Release: alt1

Summary: Prevent X server from blanking
License: public domain
Group: System/X11

Url: http://altlinux.org/DPMS
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%define conffile 50-noblank.conf
%define confdir %_sysconfdir/X11/xorg.conf.d

%description
%summary through DPMS or internal screensaver,
static equivalent of `xset s off -dpms'.

%prep

%build
cat >> %conffile << EOF
Section "Monitor"
	Identifier "Monitor0"
	Option "DPMS" "false"
EndSection

Section "ServerLayout"
	Identifier "ServerLayout0"
	Option "StandbyTime" "0"
	Option "SuspendTime" "0"
	Option "OffTime"     "0"
	Option "BlankTime"   "0"
EndSection
EOF

%install
install -pDm644 %conffile %buildroot%confdir/%conffile

%files
%config(noreplace) %confdir/%conffile

%changelog
* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release


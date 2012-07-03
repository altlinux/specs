Name: xorg-conf-right-click-ungrab
Version: 0.1
Release: alt1
Summary: X11 configuration file for enable expiremental RightClickUngrab ServerFlag
License: MIT/X11
Group: System/Configuration/Hardware
BuildArch: noarch

Source: %name-%version.tar


%description
X11 configuration file for enable expiremental RightClickUngrab ServerFlag

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/X11/xorg.conf.d/
install -m0644 *.conf %buildroot%_sysconfdir/X11/xorg.conf.d/

%files
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/*.conf

%changelog
* Wed Mar 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial release based on xorg-conf-pegatron-lucid

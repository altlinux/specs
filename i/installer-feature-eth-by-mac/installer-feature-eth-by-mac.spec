Name: installer-feature-eth-by-mac
Version: 0.3
Release: alt1

Summary: Ethernet interface binding by MAC address
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Ethernet interface binding by MAC address
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Requires: alterator-hw-functions

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%changelog
* Tue Apr 28 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- fixed return code when there are virtual interfaces 

* Fri Apr 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- rewritten using altarator-hw-functions to avoid binding virtual interfaces 

* Thu May 08 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
- script based on installer-ltsp 0.1.1


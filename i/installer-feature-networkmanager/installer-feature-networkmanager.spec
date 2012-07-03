Name: installer-feature-networkmanager
Version: 0.1
Release: alt1

Summary: Disable remote access
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Run NetworkManager at startup
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%changelog
* Tue Jul 22 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial version based in installer-*disable-remote 



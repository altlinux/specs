Name: installer-feature-cmdline-parameters
Version: 0.2
Release: alt1

Summary: Copy cmdline parameters to grub2 config
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
BuildArch: noarch

%description
%summary

%package stage2
Summary: Copy cmdline parameters to grub2 config
License: GPL
Group: System/Configuration/Other

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%changelog
* Mon Oct 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- drop dependence on installer-stage2 for use in livecd-install

* Mon Oct 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial

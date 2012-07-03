Name: installer-feature-autohostname
Version: 0.5
Release: alt1

Summary: generate default unique hostname 
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: generate default unique hostname 
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
* Thu Jun 16 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- Drop installer-stage2 require.
- Don't use HAL.

* Thu Mar 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- added prefix, idea from kipruss@ 

* Tue Mar 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- fixed work in qemu 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- don't generate hostname if it isn't default 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- board name changet to processor name 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build 


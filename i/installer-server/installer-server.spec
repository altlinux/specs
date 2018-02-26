Name: installer-server
Version: 0.2
Release: alt2

Summary: Installer common files
License: GPL
Group: System/Configuration/Other

Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>

Source: %name-%version.tar

BuildRequires: alterator rpm-devel

%description
Installer common files

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-notes
Requires: alterator-tzone openntpd
Requires: alterator-datetime
Requires: alterator-vm
Requires: x-cursor-theme-jimmac

%description stage2
Installer stage2

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage3
#modules
Requires: alterator-lilo
Requires: alterator-users
Requires: alterator-pkg
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general

%description stage3
Installer stage3

%prep
%setup -q

%install
%makeinstall

%find_lang alterator-server

%files -f alterator-server.lang
%_datadir/install2/help/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/postinstall.d/*
%_datadir/install2/initinstall.d/*
%_datadir/install2/steps/*

%files stage3
%_datadir/alterator/ui/server

%changelog
* Thu Apr 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- drop removing alterator-lilo 

* Thu Mar 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1.M40.3
- added setup of vm-profile 

* Thu Mar 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1.M40.2
- alterator-license changed to alterator-notes 

* Fri Feb 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1.M40.1
- backport to 4.0

* Wed Feb 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- fixed list of installer specific packages
- added hook to reenable copying packages from CDROM

* Wed Oct 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- use modern "Additional packages" step

* Wed Oct 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- resurrect "Additional packages" steps

* Tue Oct 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

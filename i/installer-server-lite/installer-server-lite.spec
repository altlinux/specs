Name: installer-server-lite
Version: 0.2
Release: alt1

Summary: Installer common files
License: GPL
Group: System/Configuration/Other

Packager: Eugene Prokopiev <enp@altlinux.ru>

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
Requires: alterator-license
Requires: alterator-tzone openntpd
Requires: alterator-datetime
Requires: alterator-vm
Requires: alterator-notes
Requires: alt-notes-server-lite
Requires: installer-feature-vm-simple-stage2
Requires: installer-feature-powerbutton-stage2
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
%_datadir/install2/steps/*

%files stage3
%_datadir/alterator/ui/server

%changelog
* Mon Aug 11 2008 Eugene Prokopiev <enp@altlinux.ru> 0.2-alt1
- fork installer-server

Name: installer-feature-online-repo
Version: 0.12
Release: alt1

Summary: Make online repositories available
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %name-%version.tar

%description
Make online repositories available

Requires: chrooted

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Sat Jun 02 2012 Sergey V Turchin <zerg@altlinux.org> 0.12-alt1
- turn off cdrom repository and mountpoint when turn on online repo

* Thu May 10 2012 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1
- Change arepo repository name

* Fri Nov 25 2011 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- Fix process empty item on i586 architecture

* Tue Aug 23 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt1
- Fix fail on i586 (thanks cas@)

* Mon May 23 2011 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Support x86_32 repository

* Fri Oct 22 2010 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- use curl instead chrooted ping for network availability
- use http:// instead of ftp:// sources because somebody have passive mode

* Tue Feb 09 2010 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- fix hook directory 
- fix network detection

* Wed Feb 03 2010 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- initial version


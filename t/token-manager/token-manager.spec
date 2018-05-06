%ifarch x86_64
%define cpro_arch amd64
%else
%define cpro_arch ia32
%endif

%define rev 51687e2

Name:    token-manager
Version: 0.12
Release: alt4.git%rev
Summary: Certificate manager for CryptoPro CSP

License: MIT
URL: https://github.com/bmakarenko/token-manager
Packager: Andrey Cherepanov <cas@altlinux.org>
Group:   Security/Networking
Source:  %name.tar
Source1: cpconfig-pam.alt

BuildPreReq: libpam-devel
BuildRequires: python-module-PyQt4
Requires: consolehelper
Requires: opensc

BuildArch: noarch

%description
A PyQt front-end for Crypto Pro CSP for CentOS 6 and GosLinux by The
Federal Bailiffs' Service of Russia.

%prep
%setup -q

%install
mkdir -p %buildroot/%_bindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/cpconfig-%cpro_arch
install -Dm 0644 %name.py %buildroot%_bindir/%name.py
install -Dm 0644 %name.png %buildroot%_pixmapsdir/%name.png
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %SOURCE1 %buildroot%_sysconfdir/pam.d/cpconfig-%cpro_arch
install -Dm 0644 cpconfig-%cpro_arch %buildroot%_sysconfdir/security/console.apps/cpconfig-%cpro_arch

%files
%_bindir/*
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%config(noreplace) %_sysconfdir/pam.d/cpconfig-%cpro_arch
%config(noreplace) %_sysconfdir/security/console.apps/cpconfig-%cpro_arch

%changelog
* Sun May 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.12-alt4.git51687e2
- New version.

* Sun Sep 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.12-alt3.git1143028
- Add project URL

* Mon May 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.12-alt2.git1143028
- Build from upstream tag
- Upstream fixes:
  + fix parse compound certificate fields
  + fix for card without s/n
  + fix run with missing backend

* Fri Apr 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.12-alt1
- New version with CryptoPro 4.0 support (ALT #33375)

* Tue Dec 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.11-alt2.git540ad57
- Fixed certmgr output parsing
- Small fix of getting tokens names

* Thu Nov 10 2016 Andrey Cherepanov <cas@altlinux.org> 0.11-alt1
- Initial build in Sisyphus
- Use ALT-specific pam rules

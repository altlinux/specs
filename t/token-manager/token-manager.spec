%ifarch x86_64
%define cpro_arch amd64
%else
%define cpro_arch ia32
%endif

%define rev 51687e2

Name:       token-manager
Version:    0.12
Release:    alt7

Summary:    Certificate manager for CryptoPro CSP
License:    MIT
Group:      Security/Networking
URL:        https://github.com/bmakarenko/token-manager

Packager:   Andrey Cherepanov <cas@altlinux.org>
BuildArch:  noarch

Source:     %name.tar
Source1:    cpconfig-pam.alt
Source2:    token-manager

Patch0:    port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libpam-devel python3-module-PyQt5
BuildRequires: python-tools-2to3

Requires: consolehelper opensc


%description
A PyQt front-end for Crypto Pro CSP for CentOS 6 and GosLinux by The
Federal Bailiffs' Service of Russia.

%prep
%setup -q
%patch0 -p1

2to3 -w -n $(find ./ -name '*.py')

sed -i 's|python|python3|' $(find ./ \( -name '%{name}.py' \
                                     -o -name '%{name}.desktop' \) )
sed -i 's|PyQt4|PyQt5|' token-manager.py
sed -i 's|QtGui|QtWidgets|' token-manager.py

%install
mkdir -p %buildroot/%_bindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/cpconfig-%cpro_arch
install -Dm 0644 %name.py %buildroot%_bindir/%name.py
install -Dm 0644 %name.png %buildroot%_pixmapsdir/%name.png
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %SOURCE1 %buildroot%_sysconfdir/pam.d/cpconfig-%cpro_arch
install -Dm 0755 %SOURCE2 %buildroot%_bindir/%name
install -Dm 0644 cpconfig-%cpro_arch %buildroot%_sysconfdir/security/console.apps/cpconfig-%cpro_arch

%files
%_bindir/*
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%config(noreplace) %_sysconfdir/pam.d/cpconfig-%cpro_arch
%config(noreplace) %_sysconfdir/security/console.apps/cpconfig-%cpro_arch


%changelog
* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 0.12-alt7
- Ugly port to PyQt5

* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.12-alt6.git51687e2
- Porting on python3.

* Tue Oct 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.12-alt5.git51687e2
- Add token-manager executable (ALT #33815).

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

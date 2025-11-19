%define _unpackaged_files_terminate_build 1
%ifarch x86_64
%define cpro_arch amd64
%define miss_arch ia32
%else
%define cpro_arch ia32
%define miss_arch amd64
%endif

Name:    token-manager
Version: 5.3
Release: alt1

Summary: Certificate manager for CryptoPro CSP
License: MIT
Group:   Security/Networking
URL:     https://github.com/wolandius/token-manager

ExclusiveArch: x86_64 %ix86

Source: %name-%version.tar
Source1: cpconfig-pam.alt
Patch0: token-manager-alt-links.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libpam-devel

Requires: polkit opensc

%description
A GTK front-end for Crypto Pro CSP.

The application requires following packages to be installed before you use
it (for x86_64 architecture):

* opensc
* cprocsp-rdr-pcsc-64
* lsb-cprocsp-capilite-64
* opensc, cprocsp-rdr-gui
* cprocsp-rdr-gui-gtk

Parent project by Boris Makarenko https://github.com/bmakarenko/token-manager

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install
%ifarch x86_64
mv %buildroot/usr/{lib,%_lib}
%endif
install -Dm 0644 %SOURCE1 %buildroot%_sysconfdir/pam.d/cpconfig-%cpro_arch
%ifarch %ix86
rm %buildroot%_desktopdir/token-manager.desktop
%else
rm %buildroot%_desktopdir/token-manager-%miss_arch.desktop
%endif
rm %buildroot%_sysconfdir/pam.d/cpconfig-%miss_arch \
   %buildroot%_sysconfdir/security/console.apps/cpconfig-%miss_arch
%find_lang token_manager

%files -f token_manager.lang
%_bindir/%name
%_desktopdir/*.desktop
%config(noreplace) %_sysconfdir/pam.d/cpconfig-%cpro_arch
%config(noreplace) %_sysconfdir/security/console.apps/cpconfig-%cpro_arch
%python3_sitelibdir/token_manager*
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/token_manager
%_datadir/polkit-1/actions/*.policy

%changelog
* Wed Nov 19 2025 Andrey Cherepanov <cas@altlinux.org> 5.3-alt1
- New version (fixes: OVE-20251119-0002 Support extra fields for cetificate check dates).

* Fri Jun 27 2025 Andrey Cherepanov <cas@altlinux.org> 5.2.3-alt1
- New version.
- Change upstream to https://github.com/wolandius/token-manager.

* Fri Jun 20 2025 Anton Midyukov <antohami@altlinux.org> 0.12-alt12
- NMU: Revert "Switch to use pkexec instead consolehelper"

* Mon May 05 2025 Anton Midyukov <antohami@altlinux.org> 0.12-alt11
- NMU: Switch to use pkexec instead consolehelper

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 0.12-alt10
- Returned messagebox for errors (ALT #43588).

* Tue Aug 16 2022 Andrey Cherepanov <cas@altlinux.org> 0.12-alt9
- Fix delete certificate from local storage.

* Fri Aug 05 2022 Andrey Cherepanov <cas@altlinux.org> 0.12-alt8
- Complete port to PyQt5 (ALT #38202).

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

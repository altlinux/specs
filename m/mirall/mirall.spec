Name: mirall
Version: 1.0.2
Release: alt6

Group: Networking/Other
Summary: Applet for ownflowd files syncronization
License: GPL

Source: %name-%version.tar
Patch1: mirall-1.0.2-alt-notwarn-notconfigured.patch
Patch2: mirall-1.0.2-alt-dont-check-updates.patch
Patch3: %name-g++8.patch

BuildRequires: rpm-macros-cmake cmake libqt4-devel gcc-c++ libcsync-devel

%description
Applet for file syncronization via owncloud.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake
%make -C BUILD

%install
%makeinstall_std -C BUILD
mkdir -p %buildroot/%_sysconfdir/xdg/autostart
install -m0644 mirall.desktop %buildroot/%_sysconfdir/xdg/autostart

%find_lang %name

%files -f %name.lang
%_bindir/mirall
%_sysconfdir/exclude.lst
%_sysconfdir/xdg/autostart/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/mirall.*

%changelog
* Tue Feb 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt6
- no return statement in the non-void function fixed (according g++8)

* Tue Aug 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt5
- Complete Russian translation

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt4
- exclude owncloud-client files

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2.M60P.1
- built for M60P

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3
- don't check for updates by default

* Tue Jul 10 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1.M60P.1
- built for M60P

* Tue Jul 10 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- don't show warning if not configured

* Thu May 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Apr 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt3
- Add Russian translation (ALT #27273)
- Fix typo in desktop file

* Fri Apr 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.1-alt2
- desktop file added

* Wed Apr 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.1-alt1
- initial build


Name: mirall
Version: 1.0.2
Release: alt1

Group: Networking/Other
Summary: Applet for ownflowd files syncronization
License: GPL

Source: %name-%version.tar

BuildRequires: rpm-macros-cmake cmake libqt4-devel gcc-c++ libcsync-devel

%description
Applet for file syncronization via owncloud.

%prep
%setup

%build
%cmake
%make -C BUILD

%install
%makeinstall_std -C BUILD
mkdir -p %buildroot/%_sysconfdir/xdg/autostart
install -m0644 mirall.desktop %buildroot/%_sysconfdir/xdg/autostart

%find_lang %name

%files -f %name.lang
%_bindir/*
%_sysconfdir/exclude.lst
%_sysconfdir/xdg/autostart/*
%_datadir/%name
%_iconsdir/hicolor/48x48/apps/*

%changelog
* Thu May 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Apr 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt3
- Add Russian translation (ALT #27273)
- Fix typo in desktop file

* Fri Apr 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.1-alt2
- desktop file added

* Wed Apr 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.1-alt1
- initial build


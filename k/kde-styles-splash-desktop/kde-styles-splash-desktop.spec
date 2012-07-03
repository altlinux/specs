Name: kde-styles-splash-desktop 
Version: 4.1
Release: alt1
BuildArch: noarch

Summary: KDE Splash for ALT Linux 4.1 Desktop

License: GPL
Group: Graphical desktop/KDE

Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Source: %name-%version.tar

BuildRequires: fontconfig freetype2 kde-settings kdelibs 
Requires: ksplash-engine-moodin

%description
KDE Splash for ALT Linux 4.1 Desktop

%prep
%setup -q 

%install
mkdir -p %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxDesktop
install -m 644 *.jpg %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxDesktop/
install -m 644 *.png %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxDesktop/
install -m 644 *.rc %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxDesktop/

%files
%_datadir/apps/ksplash/Themes/ALTLinuxDesktop/*

%changelog
* Fri Sep 12 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1-alt1
- new theme for ALT Linux 4.1 Desktop (Moodin engine) by cas@

* Thu Oct 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt2
- text on top fixed 

* Thu Oct 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- initial build 


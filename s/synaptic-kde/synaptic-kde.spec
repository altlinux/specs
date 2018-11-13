Name: synaptic-kde
Version: 1.0
Release: alt3

Summary: Usermode KDE bindings for synaptic
Group: System/Configuration/Packaging
License: GPL
BuildArch: noarch

Source: %name-%version.tar

Requires: synaptic yelp

%description
Synaptic is a graphical front-end for APT (Advanced Package Tool).
It attempts to be a lot easier to use than other existing APT front-ends.

This package contains usermode KDE bindings for synaptic.

%prep
%setup

%install
mkdir -p %buildroot/%_desktopdir
install -pD -m644 synaptic-kde.desktop %buildroot/%_desktopdir/

%files
%_desktopdir/synaptic-kde.desktop

%changelog
* Tue Nov 13 2018 Sergey V Turchin <zerg@altlinux.org> 1.0-alt3
- require yelp

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1.M60P.1
- built for M60P

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- show only in KDE

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M60P.1
- built for M60P

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

Name: synaptic-kde
Version: 1.0
Release: alt2

Summary: Usermode KDE bindings for synaptic
Group: System/Configuration/Packaging
License: GPL
BuildArch: noarch

Source: %name-%version.tar

Requires: synaptic

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
* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- show only in KDE

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M60P.1
- built for M60P

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

Name: seapplet
Version: 0.1.0
Release: alt1

Summary: Applet for selinux
License: GPL
Group: System/Configuration/Packaging
Packager: Andrey Kolotov <qwest@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ libqt4-devel librtmp libselinux-devel

%description
Applet for selinux.


%prep
%setup -q -n %name-%version
qmake-qt4 "CONFIG += release"

%build
%make
lrelease-qt4 security.pro

%install
%make INSTALL_ROOT=%buildroot install

mkdir -p %buildroot/%_datadir/%name/translations/
install -m644 translations/seapplet_*.qm %buildroot/%_datadir/%name/translations/
mkdir -p %buildroot/%_datadir/applications/
install -m644 %name.desktop %buildroot/%_datadir/applications/%name.desktop

mkdir -p %buildroot/%_sysconfdir/xdg/autostart/
install -m644 %name.desktop %buildroot/%_sysconfdir/xdg/autostart/%name.desktop

%files
#%doc README
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_sysconfdir/xdg/autostart/%name.desktop


%changelog
* Mon Apr 29 2013 Andriy Stepanov <stanv@altlinux.ru> 0.1.0-alt1
- Initial release

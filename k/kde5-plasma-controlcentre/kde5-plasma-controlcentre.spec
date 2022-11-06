Name: kde5-plasma-controlcentre
Version: 0.1.0
Release: alt1.gita9623a9
Summary: A control centre for KDE inspired by MacOS
License: GPL-3.0
Group: Graphical desktop/KDE
Url: https://github.com/Prayag2/kde_controlcentre
Source: %name-%version.tar

BuildArch: noarch

%description
A simple control centre widget for KDE Plasma inspired by MacOS.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/kf5/plasma/plasmoids/com.github.prayag2.controlcentre
cp -pr package/* %buildroot%_datadir/kf5/plasma/plasmoids/com.github.prayag2.controlcentre

%files
%_datadir/kf5/plasma/plasmoids/com.github.prayag2.controlcentre
%doc LICENSE

%changelog
* Sun Nov 06 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.0-alt1.gita9623a9
- Initial build for ALT


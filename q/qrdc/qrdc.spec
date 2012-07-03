Name:		qrdc
Version:	0.0.1
Release:	alt1

Summary:	QT-based Remote Desktop Connection frontend
License:	GPLv2
Group:		Networking/Remote access
URL:		http://qt-apps.org/content/show.php?action=content&content=111444
Packager:	Andrey Cherepanov <cas@altlinux.org>

Source:		%{name}_%{version}.tar.gz

BuildRequires:	gcc-c++, make, libqt4-devel 

%description
QT-based Remote Desktop Connection frontend.

%prep
%setup -q

%build
lrelease-qt4 %name.pro
qmake-qt4
make

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc doc/*
%_bindir/%name
%_datadir/qt4/translations/%{name}_*.qm
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Mon Feb 07 2011 Andrey Cherepanov <cas@altlinux.org> 0.0.1-alt1
- Initail build in Sisyphus


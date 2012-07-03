Name: pictomir
Version: 0.15.0
Release: alt2
Summary: Pictomir Child Programming System

License: GPL
Group: Education
URL: http://www.piktomir.ru/

Packager: Eugene Prokopiev <enp@altlinux.ru>

Source: %name-%version.tar

BuildRequires: gcc-c++ libqt4-devel phonon-devel

%description
Pictomir Child Programming System

%prep
%setup -q
qmake-qt4 pictomir.pro
cd src
lrelease-qt4 src.pro

%build
%make_build

%install
%make install INSTALL_ROOT=%buildroot/usr
mkdir -p %buildroot/%_desktopdir
install -m 644 *.desktop %buildroot/%_desktopdir

%files
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
* Tue Jan 10 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt2
- closes #26795

* Mon Jan 09 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt1
- new version

* Wed Dec 14 2011 Eugene Prokopiev <enp@altlinux.ru> 0.8.0-alt1
- First build for Sisyphus


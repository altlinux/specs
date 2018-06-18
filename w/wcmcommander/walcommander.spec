Name:    wcmcommander
Version: 0.20.0
Release: alt2

Summary: WCM Commander is a Far commander clone on Linux
License: %mit
Group:   File tools
URL:	 http://wcm.linderdaum.com/
#VCS:     https://github.com/corporateshark/WCMCommander

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): cmake
BuildRequires: gcc-c++ libX11-devel libfreetype-devel libsmbclient-devel libssh2-devel samba-common

Requires: fonts-ttf-dejavu fonts-ttf-liberation

Provides:  walcommander = %name-%version
Obsoletes: walcommander < %name-%version

%description
WCM Commander is a Far commander clone on Linux.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

# replaced with fonts-ttf- requires
rm -rf %buildroot%_datadir/wcm/fonts/

%files
%doc LICENSE CHANGELOG.txt readme_eng.txt README.md
%_bindir/*
%_datadir/wcm/
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Mon Jun 18 2018 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt2
- pack data files

* Sun Apr 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version
- The project was renamed to WCM Commander

* Mon Feb 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.0.1-alt1
- New version

* Mon Jan 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.18.1-alt1
- New version (ALT #30593)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- initial build for Sisyphus

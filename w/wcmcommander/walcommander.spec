Name:    wcmcommander
Version: 0.20.0
Release: alt1

Summary: WCM Commander is a Far commander clone on Linux
License: %mit
Group:   File tools
URL:	 http://wcm.linderdaum.com/
#VCS:     https://github.com/corporateshark/WCMCommander

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): cmake
BuildRequires: gcc-c++ libX11-devel libfreetype-devel libsmbclient-devel libssh2-devel samba-common

Provides:  walcommander = %name-%version
Obsoletes: walcommander < %name-%version

%description
WCM Commander is a Far commander clone on Linux.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
ln -s ../install-files src/install-files
%cmakeinstall_std

%files
%doc LICENSE CHANGELOG.txt readme_eng.txt README.md
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Sun Apr 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version
- The project was renamed to WCM Commander

* Mon Feb 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.0.1-alt1
- New version

* Mon Jan 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.18.1-alt1
- New version (ALT #30593)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- initial build for Sisyphus

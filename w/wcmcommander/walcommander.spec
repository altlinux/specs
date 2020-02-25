Name: wcmcommander
Version: 0.20.0
Release: alt3

Summary: WCM Commander is a Far commander clone on Linux
License: MIT
Group: File tools
Url: http://wcm.linderdaum.com/

# https://github.com/corporateshark/WCMCommander
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: cmake gcc-c++ libX11-devel
BuildRequires: libfreetype-devel libsmbclient-devel
BuildRequires: libssh2-devel samba-common

Requires: fonts-ttf-dejavu fonts-ttf-liberation

Provides: walcommander = %name-%version
Obsoletes: walcommander < %name-%version


%description
WCM Commander is a Far commander clone on Linux.

%prep
%setup

sed -i 's|'^#!.*python*'|#!/usr/bin/python3|' \
                        $(find ./ -name '*.py')

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
* Tue Feb 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.20.0-alt3
- Porting to python3.

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

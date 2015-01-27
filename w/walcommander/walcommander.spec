Name: walcommander
Version: 0.18.1
Release: alt1

Summary: Wal Commander GitHub Edition
License: %mit
Group: File tools
Url: https://github.com/corporateshark/WalCommander

# Source-url: https://github.com/corporateshark/WalCommander/archive/release-0.16.1.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): cmake
BuildRequires: gcc-c++ libX11-devel libfreetype-devel libsmbclient-devel libssh2-devel samba-common

%description
Wal Commander is a Far commander clone on Linux.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
ln -s ../install-files src/install-files
%cmakeinstall_std

%files
%doc LICENSE CHANGELOG CHANGELOG.GitHub readme_eng.txt README.md
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Mon Jan 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.18.1-alt1
- New version (ALT #30593)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- initial build for Sisyphus

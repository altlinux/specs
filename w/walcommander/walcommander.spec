Name: walcommander
Version: 0.20.0
Release: alt1

Summary: Wal Commander GitHub Edition
License: %mit
Group: File tools
Url: https://github.com/corporateshark/WalCommander

# Source-url: https://github.com/corporateshark/WalCommander/archive/release-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildRequires: rpm-macros-cmake cmake

# manually removed: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Sat Aug 23 2014
# optimized out: libcloog-isl4 libsasl2-3 libstdc++-devel python3-base samba-libs xorg-xproto-devel
BuildRequires: gcc-c++ libX11-devel libfreetype-devel libsmbclient-devel libssh2-devel samba-common

Requires: fonts-ttf-dejavu fonts-ttf-liberation

%description
Wal Commander is a Far commander clone on Linux.

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
%_desktopdir/*
%_datadir/wcm/
%_pixmapsdir/*

%changelog
* Mon Jun 11 2018 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt1
- new version 0.20.0 (with rpmrb script)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- initial build for Sisyphus

Name: walcommander
Version: 0.16.1
Release: alt1

Summary: Wal Commander GitHub Edition
License: %mit
Group: File tools
Url: https://github.com/corporateshark/WalCommander

# Source-url: https://github.com/corporateshark/WalCommander/archive/release-0.16.1.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

# manually removed: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Sat Aug 23 2014
# optimized out: libcloog-isl4 libsasl2-3 libstdc++-devel python3-base samba-libs xorg-xproto-devel
BuildRequires: gcc-c++ libX11-devel libfreetype-devel libsmbclient-devel libssh2-devel samba-common

%description
Wal Commander is a Far commander clone on Linux.

%prep
%setup

%build
cd wcm
# fix for start build (like in a original makefile)
rm -f libconf_ux.h
make libconf_ux.h
%make_build -f makefile.int

%install
cd wcm
#makeinstall_std
mkdir -p %buildroot%_bindir
cp -f wcm %buildroot%_bindir
cp -f -R install-files/* %buildroot%prefix

%files
%doc LICENSE CHANGELOG CHANGELOG.GitHub readme_eng.txt README.md
%_bindir/*
%_desktopdir/*
%_datadir/wcm/
#_man1dir/*

%changelog
* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- initial build for Sisyphus

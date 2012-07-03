# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: bcm43xx-fwcutter
Version: 006
Release: alt1

Summary: Utility for extracting Broadcom 43xx firmware
License: %gpl2plus
Group: System/Configuration/Hardware
Url: http://bcm43xx.berlios.de/
Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
%name is a tool which can extract firmware from various source files.
It's written for BCM43xx driver files.

%prep
%setup

%build
%make_build --silent --no-print-directory

%install
install -D %name %buildroot%_bindir/%name
install -D %name.1 %buildroot/%_man1dir/%name.1
ln -sf %_licensedir/GPL-2 COPYING

%files
%doc -d COPYING README
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 19 2007 Artem Zolochevskiy <azol@altlinux.ru> 006-alt1
- initial build for Sisyphus


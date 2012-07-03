Name: updates2iso
Version: 0.2
Release: alt1

Summary: APT-GETable ISO image from local ALTLinux updates or backports mirror
License: GPL
Group: Archiving/Cd burning

Source: %name-%version.tar.bz2

BuildArch: noarch

Requires: grep, sed, mktemp, mkisofs

%description
%name is a simple script for creating APT-GETable ISO image
from local ALTLinux updates or backports mirror

%prep
%setup -q

%install
%make_install install DESTDIR=%buildroot
ln -sf %_licensedir/GPL-2 COPYING

%files
%_bindir/*
%doc README AUTHORS
%doc -d COPYING

%changelog
* Wed Oct 18 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- initial build for Sisyphus


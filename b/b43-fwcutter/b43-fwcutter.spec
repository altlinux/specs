# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: b43-fwcutter
Version: 015
Release: alt1

Summary: Utility for extracting Broadcom 43xx firmware (for b43 driver).
License: %gpl2plus
Group: System/Configuration/Hardware
Url: http://bcm43xx.berlios.de/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
%name is a tool which can extract firmware from various source files.
It's written for BCM43xx driver files (for b43 driver).

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
* Tue Sep 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 015-alt1
- 015 release.

* Tue May 11 2010 Mikhail Efremov <sem@altlinux.org> 013-alt1
- 013 release.

* Fri Jul 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 011-alt1
- 011 release.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 009-alt1
- 009 release.

* Sun Nov 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 008-alt1
- Initial build for Sisyphus, thanks azol@ for spec. :)

* Wed Sep 19 2007 Artem Zolochevskiy <azol@altlinux.ru> 006-alt1
- initial build for Sisyphus


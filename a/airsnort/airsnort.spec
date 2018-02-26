Name: airsnort
Version: 0.2.7e
Release: alt4.qa2.1

Summary: 802.11b/g WEP Encryption key cracker
Summary(ru_RU.KOI8-R): Приложение для взлома ключей в 802.11b/g WEP сетях
Group: Networking/Other
License: GPL
Url: http://%name.sourceforge.net
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name.png

BuildRequires: libgtk+2-devel libpcap-devel
BuildRequires: desktop-file-utils

%description
AirSnort is a wireless LAN (WLAN) tool which cracks encryption keys on 802.11b
WEP networks. AirSnort operates by passively monitoring transmissions,
computing the encryption key when enough packets have been gathered.

%description -l ru_RU.KOI8-R
AirSnort это приложение для взлома ключей в 802.11b/g WEP сетях.

%prep
%setup -q

%build
%configure --prefix=/usr
%make

%install
%makeinstall

install -pm755 -d %buildroot%_datadir/applications
install -pm644 %SOURCE1 %buildroot%_datadir/applications/
install -pm755 -d %buildroot%_liconsdir
install -pm644 %SOURCE2 %buildroot%_liconsdir/
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Security \
	%buildroot%_desktopdir/airsnort.desktop

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README README.decrypt TODO
%_bindir/*
%_datadir/applications/*.desktop
%_liconsdir/*.png
%_man1dir/*

%changelog
* Sat May 21 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.7e-alt4.qa2.1
- NMU: fix desktop permissions

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.7e-alt4.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for airsnort
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.7e-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for airsnort
  * postclean-05-filetriggers for spec file

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.2.7e-alt4
- Remove unneeded update-menu calls.

* Wed Jul 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.7e-alt3
- Added desktop file.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.7e-alt2
- Fixed summaries.
- Fixed descriptions.
- Fixed buildrequires.
- Some spec cleanup.

* Tue May 17 2005 Vitaly Smirnov <device@altlinux.org> 0.2.7e-alt1
- Inital release

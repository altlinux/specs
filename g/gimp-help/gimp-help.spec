%define gimphelpdir %_datadir/gimp/2.0/help

Name: gimp-help
Version: 2.10.34
Release: alt1
Summary: Help files for the GIMP
License: GFDL
Group: Graphics

Url: http://docs.gimp.org/
Source0: https://download.gimp.org/mirror/pub/gimp/help/%name-%version.tar.bz2

Requires: gimp >= 2.10
BuildArch: noarch

BuildRequires: libgimp-devel xsltproc pngcrush python3-module-translate python3-module-libxml2 docbook-style-xsl

%description
GIMP-Help is a help system designed for use with the internal GIMP 2
help browser, external web browser and HTML renderers, and human
eyeballs.

%package en
Summary: English help files for the GIMP
Group: Graphics
Obsoletes: %name-common < %version-%release

%description en
English help files for the GIMP.

%package de
Summary: German help files for the GIMP
Group: Graphics
Obsoletes: %name-common < %version-%release

%description de
German help files for the GIMP.

%package fr
Summary: French help files for the GIMP
Group: Graphics
Obsoletes: %name-common < %version-%release

%description fr
French help files for the GIMP.

%package ru
Summary: Russian help files for the GIMP
Group: Graphics
Obsoletes: %name-common < %version-%release

%description ru
Russian help files for the GIMP.

%prep
%setup -q

%build
export ALL_LINGUAS="de en fr ru"
%configure
%make

%install
%make DESTDIR=%buildroot install

%files en
%dir %gimphelpdir
%gimphelpdir/en

%files de
%dir %gimphelpdir
%gimphelpdir/de

%files fr
%dir %gimphelpdir
%gimphelpdir/fr

%files ru
%dir %gimphelpdir
%gimphelpdir/ru

%changelog
* Mon Mar 06 2023 Valery Inozemtsev <shrek@altlinux.ru> 2.10.34-alt1
- 2.10.34

* Fri Oct 01 2021 Valery Inozemtsev <shrek@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 2.6.1-alt2
- removed set_strip_method macro

* Wed Apr 20 2011 Victor Forsiuk <force@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Oct 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Thu Apr 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Mon Jan 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt2
- split some languages into separate subpackages

* Mon Dec 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt0.M40.1
- build for branch 4.0

* Sun Dec 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.0.13-alt1
- 2.0.13

* Sat May 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.0.12-alt1
- 2.0.12
- updated build dependencies
- spec cleanup

* Sun Mar 12 2006 Anatoly Yakushin <jaa@altlinux.ru> 2.0.9-alt1
- new version

* Thu Mar 09 2006 Michael Shigorin <mike@altlinux.org> 2.0.7-alt1.1
- picked up an orphan
- spec cleanup

* Sun Mar 20 2005 Anatoly Yakushin <jaa@altlinux.ru> 2.0.7-alt1
- initial spec to ALTLINUX TEAM

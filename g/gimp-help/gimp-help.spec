%define gimpdatadir %(gimptool-2.0 --gimpdatadir)
%define gimphelpdir %gimpdatadir/help

Name: gimp-help
Version: 2.6.1
Release: alt2

Summary: Help files for the GIMP
License: GFDL
Group: Graphics

Url: http://docs.gimp.org/
Source0: http://ftp.gimp.org/pub/gimp/help/gimp-help-%version-html-en.tar
Source1: http://ftp.gimp.org/pub/gimp/help/gimp-help-%version-html-de.tar
Source2: http://ftp.gimp.org/pub/gimp/help/gimp-help-%version-html-fr.tar
Source3: http://ftp.gimp.org/pub/gimp/help/gimp-help-%version-html-ru.tar

Requires: gimp >= 2.6
BuildArch: noarch

# Upstream ships ready-made HTML-formatted helps. I see no sense in rebuilding
# them from docbook source in this package. Such build is quite time-consuming.
# This is just waste of build system time.
# BTW, ArchLinux and Mandriva went the same way.

# Automatically added by buildreq on Wed Apr 20 2011 (-bi)
BuildRequires: libgimp-devel

# Just to speed build up a little... :)
%set_fixup_method skip
%set_cleanup_method skip
%set_compress_method none
%set_verify_elf_method skip

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
%setup -c -a 1 -a 2 -a 3

%build

%install
mkdir -p %buildroot%gimphelpdir
cp -r gimp-help-2/html/* %buildroot%gimphelpdir

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

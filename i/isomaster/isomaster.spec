Name: isomaster
Version: 1.3.8
Release: alt1

Summary: An open-source, graphical CD image editor
License: GPL
Group: File tools

Url: http://littlesvr.ca/isomaster
Source: %url/releases/isomaster-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Jan 05 2010 (-bi)
BuildRequires: libgtk+2-devel

%description
ISO Master: an ISO9660 remastering utility

%prep
%setup

%build
# PREFIX is required to specify current dir for icons;
# SMP build prone to failures
%make PREFIX=%prefix

%install
%makeinstall_std PREFIX=%prefix
%find_lang %name
rm -rf %buildroot%_defaultdocdir/bkisofs

%files -f %name.lang
%_bindir/%name
%_man1dir/*
%_datadir/%name/icons/*
%doc CHANGELOG.TXT CREDITS.TXT LICENCE.TXT README.TXT
%_desktopdir/*.desktop

%changelog
* Thu Jan 06 2011 Michael Shigorin <mike@altlinux.org> 1.3.8-alt1
- 1.3.8

* Tue Jan 05 2010 Michael Shigorin <mike@altlinux.org> 1.3.7-alt1
- 1.3.7
- dropped patch (docs installation fixed upstream)
- buildreq

* Wed Sep 16 2009 Michael Shigorin <mike@altlinux.org> 1.3.6-alt1
- 1.3.6
  + repackaged tarball due to obvious upstream lapse with directory
  + fixed docs installation (another directory lapse)

* Tue Jun 30 2009 Michael Shigorin <mike@altlinux.org> 1.3.5-alt2
- fixed broken custom desktop file (closes: #20622)

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.3.5-alt1
- 1.3.5

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- applied repocop patch

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for isomaster

* Mon Feb 04 2008 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- 1.3.1

* Thu Dec 20 2007 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- 1.3

* Mon Oct 29 2007 Michael Shigorin <mike@altlinux.org> 1.2-alt1
- 1.2

* Mon Sep 10 2007 Michael Shigorin <mike@altlinux.org> 1.1-alt1
- 1.1
- no more need to shuffle manpages around, hooray!

* Sun Jan 28 2007 Michael Shigorin <mike@altlinux.org> 0.7-alt1
- 0.7
- added manpage and translations

* Sun Oct 29 2006 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- built for ALT Linux
- spec adaptation/cleanup

* Sun Oct 29 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5-1
 - updated to 0.5

* Wed Sep 28 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.4-1
 - updated to 0.4
 - removed patch for Makefile (my suggestions was included in the original release)

* Tue Sep 26 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.3-2
 - tests with new Makefile

* Sun Sep 24 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.3-1
 - initial release


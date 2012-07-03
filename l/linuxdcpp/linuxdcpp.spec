%define debug 0

Name: linuxdcpp
Version: 1.0.3
Release: alt1.1.qa1
Summary: Linux Direct Connect Client
License: GPL
Group: Networking/File transfer
Url: http://linuxdcpp.berlios.de

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Source: %name-%version.tar

BuildRequires: bzlib-devel glib2-devel libglade2-devel libgtk+2-devel scons zlib-devel libssl-devel
BuildRequires: gcc-c++ >= 3.4
BuildRequires: desktop-file-utils

%description
A client for Direct Connect ++ file sharing network.

%prep
%setup

%build
%if %debug
scons release=1 debug=1 PREFIX="/usr" FAKE_ROOT="%buildroot"
%else
scons release=1 debug=0 PREFIX="/usr" FAKE_ROOT="%buildroot"
%endif

%install
scons install

# icon for menu file
mkdir -p %buildroot%_datadir/icons/hicolor
cp -rp linuxdcpp-icons/* %buildroot%_datadir/icons/hicolor/

# menu file
mkdir -p %buildroot%_desktopdir
install -pm644 linuxdcpp.desktop %buildroot%_desktopdir/linuxdcpp.desktop

# move to more generic place
mv %buildroot%_docdir/%name %buildroot%_docdir/%name-%version

%if %debug
%add_strip_skiplist %_bindir/linuxdcpp
%endif
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=FileTransfer \
	--add-category=P2P \
	%buildroot%_desktopdir/linuxdcpp.desktop

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/linuxdcpp.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_docdir/%name-%version

%changelog
* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.3-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for linuxdcpp
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Mar 18 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0.3-alt1
- 1.0.3
- Updated linuxdcpp.desktop
- Removed from spec deprecated update-menus calls

* Fri Jul 04 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.0.2-alt1
- Updated to CVS snapshot from 20080703.
- Security fixes:
  + CVE-2008-2953
  + CVE-2008-2954
  (Linux DC++ NULL Pointer Dereference and Incomplete Message Denial of
  Service) (Closes: #16248)

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.0.2-alt0.20080128
- 1.0.2 CVS from 20080128.

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt1.20071204
- CVS from 20071204.

* Tue Nov 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt5.20071113
- CVS from 20071113.

* Tue Aug 07 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt4.20070804
- CVS from 20070804.

* Mon Jul 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt4.20070707
- CVS from 20070707.

* Thu Jun 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt4.20070506
- Removed Tango DL/UL icons as suggested by zerg@ in #11950.

* Tue May 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt3.20070506
- Added Tango icons as suggested by shrek@.

* Mon May 07 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt2.20070506
- CVS from 20070506.

* Sun Apr 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt2.20070328
- Added magnet links patch by Max Lapan.

* Thu Mar 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20070328
- CVS from 20070328.

* Tue Mar 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20070324
- CVS from 20070324.

* Mon Feb 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20070204
- CVS from 20070204.
- Upstream fixed all the problems with encodings and such.
- Patches dropped.
- README dropped.
- Modified startup .desktop file.

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20070105
- CVS from 20070105.
- Added quick fix patch for "help" button.

* Mon Jan 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20070101
- CVS from 20070101.

* Sun Nov 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20061105
- CVS from 20061105.

* Sun Oct 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20061015
- CVS from 20061015.
- New launching scheme.
- Moved to git.

* Mon Aug 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060828
- CVS from 20060828.
- Some spec cleanup.
- Moved docs to %%_datadir/doc/%%name-%%version.
- README is now packaged too.

* Fri Aug 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060823.1
- Fixed patch2.

* Wed Aug 23 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060823
- current CVS.
- Added patch2 to deal with codepages.

* Thu Aug 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060817
- current cvs.

* Sat Aug 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060805
- current CVS.
- Fallback locale is CP1251.

* Sat Jul 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060715
- current CVS.

* Mon Jun 26 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060626
- current CVS.
- added patch1 to solve problems with russian hubs.

* Tue Jun 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060613
- current CVS.

* Wed May 31 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060531
- current CVS.
- removed patch1, as it merged upstream.

* Tue May 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060530.5
- current CVS.
- spec file cleanup.
- new icon.
- dropped oldskool menu.
- fixed startup file.

* Sat Feb 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060225
- current CVS.
- updated path patch.
- added desktop file.

* Tue Jan 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060117
- updated savecolumn patch.

* Wed Jan 11 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060111
- added savecolumnwidth patch by Steven Sheehy.

* Fri Jan 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20060106
- CVS from 06012006.
- patches from Steven Sheehy are into mainstream.

* Wed Dec 28 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20051227
- CVS from 27122005.
- Added patch by Steven Sheehy fixing file list problems.

* Sun Dec 25 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20051224
- CVS from 24122005.

* Wed Dec 14 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20051215
- CVS from 15122005.

* Sun Nov 06 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20051106
- CVS from 06112005.

* Thu Oct 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20051020
- CVS from 20102005. 

* Sun Oct 16 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20051016
- CVS from 16102005.

* Wed Sep 28 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20050923
- CVS from 23092005.

* Sun Sep 18 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20050907
- CVS from 07092005.

* Sun Aug 21 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20050821
- CVS from 21082005
- removed transferlist patch.

* Mon Jul 11 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20050711
- CVS from 11072005
- Read README.ALT.KOI8-R for details.

* Sat Jun 25 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt1.20050625
- CVS from 25062005.
- Initial build for Sisyphus.
- Added transferlist context-menu patch.

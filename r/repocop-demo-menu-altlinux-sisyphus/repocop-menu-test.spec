Name: repocop-demo-menu-altlinux-sisyphus
Version: 0.04.20180111
Release: alt1

Summary: menu test with demo applications
License: %lgpl2plus
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl(File/Path.pm) perl(DBI.pm) perl(DBD/SQLite.pm)
BuildArch: noarch
Requires: /usr/bin/kdialog

%description
The package contains demonstration versions of desktop menu entries for all 
existing sisyphus applications. Use it for menu layout testing purposes.

%prep
%setup

%build
#./generate_fake_menus freedesktop-desktop.db

%install
mkdir -p %buildroot%_datadir/desktop-directories %buildroot%_sysconfdir/xdg/menus
mkdir -p %buildroot%_bindir
#%buildroot%_desktopdir

cp -a usr %buildroot/

cat > %buildroot%_bindir/demo-menu-entry << 'EOF'
#!/bin/sh
categories=`grep '^Categories=' "$1"`
terminal=`grep '^X-Demo-Terminal=' "$1" | sed -e s,X-Demo-,,`
id=`grep '^X-Demo-ID=' "$1" | sed -e s,X-Demo-,,`
kdialog --title 'demo application' --msgbox 'This is menu demo, not a real application.\nUninstall %name to remove me.\n\n'"file=$1\n\n""$categories\n$terminal\n""$id"
EOF
chmod 755 %buildroot%_bindir/demo-menu-entry
install -Dm644 demo-menu-entry.png %buildroot%_liconsdir/demo-menu-entry.png

%files 
%_bindir/demo-menu-entry
%_liconsdir/demo-menu-entry.png
%_datadir/kde*/*
%_desktopdir/*

%changelog
* Thu Jan 11 2018 Cronbuild Service <cronbuild@altlinux.org> 0.04.20180111-alt1
- repocop cronbuild 20180111. At your service.

* Thu Dec 28 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171228-alt1
- repocop cronbuild 20171228. At your service.

* Thu Dec 14 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171214-alt1
- repocop cronbuild 20171214. At your service.

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171130-alt1
- repocop cronbuild 20171130. At your service.

* Thu Nov 16 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171116-alt1
- repocop cronbuild 20171116. At your service.

* Thu Nov 02 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171102-alt1
- repocop cronbuild 20171102. At your service.

* Tue Oct 17 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171017-alt1
- repocop cronbuild 20171017. At your service.

* Tue Oct 03 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20171003-alt1
- repocop cronbuild 20171003. At your service.

* Tue Sep 19 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170919-alt1
- repocop cronbuild 20170919. At your service.

* Tue Sep 05 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170905-alt1
- repocop cronbuild 20170905. At your service.

* Tue Aug 22 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170822-alt1
- repocop cronbuild 20170822. At your service.

* Tue Aug 08 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170808-alt1
- repocop cronbuild 20170808. At your service.

* Tue Jul 25 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170725-alt1
- repocop cronbuild 20170725. At your service.

* Tue Jul 11 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170711-alt1
- repocop cronbuild 20170711. At your service.

* Tue Jun 27 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170627-alt1
- repocop cronbuild 20170627. At your service.

* Tue Jun 13 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170613-alt1
- repocop cronbuild 20170613. At your service.

* Tue May 30 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170530-alt1
- repocop cronbuild 20170530. At your service.

* Tue May 16 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170516-alt1
- repocop cronbuild 20170516. At your service.

* Tue May 02 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170502-alt1
- repocop cronbuild 20170502. At your service.

* Tue Apr 18 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170418-alt1
- repocop cronbuild 20170418. At your service.

* Tue Apr 04 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170404-alt1
- repocop cronbuild 20170404. At your service.

* Tue Mar 21 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170321-alt1
- repocop cronbuild 20170321. At your service.

* Tue Mar 07 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170307-alt1
- repocop cronbuild 20170307. At your service.

* Tue Feb 21 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170221-alt1
- repocop cronbuild 20170221. At your service.

* Tue Feb 07 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170207-alt1
- repocop cronbuild 20170207. At your service.

* Tue Jan 24 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170124-alt1
- repocop cronbuild 20170124. At your service.

* Tue Jan 10 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04.20170110-alt1
- repocop cronbuild 20170110. At your service.

* Tue Dec 27 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161227-alt1
- repocop cronbuild 20161227. At your service.

* Tue Dec 13 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161213-alt1
- repocop cronbuild 20161213. At your service.

* Sat Nov 26 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161126-alt1
- repocop cronbuild 20161126. At your service.

* Sat Nov 12 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161112-alt1
- repocop cronbuild 20161112. At your service.

* Sat Oct 29 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161029-alt1
- repocop cronbuild 20161029. At your service.

* Sat Oct 15 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161015-alt1
- repocop cronbuild 20161015. At your service.

* Sat Oct 01 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20161001-alt1
- repocop cronbuild 20161001. At your service.

* Sat Sep 17 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160917-alt1
- repocop cronbuild 20160917. At your service.

* Sat Sep 03 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160903-alt1
- repocop cronbuild 20160903. At your service.

* Sat Aug 20 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160820-alt1
- repocop cronbuild 20160820. At your service.

* Sat Aug 06 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160806-alt1
- repocop cronbuild 20160806. At your service.

* Sat Jul 23 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160723-alt1
- repocop cronbuild 20160723. At your service.

* Sat Jul 09 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160709-alt1
- repocop cronbuild 20160709. At your service.

* Sat Jun 25 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160625-alt1
- repocop cronbuild 20160625. At your service.

* Sat Jun 11 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160611-alt1
- repocop cronbuild 20160611. At your service.

* Sat May 28 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160528-alt1
- repocop cronbuild 20160528. At your service.

* Wed May 04 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160504-alt1
- repocop cronbuild 20160504. At your service.

* Wed Apr 20 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160420-alt1
- repocop cronbuild 20160420. At your service.

* Wed Apr 06 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160406-alt1
- repocop cronbuild 20160406. At your service.

* Tue Mar 22 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160322-alt1
- repocop cronbuild 20160322. At your service.

* Tue Mar 08 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160308-alt1
- repocop cronbuild 20160308. At your service.

* Tue Feb 23 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160223-alt1
- repocop cronbuild 20160223. At your service.

* Tue Feb 09 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160209-alt1
- repocop cronbuild 20160209. At your service.

* Tue Jan 26 2016 Cronbuild Service <cronbuild@altlinux.org> 0.04.20160126-alt1
- repocop cronbuild 20160126. At your service.

* Sat Dec 12 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20151212-alt1
- repocop cronbuild 20151212. At your service.

* Sat Nov 28 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20151128-alt1
- repocop cronbuild 20151128. At your service.

* Sat Nov 14 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20151114-alt1
- repocop cronbuild 20151114. At your service.

* Sat Oct 31 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20151031-alt1
- repocop cronbuild 20151031. At your service.

* Sat Oct 17 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20151017-alt1
- repocop cronbuild 20151017. At your service.

* Sat Oct 03 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20151003-alt1
- repocop cronbuild 20151003. At your service.

* Sat Sep 19 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150919-alt1
- repocop cronbuild 20150919. At your service.

* Sat Sep 05 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150905-alt1
- repocop cronbuild 20150905. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150823-alt1
- repocop cronbuild 20150823. At your service.

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150730-alt1
- repocop cronbuild 20150730. At your service.

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150716-alt1
- repocop cronbuild 20150716. At your service.

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150702-alt1
- repocop cronbuild 20150702. At your service.

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150618-alt1
- repocop cronbuild 20150618. At your service.

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150604-alt1
- repocop cronbuild 20150604. At your service.

* Thu May 21 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150521-alt1
- repocop cronbuild 20150521. At your service.

* Thu May 07 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150507-alt1
- repocop cronbuild 20150507. At your service.

* Thu Apr 23 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150423-alt1
- repocop cronbuild 20150423. At your service.

* Thu Apr 09 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150409-alt1
- repocop cronbuild 20150409. At your service.

* Thu Mar 26 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150326-alt1
- repocop cronbuild 20150326. At your service.

* Thu Mar 12 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150312-alt1
- repocop cronbuild 20150312. At your service.

* Thu Feb 26 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150226-alt1
- repocop cronbuild 20150226. At your service.

* Thu Feb 12 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150212-alt1
- repocop cronbuild 20150212. At your service.

* Thu Jan 29 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150129-alt1
- repocop cronbuild 20150129. At your service.

* Thu Jan 15 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150115-alt1
- repocop cronbuild 20150115. At your service.

* Thu Jan 01 2015 Cronbuild Service <cronbuild@altlinux.org> 0.04.20150101-alt1
- repocop cronbuild 20150101. At your service.

* Thu Dec 18 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20141218-alt1
- repocop cronbuild 20141218. At your service.

* Thu Dec 04 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20141204-alt1
- repocop cronbuild 20141204. At your service.

* Thu Nov 20 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20141120-alt1
- repocop cronbuild 20141120. At your service.

* Thu Nov 06 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20141106-alt1
- repocop cronbuild 20141106. At your service.

* Thu Oct 23 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20141023-alt1
- repocop cronbuild 20141023. At your service.

* Thu Oct 09 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20141009-alt1
- repocop cronbuild 20141009. At your service.

* Thu Sep 25 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140925-alt1
- repocop cronbuild 20140925. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140911-alt1
- repocop cronbuild 20140911. At your service.

* Thu Jul 03 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140703-alt1
- repocop cronbuild 20140703. At your service.

* Thu Jun 19 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140619-alt1
- repocop cronbuild 20140619. At your service.

* Thu Jun 05 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140605-alt1
- repocop cronbuild 20140605. At your service.

* Thu May 22 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140522-alt1
- repocop cronbuild 20140522. At your service.

* Thu May 08 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140508-alt1
- repocop cronbuild 20140508. At your service.

* Thu Apr 24 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140424-alt1
- repocop cronbuild 20140424. At your service.

* Thu Apr 10 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140410-alt1
- repocop cronbuild 20140410. At your service.

* Thu Mar 27 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140327-alt1
- repocop cronbuild 20140327. At your service.

* Thu Mar 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140313-alt1
- repocop cronbuild 20140313. At your service.

* Thu Feb 27 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140227-alt1
- repocop cronbuild 20140227. At your service.

* Thu Feb 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140213-alt1
- repocop cronbuild 20140213. At your service.

* Thu Jan 30 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140130-alt1
- repocop cronbuild 20140130. At your service.

* Thu Jan 16 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140116-alt1
- repocop cronbuild 20140116. At your service.

* Thu Jan 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04.20140102-alt1
- repocop cronbuild 20140102. At your service.

* Thu Dec 19 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20131219-alt1
- repocop cronbuild 20131219. At your service.

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20131205-alt1
- repocop cronbuild 20131205. At your service.

* Thu Nov 21 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20131121-alt1
- repocop cronbuild 20131121. At your service.

* Thu Nov 07 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20131107-alt1
- repocop cronbuild 20131107. At your service.

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20131024-alt1
- repocop cronbuild 20131024. At your service.

* Thu Oct 10 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20131010-alt1
- repocop cronbuild 20131010. At your service.

* Thu Sep 26 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130926-alt1
- repocop cronbuild 20130926. At your service.

* Thu Sep 12 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130912-alt1
- repocop cronbuild 20130912. At your service.

* Thu Aug 29 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130829-alt1
- repocop cronbuild 20130829. At your service.

* Thu Aug 15 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130815-alt1
- repocop cronbuild 20130815. At your service.

* Thu Aug 01 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130801-alt1
- repocop cronbuild 20130801. At your service.

* Thu Jul 18 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130718-alt1
- repocop cronbuild 20130718. At your service.

* Thu Jul 04 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130704-alt1
- repocop cronbuild 20130704. At your service.

* Thu Jun 20 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130620-alt1
- repocop cronbuild 20130620. At your service.

* Wed Jun 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130605-alt1
- repocop cronbuild 20130605. At your service.

* Wed May 22 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130522-alt1
- repocop cronbuild 20130522. At your service.

* Wed May 08 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130508-alt1
- repocop cronbuild 20130508. At your service.

* Sun Apr 14 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130414-alt1
- repocop cronbuild 20130414. At your service.

* Sun Mar 31 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130331-alt1
- repocop cronbuild 20130331. At your service.

* Sun Mar 17 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130317-alt1
- repocop cronbuild 20130317. At your service.

* Sun Mar 03 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130303-alt1
- repocop cronbuild 20130303. At your service.

* Sun Feb 17 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130217-alt1
- repocop cronbuild 20130217. At your service.

* Sun Feb 03 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130203-alt1
- repocop cronbuild 20130203. At your service.

* Sun Jan 20 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130120-alt1
- repocop cronbuild 20130120. At your service.

* Sun Jan 06 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04.20130106-alt1
- repocop cronbuild 20130106. At your service.

* Sun Dec 23 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20121223-alt1
- repocop cronbuild 20121223. At your service.

* Sun Dec 09 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20121209-alt1
- repocop cronbuild 20121209. At your service.

* Sun Nov 25 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20121125-alt1
- repocop cronbuild 20121125. At your service.

* Sun Nov 11 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20121111-alt1
- repocop cronbuild 20121111. At your service.

* Sun Oct 28 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20121028-alt1
- repocop cronbuild 20121028. At your service.

* Sun Oct 14 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20121014-alt1
- repocop cronbuild 20121014. At your service.

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120930-alt1
- repocop cronbuild 20120930. At your service.

* Wed Sep 12 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120912-alt1
- repocop cronbuild 20120912. At your service.

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120829-alt1
- repocop cronbuild 20120829. At your service.

* Wed Aug 15 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120815-alt1
- repocop cronbuild 20120815. At your service.

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120801-alt1
- repocop cronbuild 20120801. At your service.

* Wed Jul 18 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120718-alt1
- repocop cronbuild 20120718. At your service.

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120704-alt1
- repocop cronbuild 20120704. At your service.

* Wed Jun 20 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120620-alt1
- repocop cronbuild 20120620. At your service.

* Wed Jun 06 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120606-alt1
- repocop cronbuild 20120606. At your service.

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120523-alt1
- repocop cronbuild 20120523. At your service.

* Wed May 09 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120509-alt1
- repocop cronbuild 20120509. At your service.

* Wed Apr 25 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120425-alt1
- repocop cronbuild 20120425. At your service.

* Wed Apr 11 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120411-alt1
- repocop cronbuild 20120411. At your service.

* Wed Mar 28 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120328-alt1
- repocop cronbuild 20120328. At your service.

* Wed Mar 14 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120314-alt1
- repocop cronbuild 20120314. At your service.

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120229-alt1
- repocop cronbuild 20120229. At your service.

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120215-alt1
- repocop cronbuild 20120215. At your service.

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120201-alt1
- repocop cronbuild 20120201. At your service.

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120118-alt1
- repocop cronbuild 20120118. At your service.

* Wed Jan 04 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120104-alt1
- repocop cronbuild 20120104. At your service.

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111221-alt1
- repocop cronbuild 20111221. At your service.

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111207-alt1
- repocop cronbuild 20111207. At your service.

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111123-alt1
- repocop cronbuild 20111123. At your service.

* Wed Nov 09 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111109-alt1
- repocop cronbuild 20111109. At your service.

* Wed Oct 26 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111026-alt1
- repocop cronbuild 20111026. At your service.

* Wed Oct 12 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111012-alt1
- repocop cronbuild 20111012. At your service.

* Wed Sep 28 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110928-alt1
- repocop cronbuild 20110928. At your service.

* Wed Sep 14 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110914-alt1
- repocop cronbuild 20110914. At your service.

* Wed Aug 31 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110831-alt1
- repocop cronbuild 20110831. At your service.

* Wed Aug 17 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110817-alt1
- repocop cronbuild 20110817. At your service.

* Wed Aug 03 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110803-alt1
- repocop cronbuild 20110803. At your service.

* Wed Jul 20 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110720-alt1
- repocop cronbuild 20110720. At your service.

* Wed Jul 06 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110706-alt1
- repocop cronbuild 20110706. At your service.

* Wed Jun 22 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110622-alt1
- repocop cronbuild 20110622. At your service.

* Wed Jun 08 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110608-alt1
- repocop cronbuild 20110608. At your service.

* Wed May 25 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110525-alt1
- repocop cronbuild 20110525. At your service.

* Wed May 11 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110511-alt1
- repocop cronbuild 20110511. At your service.

* Wed Apr 27 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110427-alt1
- repocop cronbuild 20110427. At your service.

* Thu Apr 21 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110421-alt1
- repocop cronbuild 20110421. At your service.

* Thu Apr 07 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110407-alt1
- repocop cronbuild 20110407. At your service.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.04.20110329-alt1
- repocop cronbuild 20110329. At your service.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.04.20110328-alt1
- update 20110328

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.04.20110326-alt1
- package generated .desktop instead of db

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.03.20110324-alt1
- support for Terminal key

* Tue Mar 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.02.20110321-alt1
- added categories info.

* Wed Mar 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.01.20110315-alt1
- Initial build


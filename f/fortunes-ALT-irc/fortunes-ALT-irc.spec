%define pkgname ALT-irc

Name: fortunes-ALT-irc
Version: 20120626
Release: alt2

Summary: Quotes from IRC channel #altlinux (freenode network)
Group: Games/Other
License: distributable

Url: http://bash.altlinux.org/

Packager: Andrey Rahmatullin <wrar@altlinux.org>

BuildArch: noarch

Source: %pkgname.bz2

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%description
Quotes from IRC channel #altlinux (freenode network), gathered at
http://bash.altlinux.org/

%install
mkdir -p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 > %buildroot%_gamesdatadir/fortune/%pkgname
strfile %buildroot%_gamesdatadir/fortune/%pkgname %buildroot%_gamesdatadir/fortune/%pkgname.dat

%files
%_gamesdatadir/fortune/*

%changelog
* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 20120626-alt2
- repocop cronbuild 20120626. At your service.

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 20120619-alt2
- repocop cronbuild 20120619. At your service.

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 20120612-alt2
- repocop cronbuild 20120612. At your service.

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 20120605-alt2
- repocop cronbuild 20120605. At your service.

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 20120529-alt2
- repocop cronbuild 20120529. At your service.

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 20120522-alt2
- repocop cronbuild 20120522. At your service.

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 20120515-alt2
- repocop cronbuild 20120515. At your service.

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 20120508-alt2
- repocop cronbuild 20120508. At your service.

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20120424-alt2
- repocop cronbuild 20120424. At your service.

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120417-alt2
- repocop cronbuild 20120417. At your service.

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 20120410-alt2
- repocop cronbuild 20120410. At your service.

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 20120402-alt2
- repocop cronbuild 20120402. At your service.

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 20120326-alt2
- repocop cronbuild 20120326. At your service.

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 20120319-alt2
- repocop cronbuild 20120319. At your service.

* Mon Mar 12 2012 Cronbuild Service <cronbuild@altlinux.org> 20120312-alt2
- repocop cronbuild 20120312. At your service.

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 20120221-alt2
- repocop cronbuild 20120221. At your service.

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 20120214-alt2
- repocop cronbuild 20120214. At your service.

* Tue Feb 07 2012 Cronbuild Service <cronbuild@altlinux.org> 20120207-alt2
- repocop cronbuild 20120207. At your service.

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 20120131-alt2
- repocop cronbuild 20120131. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20120124-alt2
- repocop cronbuild 20120124. At your service.

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120117-alt2
- repocop cronbuild 20120117. At your service.

* Tue Jan 03 2012 Cronbuild Service <cronbuild@altlinux.org> 20120103-alt2
- repocop cronbuild 20120103. At your service.

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 20111227-alt2
- repocop cronbuild 20111227. At your service.

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 20111220-alt2
- repocop cronbuild 20111220. At your service.

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 20111213-alt2
- repocop cronbuild 20111213. At your service.

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 20111206-alt2
- repocop cronbuild 20111206. At your service.

* Tue Nov 29 2011 Cronbuild Service <cronbuild@altlinux.org> 20111129-alt2
- repocop cronbuild 20111129. At your service.

* Tue Nov 22 2011 Cronbuild Service <cronbuild@altlinux.org> 20111122-alt2
- repocop cronbuild 20111122. At your service.

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20111116-alt2
- repocop cronbuild 20111116. At your service.

* Wed Nov 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20111109-alt2
- repocop cronbuild 20111109. At your service.

* Wed Nov 02 2011 Cronbuild Service <cronbuild@altlinux.org> 20111102-alt2
- repocop cronbuild 20111102. At your service.

* Wed Oct 26 2011 Cronbuild Service <cronbuild@altlinux.org> 20111026-alt2
- repocop cronbuild 20111026. At your service.

* Wed Oct 19 2011 Cronbuild Service <cronbuild@altlinux.org> 20111019-alt2
- repocop cronbuild 20111019. At your service.

* Wed Oct 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20111012-alt2
- repocop cronbuild 20111012. At your service.

* Tue Oct 04 2011 Cronbuild Service <cronbuild@altlinux.org> 20111004-alt2
- repocop cronbuild 20111004. At your service.

* Tue Sep 27 2011 Cronbuild Service <cronbuild@altlinux.org> 20110927-alt2
- repocop cronbuild 20110927. At your service.

* Tue Sep 20 2011 Cronbuild Service <cronbuild@altlinux.org> 20110920-alt2
- repocop cronbuild 20110920. At your service.

* Tue Sep 13 2011 Cronbuild Service <cronbuild@altlinux.org> 20110913-alt2
- repocop cronbuild 20110913. At your service.

* Tue Sep 06 2011 Cronbuild Service <cronbuild@altlinux.org> 20110906-alt2
- repocop cronbuild 20110906. At your service.

* Tue Aug 30 2011 Cronbuild Service <cronbuild@altlinux.org> 20110830-alt2
- repocop cronbuild 20110830. At your service.

* Tue Aug 23 2011 Cronbuild Service <cronbuild@altlinux.org> 20110823-alt2
- repocop cronbuild 20110823. At your service.

* Tue Aug 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20110816-alt2
- repocop cronbuild 20110816. At your service.

* Tue Aug 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110809-alt2
- repocop cronbuild 20110809. At your service.

* Tue Aug 02 2011 Cronbuild Service <cronbuild@altlinux.org> 20110802-alt2
- repocop cronbuild 20110802. At your service.

* Tue Jul 26 2011 Cronbuild Service <cronbuild@altlinux.org> 20110726-alt2
- repocop cronbuild 20110726. At your service.

* Tue Jul 19 2011 Cronbuild Service <cronbuild@altlinux.org> 20110719-alt2
- repocop cronbuild 20110719. At your service.

* Tue Jul 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110712-alt2
- repocop cronbuild 20110712. At your service.

* Tue Jul 05 2011 Cronbuild Service <cronbuild@altlinux.org> 20110705-alt2
- repocop cronbuild 20110705. At your service.

* Tue Jun 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110628-alt2
- repocop cronbuild 20110628. At your service.

* Tue Jun 21 2011 Cronbuild Service <cronbuild@altlinux.org> 20110621-alt2
- repocop cronbuild 20110621. At your service.

* Tue Jun 14 2011 Cronbuild Service <cronbuild@altlinux.org> 20110614-alt2
- repocop cronbuild 20110614. At your service.

* Tue Jun 07 2011 Cronbuild Service <cronbuild@altlinux.org> 20110607-alt2
- repocop cronbuild 20110607. At your service.

* Tue May 31 2011 Cronbuild Service <cronbuild@altlinux.org> 20110531-alt2
- repocop cronbuild 20110531. At your service.

* Tue May 24 2011 Cronbuild Service <cronbuild@altlinux.org> 20110524-alt2
- repocop cronbuild 20110524. At your service.

* Tue May 17 2011 Cronbuild Service <cronbuild@altlinux.org> 20110517-alt2
- repocop cronbuild 20110517. At your service.

* Tue May 10 2011 Cronbuild Service <cronbuild@altlinux.org> 20110510-alt2
- repocop cronbuild 20110510. At your service.

* Tue May 03 2011 Cronbuild Service <cronbuild@altlinux.org> 20110503-alt2
- repocop cronbuild 20110503. At your service.

* Tue Apr 26 2011 Cronbuild Service <cronbuild@altlinux.org> 20110426-alt2
- repocop cronbuild 20110426. At your service.

* Tue Apr 19 2011 Cronbuild Service <cronbuild@altlinux.org> 20110419-alt2
- repocop cronbuild 20110419. At your service.

* Tue Apr 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110412-alt2
- repocop cronbuild 20110412. At your service.

* Tue Apr 05 2011 Cronbuild Service <cronbuild@altlinux.org> 20110405-alt2
- repocop cronbuild 20110405. At your service.

* Tue Mar 29 2011 Cronbuild Service <cronbuild@altlinux.org> 20110329-alt2
- repocop cronbuild 20110329. At your service.

* Tue Mar 22 2011 Cronbuild Service <cronbuild@altlinux.org> 20110322-alt2
- repocop cronbuild 20110322. At your service.

* Tue Mar 15 2011 Cronbuild Service <cronbuild@altlinux.org> 20110315-alt2
- repocop cronbuild 20110315. At your service.

* Tue Mar 08 2011 Cronbuild Service <cronbuild@altlinux.org> 20110308-alt2
- repocop cronbuild 20110308. At your service.

* Tue Mar 01 2011 Cronbuild Service <cronbuild@altlinux.org> 20110301-alt2
- repocop cronbuild 20110301. At your service.

* Tue Feb 22 2011 Cronbuild Service <cronbuild@altlinux.org> 20110222-alt2
- repocop cronbuild 20110222. At your service.

* Tue Feb 15 2011 Cronbuild Service <cronbuild@altlinux.org> 20110215-alt2
- repocop cronbuild 20110215. At your service.

* Tue Feb 08 2011 Cronbuild Service <cronbuild@altlinux.org> 20110208-alt2
- repocop cronbuild 20110208. At your service.

* Tue Feb 01 2011 Cronbuild Service <cronbuild@altlinux.org> 20110201-alt2
- repocop cronbuild 20110201. At your service.

* Tue Jan 25 2011 Cronbuild Service <cronbuild@altlinux.org> 20110125-alt2
- repocop cronbuild 20110125. At your service.

* Tue Jan 18 2011 Cronbuild Service <cronbuild@altlinux.org> 20110118-alt2
- repocop cronbuild 20110118. At your service.

* Tue Jan 11 2011 Cronbuild Service <cronbuild@altlinux.org> 20110111-alt2
- repocop cronbuild 20110111. At your service.

* Tue Jan 04 2011 Cronbuild Service <cronbuild@altlinux.org> 20110104-alt2
- repocop cronbuild 20110104. At your service.

* Tue Dec 28 2010 Cronbuild Service <cronbuild@altlinux.org> 20101228-alt2
- repocop cronbuild 20101228. At your service.

* Tue Dec 21 2010 Cronbuild Service <cronbuild@altlinux.org> 20101221-alt2
- repocop cronbuild 20101221. At your service.

* Tue Dec 14 2010 Cronbuild Service <cronbuild@altlinux.org> 20101214-alt2
- repocop cronbuild 20101214. At your service.

* Tue Dec 07 2010 Cronbuild Service <cronbuild@altlinux.org> 20101207-alt2
- repocop cronbuild 20101207. At your service.

* Tue Nov 30 2010 Cronbuild Service <cronbuild@altlinux.org> 20101130-alt2
- repocop cronbuild 20101130. At your service.

* Tue Nov 23 2010 Cronbuild Service <cronbuild@altlinux.org> 20101123-alt2
- repocop cronbuild 20101123. At your service.

* Tue Nov 16 2010 Cronbuild Service <cronbuild@altlinux.org> 20101116-alt2
- repocop cronbuild 20101116. At your service.

* Mon Nov 15 2010 Cronbuild Service <cronbuild@altlinux.org> 20101115-alt2
- repocop cronbuild 20101115. At your service.

* Mon Nov 15 2010 Artem Zolochevskiy <azol@altlinux.ru> 20101115-alt1
- remove azol@ quotes

* Sat Sep 25 2010 Andrey Rahmatullin <wrar@altlinux.org> 20100925-alt1
- first Fortunator release
- 1686 quotes

* Mon Jan 04 2010 Andrey Rahmatullin <wrar@altlinux.ru> 20100104-alt1
- 93 new quotes

* Sat Sep 05 2009 Andrey Rahmatullin <wrar@altlinux.ru> 20090905-alt1
- 157 new quotes

* Fri Jan 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 20090130-alt1
- 68 new quotes

* Tue Oct 21 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20081021-alt1
- 94 new quotes

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20080809-alt1
- 164 new quotes

* Wed Apr 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20080401-alt1
- April Fools' Day edition
- 65 new quotes

* Mon Mar 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20080310-alt1
- 107 new quotes

* Tue Jan 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20080129-alt1
- 83 new quotes

* Tue Dec 25 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20071225-alt1
- 52 new quotes

* Wed Oct 24 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20071024-alt1
- 28 new quotes

* Sat Sep 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070922-alt2
- 4 new quotes

* Sat Sep 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070922-alt1
- 21 new quotes

* Thu Aug 16 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070816-alt1
- 36 new quotes

* Tue Jul 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070731-alt1
- 33 new quotes

* Sat Jun 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070623-alt1
- 37 new quotes
- add Packager:

* Mon Apr 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070430-alt1
- 55 new quotes

* Sat Apr 21 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070421-alt1
- lots of new quotes
- generate dat file at build time

* Sat May 14 2005 Mike A. Plugnikov <amike@altlinux.ru> 20050514-alt1
- Add many new fortunes
- Description changed
- Database filename changed to ALT-irc

* Wed Aug 04 2004 Mike A. Plugnikov <amike@altlinux.ru> 20040804-alt1
- Add 2 fortunes

* Tue Jul 20 2004 Mike A. Plugnikov <amike@altlinux.ru> 20040720-alt1
- First release

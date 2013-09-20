# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename he
%define packagversion 2.5.0
%define packagedate 201309192013
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hebrew
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-he
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.5
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.5
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Provides: %moodle_name-%packagetype-%packagename = %version-%release
Provides: %moodle_name-%packagetype-%oldpackagename = %version-%release
Conflicts: %moodle_name-%packagetype-%packagename < %version
Conflicts: %moodle_name-%packagetype-%oldpackagename < %version

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

%files
%moodle_langdir/*

%changelog
* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309192013-alt1
- repocop cronbuild 20130920. At your service.
- he.zip build 2013-09-19 20:13 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309131237-alt1
- repocop cronbuild 20130913. At your service.
- he.zip build 2013-09-13 12:37 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309061024-alt1
- repocop cronbuild 20130906. At your service.
- he.zip build 2013-09-06 10:24 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308302329-alt1
- repocop cronbuild 20130831. At your service.
- he.zip build 2013-08-30 23:29 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308221251-alt1
- repocop cronbuild 20130824. At your service.
- he.zip build 2013-08-22 12:51 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308152201-alt1
- repocop cronbuild 20130817. At your service.
- he.zip build 2013-08-15 22:01 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308091135-alt1
- repocop cronbuild 20130810. At your service.
- he.zip build 2013-08-09 11:35 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307301805-alt1
- repocop cronbuild 20130803. At your service.
- he.zip build 2013-07-30 18:05 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307270158-alt1
- repocop cronbuild 20130727. At your service.
- he.zip build 2013-07-27 01:58 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307191336-alt1
- repocop cronbuild 20130720. At your service.
- he.zip build 2013-07-19 13:36 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121421-alt1
- repocop cronbuild 20130713. At your service.
- he.zip build 2013-07-12 14:21 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307050717-alt1
- repocop cronbuild 20130706. At your service.
- he.zip build 2013-07-05 07:17 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306261503-alt1
- repocop cronbuild 20130629. At your service.
- he.zip build 2013-06-26 15:03 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306190605-alt1
- repocop cronbuild 20130622. At your service.
- he.zip build 2013-06-19 06:05 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306141652-alt1
- repocop cronbuild 20130615. At your service.
- he.zip build 2013-06-14 16:52 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306072048-alt1
- repocop cronbuild 20130608. At your service.
- he.zip build 2013-06-07 20:48 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-he
- he.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221731-alt1
- repocop cronbuild 20130524. At your service.
- he.zip build 2013-05-22 17:31 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305151639-alt1
- repocop cronbuild 20130517. At your service.
- he.zip build 2013-05-15 16:39 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305082151-alt1
- repocop cronbuild 20130509. At your service.
- he.zip build 2013-05-08 21:51 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304161834-alt1
- Rename package to moodle2.4-lang-he
- he.zip build 2013-04-16 18:34 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304161834-alt1
- repocop cronbuild 20130417. At your service.
- he.zip build 2013-04-16 18:34 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304091434-alt1
- repocop cronbuild 20130410. At your service.
- he.zip build 2013-04-09 14:34 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303310944-alt1
- repocop cronbuild 20130403. At your service.
- he.zip build 2013-03-31 09:44 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303261728-alt1
- repocop cronbuild 20130327. At your service.
- he.zip build 2013-03-26 17:28 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303181403-alt1
- repocop cronbuild 20130320. At your service.
- he.zip build 2013-03-18 14:03 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303091000-alt1
- repocop cronbuild 20130313. At your service.
- he.zip build 2013-03-09 10:00 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302271941-alt1
- repocop cronbuild 20130304. At your service.
- he.zip build 2013-02-27 19:41 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302242006-alt1
- repocop cronbuild 20130225. At your service.
- he.zip build 2013-02-24 20:06 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302161236-alt1
- repocop cronbuild 20130218. At your service.
- he.zip build 2013-02-16 12:36 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302100909-alt1
- repocop cronbuild 20130211. At your service.
- he.zip build 2013-02-10 09:09 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302032155-alt1
- repocop cronbuild 20130204. At your service.
- he.zip build 2013-02-03 21:55 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301271212-alt1
- repocop cronbuild 20130128. At your service.
- he.zip build 2013-01-27 12:12 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301150745-alt1
- repocop cronbuild 20130121. At your service.
- he.zip build 2013-01-15 07:45 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301131923-alt1
- repocop cronbuild 20130114. At your service.
- he.zip build 2013-01-13 19:23 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301052242-alt1
- repocop cronbuild 20130107. At your service.
- he.zip build 2013-01-05 22:42 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212302114-alt1
- repocop cronbuild 20121231. At your service.
- he.zip build 2012-12-30 21:14 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212231956-alt1
- repocop cronbuild 20121224. At your service.
- he.zip build 2012-12-23 19:56 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212160757-alt1
- repocop cronbuild 20121217. At your service.
- he.zip build 2012-12-16 07:57 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212092217-alt1
- repocop cronbuild 20121210. At your service.
- he.zip build 2012-12-09 22:17 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211281120-alt1
- repocop cronbuild 20121203. At your service.
- he.zip build 2012-11-28 11:20 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211251416-alt1
- repocop cronbuild 20121126. At your service.
- he.zip build 2012-11-25 14:16 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211152351-alt1
- repocop cronbuild 20121119. At your service.
- he.zip build 2012-11-15 23:51 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211071628-alt1
- repocop cronbuild 20121112. At your service.
- he.zip build 2012-11-07 16:28 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211041626-alt1
- repocop cronbuild 20121105. At your service.
- he.zip build 2012-11-04 16:26 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210282116-alt1
- repocop cronbuild 20121029. At your service.
- he.zip build 2012-10-28 21:16 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210201959-alt1
- repocop cronbuild 20121022. At your service.
- he.zip build 2012-10-20 19:59 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210142202-alt1
- repocop cronbuild 20121015. At your service.
- he.zip build 2012-10-14 22:02 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210071916-alt1
- repocop cronbuild 20121008. At your service.
- he.zip build 2012-10-07 19:16 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209301959-alt1
- repocop cronbuild 20121001. At your service.
- he.zip build 2012-09-30 19:59 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209141008-alt1
- repocop cronbuild 20120918. At your service.
- he.zip build 2012-09-14 10:08 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209091236-alt1
- repocop cronbuild 20120911. At your service.
- he.zip build 2012-09-09 12:36 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209021231-alt1
- repocop cronbuild 20120904. At your service.
- he.zip build 2012-09-02 12:31 UTC

* Tue Aug 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208151023-alt1
- repocop cronbuild 20120821. At your service.
- he.zip build 2012-08-15 10:23 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208071733-alt1
- repocop cronbuild 20120807. At your service.
- he.zip build 2012-08-07 17:33 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207241404-alt1
- repocop cronbuild 20120724. At your service.
- he.zip build 2012-07-24 14:04 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207170952-alt1
- repocop cronbuild 20120717. At your service.
- he.zip build 2012-07-17 09:52 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207101258-alt1
- repocop cronbuild 20120710. At your service.
- he.zip build 2012-07-10 12:58 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207030834-alt1
- repocop cronbuild 20120703. At your service.
- he.zip build 2012-07-03 08:34 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206211345-alt1
- repocop cronbuild 20120626. At your service.
- he.zip build 2012-06-21 13:45 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206180928-alt1
- repocop cronbuild 20120619. At your service.
- he.zip build 2012-06-18 09:28 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205291333-alt1
- repocop cronbuild 20120529. At your service.
- he.zip build 2012-05-29 13:33 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205150820-alt1
- repocop cronbuild 20120521. At your service.
- he.zip build 2012-05-15 08:20 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- he.zip build 2012-05-11 11:00 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204301327-alt1
- repocop cronbuild 20120501. At your service.
- he.zip build 2012-04-30 13:27 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204151134-alt1
- repocop cronbuild 20120417. At your service.
- he.zip build 2012-04-15 11:34 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204021157-alt1
- repocop cronbuild 20120403. At your service.
- he.zip build 2012-04-02 11:57 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203221535-alt1
- repocop cronbuild 20120327. At your service.
- he.zip build 2012-03-22 15:35 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203191429-alt1
- repocop cronbuild 20120320. At your service.
- he.zip build 2012-03-19 14:29 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203181546-alt1
- Rename package to moodle2.2-lang-he
- he.zip build 2012-03-18 15:46 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203060922-alt1
- repocop cronbuild 20120306. At your service.
- he.zip build 2012-03-06 09:22 UTC

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202161217-alt1
- repocop cronbuild 20120221. At your service.
- he.zip build 2012-02-16 12:17 UTC

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202141443-alt1
- repocop cronbuild 20120214. At your service.
- he.zip build 2012-02-14 14:43 UTC

* Tue Feb 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202061439-alt1
- repocop cronbuild 20120207. At your service.
- he.zip build 2012-02-06 14:39 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201261241-alt1
- repocop cronbuild 20120131. At your service.
- he.zip build 2012-01-26 12:41 UTC

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201191327-alt1
- repocop cronbuild 20120124. At your service.
- he.zip build 2012-01-19 13:27 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201171128-alt1
- repocop cronbuild 20120117. At your service.
- he.zip build 2012-01-17 11:28 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112190920-alt1
- repocop cronbuild 20111220. At your service.
- he.zip build 2011-12-19 09:20 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111213. At your service.
- he.zip build 2011-12-09 16:00 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112061435-alt1
- repocop cronbuild 20111206. At your service.
- he.zip build 2011-12-06 14:35 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111241405-alt1
- Rename package to moodle2.1-lang-he
- he.zip build 2011-11-24 14:05

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111201348-alt2
- Fix requires

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111201348-alt1
- repocop cronbuild 20111120. At your service.
- he.zip build 2011-11-20 13:48 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111101425-alt1
- repocop cronbuild 20111116. At your service.
- he.zip build 2011-11-10 14:25 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- he.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- he.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-he
- he.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110804-alt1
- he_utf8.zip build 2011-08-04
- initial build for ALT Linux Sisyphus

# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ru
%define packagversion 2.2.0
%define packagedate 201603170047
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Russian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-ru
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.2
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.2
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
* Fri Mar 18 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201603170047-alt1
- repocop cronbuild 20160318. At your service.
- ru.zip build 2016-03-17 00:47 UTC

* Tue Feb 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201602231429-alt1
- repocop cronbuild 20160223. At your service.
- ru.zip build 2016-02-23 14:29 UTC

* Mon Feb 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201602081246-alt1
- repocop cronbuild 20160208. At your service.
- ru.zip build 2016-02-08 12:46 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201601141459-alt1
- repocop cronbuild 20160124. At your service.
- ru.zip build 2016-01-14 14:59 UTC

* Wed Dec 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201512080511-alt1
- repocop cronbuild 20151209. At your service.
- ru.zip build 2015-12-08 05:11 UTC

* Sun Dec 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201512051417-alt1
- repocop cronbuild 20151206. At your service.
- ru.zip build 2015-12-05 14:17 UTC

* Thu Nov 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511241116-alt1
- repocop cronbuild 20151126. At your service.
- ru.zip build 2015-11-24 11:16 UTC

* Sun Nov 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511210841-alt1
- repocop cronbuild 20151122. At your service.
- ru.zip build 2015-11-21 08:41 UTC

* Sat Nov 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511201417-alt1
- repocop cronbuild 20151121. At your service.
- ru.zip build 2015-11-20 14:17 UTC

* Thu Nov 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511192139-alt1
- repocop cronbuild 20151119. At your service.
- ru.zip build 2015-11-19 21:39 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511091309-alt1
- repocop cronbuild 20151109. At your service.
- ru.zip build 2015-11-09 13:09 UTC

* Sat Nov 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511061157-alt1
- repocop cronbuild 20151107. At your service.
- ru.zip build 2015-11-06 11:57 UTC

* Wed Nov 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511042215-alt1
- repocop cronbuild 20151104. At your service.
- ru.zip build 2015-11-04 22:15 UTC

* Tue Nov 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511021344-alt1
- repocop cronbuild 20151103. At your service.
- ru.zip build 2015-11-02 13:44 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511011603-alt1
- repocop cronbuild 20151102. At your service.
- ru.zip build 2015-11-01 16:03 UTC

* Sun Nov 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510312156-alt1
- repocop cronbuild 20151101. At your service.
- ru.zip build 2015-10-31 21:56 UTC

* Sat Oct 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510301311-alt1
- repocop cronbuild 20151031. At your service.
- ru.zip build 2015-10-30 13:11 UTC

* Thu Oct 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510291505-alt1
- repocop cronbuild 20151029. At your service.
- ru.zip build 2015-10-29 15:05 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510261446-alt1
- repocop cronbuild 20151026. At your service.
- ru.zip build 2015-10-26 14:46 UTC

* Fri Oct 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510231329-alt1
- repocop cronbuild 20151023. At your service.
- ru.zip build 2015-10-23 13:29 UTC

* Thu Sep 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201509231952-alt1
- repocop cronbuild 20150924. At your service.
- ru.zip build 2015-09-23 19:52 UTC

* Sat Sep 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201509110654-alt1
- repocop cronbuild 20150912. At your service.
- ru.zip build 2015-09-11 06:54 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201508011759-alt1
- repocop cronbuild 20150823. At your service.
- ru.zip build 2015-08-01 17:59 UTC

* Tue Jul 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201507270937-alt1
- repocop cronbuild 20150728. At your service.
- ru.zip build 2015-07-27 09:37 UTC

* Sat Jul 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201507231017-alt1
- repocop cronbuild 20150725. At your service.
- ru.zip build 2015-07-23 10:17 UTC

* Mon Jul 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201507191243-alt1
- repocop cronbuild 20150720. At your service.
- ru.zip build 2015-07-19 12:43 UTC

* Wed Jul 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201506301318-alt1
- repocop cronbuild 20150701. At your service.
- ru.zip build 2015-06-30 13:18 UTC

* Wed Jun 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201506232020-alt1
- repocop cronbuild 20150624. At your service.
- ru.zip build 2015-06-23 20:20 UTC

* Wed Jun 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201506091856-alt1
- repocop cronbuild 20150610. At your service.
- ru.zip build 2015-06-09 18:56 UTC

* Mon May 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201505241448-alt1
- repocop cronbuild 20150525. At your service.
- ru.zip build 2015-05-24 14:48 UTC

* Sun May 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201505232006-alt1
- repocop cronbuild 20150524. At your service.
- ru.zip build 2015-05-23 20:06 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201505220841-alt1
- repocop cronbuild 20150522. At your service.
- ru.zip build 2015-05-22 08:41 UTC

* Tue May 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201505111343-alt1
- repocop cronbuild 20150512. At your service.
- ru.zip build 2015-05-11 13:43 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504090917-alt1
- repocop cronbuild 20150410. At your service.
- ru.zip build 2015-04-09 09:17 UTC

* Wed Apr 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504071354-alt1
- repocop cronbuild 20150408. At your service.
- ru.zip build 2015-04-07 13:54 UTC

* Sun Apr 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504041736-alt1
- repocop cronbuild 20150405. At your service.
- ru.zip build 2015-04-04 17:36 UTC

* Mon Mar 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503291014-alt1
- repocop cronbuild 20150330. At your service.
- ru.zip build 2015-03-29 10:14 UTC

* Thu Mar 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503041551-alt1
- repocop cronbuild 20150305. At your service.
- ru.zip build 2015-03-04 15:51 UTC

* Mon Mar 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503010624-alt1
- repocop cronbuild 20150302. At your service.
- ru.zip build 2015-03-01 06:24 UTC

* Tue Feb 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502091443-alt1
- repocop cronbuild 20150210. At your service.
- ru.zip build 2015-02-09 14:43 UTC

* Mon Feb 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502081730-alt1
- repocop cronbuild 20150209. At your service.
- ru.zip build 2015-02-08 17:30 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502061342-alt1
- repocop cronbuild 20150207. At your service.
- ru.zip build 2015-02-06 13:42 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501291737-alt1
- repocop cronbuild 20150130. At your service.
- ru.zip build 2015-01-29 17:37 UTC

* Thu Jan 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501281724-alt1
- repocop cronbuild 20150129. At your service.
- ru.zip build 2015-01-28 17:24 UTC

* Sat Jan 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501230916-alt1
- repocop cronbuild 20150124. At your service.
- ru.zip build 2015-01-23 09:16 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501221631-alt1
- repocop cronbuild 20150123. At your service.
- ru.zip build 2015-01-22 16:31 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501151713-alt1
- repocop cronbuild 20150116. At your service.
- ru.zip build 2015-01-15 17:13 UTC

* Mon Jan 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501110841-alt1
- repocop cronbuild 20150112. At your service.
- ru.zip build 2015-01-11 08:41 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501081709-alt1
- repocop cronbuild 20150109. At your service.
- ru.zip build 2015-01-08 17:09 UTC

* Mon Jan 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501052041-alt1
- repocop cronbuild 20150105. At your service.
- ru.zip build 2015-01-05 20:41 UTC

* Mon Jan 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501041817-alt1
- repocop cronbuild 20150105. At your service.
- ru.zip build 2015-01-04 18:17 UTC

* Sun Jan 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501031934-alt1
- repocop cronbuild 20150104. At your service.
- ru.zip build 2015-01-03 19:34 UTC

* Sat Jan 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501022146-alt1
- repocop cronbuild 20150103. At your service.
- ru.zip build 2015-01-02 21:46 UTC

* Tue Dec 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412301006-alt1
- repocop cronbuild 20141230. At your service.
- ru.zip build 2014-12-30 10:06 UTC

* Wed Dec 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412241301-alt1
- repocop cronbuild 20141224. At your service.
- ru.zip build 2014-12-24 13:01 UTC

* Wed Dec 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412172035-alt1
- repocop cronbuild 20141217. At your service.
- ru.zip build 2014-12-17 20:35 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412101230-alt1
- repocop cronbuild 20141211. At your service.
- ru.zip build 2014-12-10 12:30 UTC

* Tue Dec 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412090925-alt1
- repocop cronbuild 20141209. At your service.
- ru.zip build 2014-12-09 09:25 UTC

* Tue Dec 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412011830-alt1
- repocop cronbuild 20141202. At your service.
- ru.zip build 2014-12-01 18:30 UTC

* Sun Nov 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411230957-alt1
- repocop cronbuild 20141123. At your service.
- ru.zip build 2014-11-23 09:57 UTC

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411201117-alt1
- repocop cronbuild 20141121. At your service.
- ru.zip build 2014-11-20 11:17 UTC

* Mon Nov 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411032017-alt1
- repocop cronbuild 20141103. At your service.
- ru.zip build 2014-11-03 20:17 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410300826-alt1
- repocop cronbuild 20141031. At your service.
- ru.zip build 2014-10-30 08:26 UTC

* Mon Oct 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410271324-alt1
- repocop cronbuild 20141027. At your service.
- ru.zip build 2014-10-27 13:24 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410230829-alt1
- repocop cronbuild 20141024. At your service.
- ru.zip build 2014-10-23 08:29 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410170952-alt1
- repocop cronbuild 20141018. At your service.
- ru.zip build 2014-10-17 09:52 UTC

* Wed Oct 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410140948-alt1
- repocop cronbuild 20141015. At your service.
- ru.zip build 2014-10-14 09:48 UTC

* Mon Oct 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410051904-alt1
- repocop cronbuild 20141006. At your service.
- ru.zip build 2014-10-05 19:04 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410041938-alt1
- repocop cronbuild 20141004. At your service.
- ru.zip build 2014-10-04 19:38 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410031935-alt1
- repocop cronbuild 20141004. At your service.
- ru.zip build 2014-10-03 19:35 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409261754-alt1
- repocop cronbuild 20140927. At your service.
- ru.zip build 2014-09-26 17:54 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409252012-alt1
- repocop cronbuild 20140926. At your service.
- ru.zip build 2014-09-25 20:12 UTC

* Mon Sep 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409221727-alt1
- repocop cronbuild 20140922. At your service.
- ru.zip build 2014-09-22 17:27 UTC

* Sun Sep 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409211017-alt1
- repocop cronbuild 20140921. At your service.
- ru.zip build 2014-09-21 10:17 UTC

* Sat Sep 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409191146-alt1
- repocop cronbuild 20140920. At your service.
- ru.zip build 2014-09-19 11:46 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201408291544-alt1
- repocop cronbuild 20140913. At your service.
- ru.zip build 2014-08-29 15:44 UTC

* Mon Jul 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201407061939-alt1
- repocop cronbuild 20140707. At your service.
- ru.zip build 2014-07-06 19:39 UTC

* Thu Jul 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201407032055-alt1
- repocop cronbuild 20140703. At your service.
- ru.zip build 2014-07-03 20:55 UTC

* Wed May 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405271752-alt1
- repocop cronbuild 20140528. At your service.
- ru.zip build 2014-05-27 17:52 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405151028-alt1
- repocop cronbuild 20140516. At your service.
- ru.zip build 2014-05-15 10:28 UTC

* Sun May 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405040514-alt1
- repocop cronbuild 20140504. At your service.
- ru.zip build 2014-05-04 05:14 UTC

* Wed Apr 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201404160632-alt1
- repocop cronbuild 20140416. At your service.
- ru.zip build 2014-04-16 06:32 UTC

* Wed Mar 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403052121-alt1
- repocop cronbuild 20140305. At your service.
- ru.zip build 2014-03-05 21:21 UTC

* Sun Mar 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403011507-alt1
- repocop cronbuild 20140302. At your service.
- ru.zip build 2014-03-01 15:07 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402152054-alt1
- repocop cronbuild 20140215. At your service.
- ru.zip build 2014-02-15 20:54 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402140911-alt1
- repocop cronbuild 20140214. At your service.
- ru.zip build 2014-02-14 09:11 UTC

* Wed Feb 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402110947-alt1
- repocop cronbuild 20140212. At your service.
- ru.zip build 2014-02-11 09:47 UTC

* Tue Feb 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402102008-alt1
- repocop cronbuild 20140211. At your service.
- ru.zip build 2014-02-10 20:08 UTC

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401252027-alt1
- repocop cronbuild 20140125. At your service.
- ru.zip build 2014-01-25 20:27 UTC

* Sun Jan 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401112203-alt1
- repocop cronbuild 20140112. At your service.
- ru.zip build 2014-01-11 22:03 UTC

* Fri Jan 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401091113-alt1
- repocop cronbuild 20140110. At your service.
- ru.zip build 2014-01-09 11:13 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312122034-alt1
- repocop cronbuild 20131213. At your service.
- ru.zip build 2013-12-12 20:34 UTC

* Wed Dec 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312111548-alt1
- repocop cronbuild 20131211. At your service.
- ru.zip build 2013-12-11 15:48 UTC

* Mon Dec 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312021635-alt1
- repocop cronbuild 20131202. At your service.
- ru.zip build 2013-12-02 16:35 UTC

* Tue Nov 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311251442-alt1
- repocop cronbuild 20131126. At your service.
- ru.zip build 2013-11-25 14:42 UTC

* Wed Nov 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311201714-alt1
- repocop cronbuild 20131120. At your service.
- ru.zip build 2013-11-20 17:14 UTC

* Mon Nov 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311181826-alt1
- repocop cronbuild 20131118. At your service.
- ru.zip build 2013-11-18 18:26 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311141433-alt1
- repocop cronbuild 20131115. At your service.
- ru.zip build 2013-11-14 14:33 UTC

* Mon Nov 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311111927-alt1
- repocop cronbuild 20131111. At your service.
- ru.zip build 2013-11-11 19:27 UTC

* Sat Nov 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311090853-alt1
- repocop cronbuild 20131109. At your service.
- ru.zip build 2013-11-09 08:53 UTC

* Tue Nov 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311050410-alt1
- repocop cronbuild 20131105. At your service.
- ru.zip build 2013-11-05 04:10 UTC

* Mon Nov 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311041827-alt1
- repocop cronbuild 20131104. At your service.
- ru.zip build 2013-11-04 18:27 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310312025-alt1
- repocop cronbuild 20131101. At your service.
- ru.zip build 2013-10-31 20:25 UTC

* Wed Oct 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310301947-alt1
- repocop cronbuild 20131030. At your service.
- ru.zip build 2013-10-30 19:47 UTC

* Wed Oct 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310291734-alt1
- repocop cronbuild 20131030. At your service.
- ru.zip build 2013-10-29 17:34 UTC

* Sun Oct 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310271837-alt1
- repocop cronbuild 20131027. At your service.
- ru.zip build 2013-10-27 18:37 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310250659-alt1
- repocop cronbuild 20131025. At your service.
- ru.zip build 2013-10-25 06:59 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310241345-alt1
- repocop cronbuild 20131025. At your service.
- ru.zip build 2013-10-24 13:45 UTC

* Wed Oct 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310231846-alt1
- repocop cronbuild 20131023. At your service.
- ru.zip build 2013-10-23 18:46 UTC

* Wed Oct 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310091137-alt1
- repocop cronbuild 20131009. At your service.
- ru.zip build 2013-10-09 11:37 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310031608-alt1
- repocop cronbuild 20131004. At your service.
- ru.zip build 2013-10-03 16:08 UTC

* Sat Sep 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309131258-alt1
- repocop cronbuild 20130914. At your service.
- ru.zip build 2013-09-13 12:58 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309121403-alt1
- repocop cronbuild 20130913. At your service.
- ru.zip build 2013-09-12 14:03 UTC

* Sat Sep 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309061838-alt1
- repocop cronbuild 20130907. At your service.
- ru.zip build 2013-09-06 18:38 UTC

* Mon Sep 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309011838-alt1
- repocop cronbuild 20130902. At your service.
- ru.zip build 2013-09-01 18:38 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308301154-alt1
- repocop cronbuild 20130830. At your service.
- ru.zip build 2013-08-30 11:54 UTC

* Wed Aug 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308272043-alt1
- repocop cronbuild 20130828. At your service.
- ru.zip build 2013-08-27 20:43 UTC

* Tue Aug 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308261912-alt1
- repocop cronbuild 20130827. At your service.
- ru.zip build 2013-08-26 19:12 UTC

* Mon Aug 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308191345-alt1
- repocop cronbuild 20130819. At your service.
- ru.zip build 2013-08-19 13:45 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308161426-alt1
- repocop cronbuild 20130817. At your service.
- ru.zip build 2013-08-16 14:26 UTC

* Thu Aug 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308141907-alt1
- repocop cronbuild 20130815. At your service.
- ru.zip build 2013-08-14 19:07 UTC

* Wed Aug 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308132049-alt1
- repocop cronbuild 20130814. At your service.
- ru.zip build 2013-08-13 20:49 UTC

* Tue Aug 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308130859-alt1
- repocop cronbuild 20130813. At your service.
- ru.zip build 2013-08-13 08:59 UTC

* Mon Aug 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308112049-alt1
- repocop cronbuild 20130812. At your service.
- ru.zip build 2013-08-11 20:49 UTC

* Sun Aug 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308102123-alt1
- repocop cronbuild 20130811. At your service.
- ru.zip build 2013-08-10 21:23 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308092317-alt1
- repocop cronbuild 20130810. At your service.
- ru.zip build 2013-08-09 23:17 UTC

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308090958-alt1
- repocop cronbuild 20130809. At your service.
- ru.zip build 2013-08-09 09:58 UTC

* Thu Aug 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308071225-alt1
- repocop cronbuild 20130808. At your service.
- ru.zip build 2013-08-07 12:25 UTC

* Wed Aug 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308062207-alt1
- repocop cronbuild 20130807. At your service.
- ru.zip build 2013-08-06 22:07 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308021032-alt1
- repocop cronbuild 20130803. At your service.
- ru.zip build 2013-08-02 10:32 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308012302-alt1
- repocop cronbuild 20130802. At your service.
- ru.zip build 2013-08-01 23:02 UTC

* Thu Aug 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307312238-alt1
- repocop cronbuild 20130801. At your service.
- ru.zip build 2013-07-31 22:38 UTC

* Wed Jul 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307302146-alt1
- repocop cronbuild 20130731. At your service.
- ru.zip build 2013-07-30 21:46 UTC

* Tue Jul 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307292303-alt1
- repocop cronbuild 20130730. At your service.
- ru.zip build 2013-07-29 23:03 UTC

* Mon Jul 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307282130-alt1
- repocop cronbuild 20130729. At your service.
- ru.zip build 2013-07-28 21:30 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307262134-alt1
- repocop cronbuild 20130727. At your service.
- ru.zip build 2013-07-26 21:34 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307251552-alt1
- repocop cronbuild 20130726. At your service.
- ru.zip build 2013-07-25 15:52 UTC

* Thu Jul 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307241941-alt1
- repocop cronbuild 20130725. At your service.
- ru.zip build 2013-07-24 19:41 UTC

* Wed Jul 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307232007-alt1
- repocop cronbuild 20130724. At your service.
- ru.zip build 2013-07-23 20:07 UTC

* Tue Jul 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307222115-alt1
- repocop cronbuild 20130723. At your service.
- ru.zip build 2013-07-22 21:15 UTC

* Mon Jul 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307211919-alt1
- repocop cronbuild 20130722. At your service.
- ru.zip build 2013-07-21 19:19 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307181100-alt1
- repocop cronbuild 20130719. At your service.
- ru.zip build 2013-07-18 11:00 UTC

* Thu Jul 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307172149-alt1
- repocop cronbuild 20130718. At your service.
- ru.zip build 2013-07-17 21:49 UTC

* Mon Jul 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307142048-alt1
- repocop cronbuild 20130715. At your service.
- ru.zip build 2013-07-14 20:48 UTC

* Sun Jul 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307132052-alt1
- repocop cronbuild 20130714. At your service.
- ru.zip build 2013-07-13 20:52 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307121937-alt1
- repocop cronbuild 20130713. At your service.
- ru.zip build 2013-07-12 19:37 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307111407-alt1
- repocop cronbuild 20130712. At your service.
- ru.zip build 2013-07-11 14:07 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307051948-alt1
- repocop cronbuild 20130706. At your service.
- ru.zip build 2013-07-05 19:48 UTC

* Thu Jun 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306261912-alt1
- repocop cronbuild 20130627. At your service.
- ru.zip build 2013-06-26 19:12 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306201352-alt1
- repocop cronbuild 20130621. At your service.
- ru.zip build 2013-06-20 13:52 UTC

* Tue May 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305270449-alt1
- repocop cronbuild 20130528. At your service.
- ru.zip build 2013-05-27 04:49 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305231845-alt1
- repocop cronbuild 20130524. At your service.
- ru.zip build 2013-05-23 18:45 UTC

* Thu May 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305211305-alt1
- repocop cronbuild 20130523. At your service.
- ru.zip build 2013-05-21 13:05 UTC

* Tue May 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305200524-alt1
- repocop cronbuild 20130521. At your service.
- ru.zip build 2013-05-20 05:24 UTC

* Sun May 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305180813-alt1
- repocop cronbuild 20130519. At your service.
- ru.zip build 2013-05-18 08:13 UTC

* Sat May 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305171943-alt1
- repocop cronbuild 20130518. At your service.
- ru.zip build 2013-05-17 19:43 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304291248-alt1
- repocop cronbuild 20130509. At your service.
- ru.zip build 2013-04-29 12:48 UTC

* Sun Apr 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304141933-alt1
- repocop cronbuild 20130414. At your service.
- ru.zip build 2013-04-14 19:33 UTC

* Sat Apr 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304062144-alt1
- repocop cronbuild 20130406. At your service.
- ru.zip build 2013-04-06 21:44 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304031528-alt1
- repocop cronbuild 20130403. At your service.
- ru.zip build 2013-04-03 15:28 UTC

* Sun Mar 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303172106-alt1
- repocop cronbuild 20130317. At your service.
- ru.zip build 2013-03-17 21:06 UTC

* Wed Mar 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303051413-alt1
- repocop cronbuild 20130306. At your service.
- ru.zip build 2013-03-05 14:13 UTC

* Sat Feb 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302151550-alt1
- repocop cronbuild 20130216. At your service.
- ru.zip build 2013-02-15 15:50 UTC

* Wed Feb 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302131042-alt1
- repocop cronbuild 20130213. At your service.
- ru.zip build 2013-02-13 10:42 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302101429-alt1
- repocop cronbuild 20130211. At your service.
- ru.zip build 2013-02-10 14:29 UTC

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301280958-alt1
- repocop cronbuild 20130129. At your service.
- ru.zip build 2013-01-28 09:58 UTC

* Sat Jan 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261559-alt1
- repocop cronbuild 20130126. At your service.
- ru.zip build 2013-01-26 15:59 UTC

* Tue Jan 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301212155-alt1
- repocop cronbuild 20130122. At your service.
- ru.zip build 2013-01-21 21:55 UTC

* Sat Jan 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301121811-alt1
- repocop cronbuild 20130112. At your service.
- ru.zip build 2013-01-12 18:11 UTC

* Fri Jan 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301112114-alt1
- repocop cronbuild 20130111. At your service.
- ru.zip build 2013-01-11 21:14 UTC

* Sat Jan 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301051948-alt1
- repocop cronbuild 20130105. At your service.
- ru.zip build 2013-01-05 19:48 UTC

* Sat Dec 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212221221-alt1
- repocop cronbuild 20121222. At your service.
- ru.zip build 2012-12-22 12:21 UTC

* Wed Dec 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212191047-alt1
- repocop cronbuild 20121219. At your service.
- ru.zip build 2012-12-19 10:47 UTC

* Tue Dec 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212180737-alt1
- repocop cronbuild 20121218. At your service.
- ru.zip build 2012-12-18 07:37 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212171532-alt1
- repocop cronbuild 20121217. At your service.
- ru.zip build 2012-12-17 15:32 UTC

* Wed Dec 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212051812-alt1
- repocop cronbuild 20121205. At your service.
- ru.zip build 2012-12-05 18:12 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211032111-alt1
- repocop cronbuild 20121105. At your service.
- ru.zip build 2012-11-03 21:11 UTC

* Thu Nov 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121101. At your service.
- ru.zip build 2012-11-01 07:00 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210011159-alt1
- repocop cronbuild 20121001. At your service.
- ru.zip build 2012-10-01 11:59 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209251230-alt1
- repocop cronbuild 20121001. At your service.
- ru.zip build 2012-09-25 12:30 UTC

* Wed Sep 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209121028-alt1
- repocop cronbuild 20120912. At your service.
- ru.zip build 2012-09-12 10:28 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209111534-alt1
- repocop cronbuild 20120911. At your service.
- ru.zip build 2012-09-11 15:34 UTC

* Thu Sep 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209061451-alt1
- repocop cronbuild 20120906. At your service.
- ru.zip build 2012-09-06 14:51 UTC

* Fri Aug 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120831. At your service.
- ru.zip build 2012-08-31 10:30 UTC

* Fri Aug 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208240740-alt1
- repocop cronbuild 20120824. At your service.
- ru.zip build 2012-08-24 07:40 UTC

* Thu Aug 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208161816-alt1
- repocop cronbuild 20120816. At your service.
- ru.zip build 2012-08-16 18:16 UTC

* Sat Aug 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208040909-alt1
- repocop cronbuild 20120804. At your service.
- ru.zip build 2012-08-04 09:09 UTC

* Fri Aug 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208031851-alt1
- repocop cronbuild 20120803. At your service.
- ru.zip build 2012-08-03 18:51 UTC

* Thu Aug 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208022032-alt1
- repocop cronbuild 20120802. At your service.
- ru.zip build 2012-08-02 20:32 UTC

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208012126-alt1
- repocop cronbuild 20120801. At your service.
- ru.zip build 2012-08-01 21:26 UTC

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207310756-alt1
- repocop cronbuild 20120801. At your service.
- ru.zip build 2012-07-31 07:56 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207302008-alt1
- repocop cronbuild 20120731. At your service.
- ru.zip build 2012-07-30 20:08 UTC

* Fri Jul 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207200826-alt1
- repocop cronbuild 20120720. At your service.
- ru.zip build 2012-07-20 08:26 UTC

* Thu Jul 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207191933-alt1
- repocop cronbuild 20120719. At your service.
- ru.zip build 2012-07-19 19:33 UTC

* Wed Jul 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207180728-alt1
- repocop cronbuild 20120718. At your service.
- ru.zip build 2012-07-18 07:28 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207151954-alt1
- repocop cronbuild 20120717. At your service.
- ru.zip build 2012-07-15 19:54 UTC

* Sun Jul 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207151738-alt1
- repocop cronbuild 20120715. At your service.
- ru.zip build 2012-07-15 17:38 UTC

* Fri Jul 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207131300-alt1
- repocop cronbuild 20120713. At your service.
- ru.zip build 2012-07-13 13:00 UTC

* Thu Jul 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207120506-alt1
- repocop cronbuild 20120712. At your service.
- ru.zip build 2012-07-12 05:06 UTC

* Thu Jun 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206140650-alt1
- repocop cronbuild 20120614. At your service.
- ru.zip build 2012-06-14 06:50 UTC

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206130918-alt1
- repocop cronbuild 20120613. At your service.
- ru.zip build 2012-06-13 09:18 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206041827-alt1
- repocop cronbuild 20120605. At your service.
- ru.zip build 2012-06-04 18:27 UTC

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120523. At your service.
- ru.zip build 2012-05-23 15:49 UTC

* Fri May 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120511. At your service.
- ru.zip build 2012-05-11 11:00 UTC

* Fri May 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205041517-alt1
- repocop cronbuild 20120504. At your service.
- ru.zip build 2012-05-04 15:17 UTC

* Wed May 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205021803-alt1
- repocop cronbuild 20120502. At your service.
- ru.zip build 2012-05-02 18:03 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204300527-alt1
- repocop cronbuild 20120501. At your service.
- ru.zip build 2012-04-30 05:27 UTC

* Fri Apr 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204130803-alt1
- repocop cronbuild 20120413. At your service.
- ru.zip build 2012-04-13 08:03 UTC

* Thu Apr 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204122046-alt1
- repocop cronbuild 20120412. At your service.
- ru.zip build 2012-04-12 20:46 UTC

* Sun Apr 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204031003-alt1
- repocop cronbuild 20120408. At your service.
- ru.zip build 2012-04-03 10:03 UTC

* Wed Mar 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203280830-alt1
- repocop cronbuild 20120328. At your service.
- ru.zip build 2012-03-28 08:30 UTC

* Fri Mar 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203232037-alt1
- repocop cronbuild 20120323. At your service.
- ru.zip build 2012-03-23 20:37 UTC

* Thu Mar 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203221320-alt1
- repocop cronbuild 20120322. At your service.
- ru.zip build 2012-03-22 13:20 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203200753-alt1
- repocop cronbuild 20120320. At your service.
- ru.zip build 2012-03-20 07:53 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203051832-alt1
- Rename package to moodle2.2-lang-ru
- ru.zip build 2012-03-05 18:32 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203051138-alt1
- repocop cronbuild 20120306. At your service.
- ru.zip build 2012-03-05 11:38 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120301. At your service.
- ru.zip build 2012-03-01 11:00 UTC

* Sun Feb 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202260940-alt1
- repocop cronbuild 20120226. At your service.
- ru.zip build 2012-02-26 09:40 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202010703-alt1
- repocop cronbuild 20120201. At your service.
- ru.zip build 2012-02-01 07:03 UTC

* Sat Jan 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201280352-alt1
- repocop cronbuild 20120128. At your service.
- ru.zip build 2012-01-28 03:52 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201251829-alt1
- repocop cronbuild 20120125. At your service.
- ru.zip build 2012-01-25 18:29 UTC

* Sat Jan 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201211904-alt1
- repocop cronbuild 20120121. At your service.
- ru.zip build 2012-01-21 19:04 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201051751-alt1
- repocop cronbuild 20120105. At your service.
- ru.zip build 2012-01-05 17:51 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112221011-alt1
- repocop cronbuild 20111222. At your service.
- ru.zip build 2011-12-22 10:11 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112211944-alt1
- repocop cronbuild 20111221. At your service.
- ru.zip build 2011-12-21 19:44 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112151437-alt1
- repocop cronbuild 20111215. At your service.
- ru.zip build 2011-12-15 14:37 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112141935-alt1
- repocop cronbuild 20111214. At your service.
- ru.zip build 2011-12-14 19:35 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112131517-alt1
- repocop cronbuild 20111213. At your service.
- ru.zip build 2011-12-13 15:17 UTC

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112100727-alt1
- repocop cronbuild 20111210. At your service.
- ru.zip build 2011-12-10 07:27 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- ru.zip build 2011-12-09 16:00 UTC

* Sun Nov 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111271657-alt1
- repocop cronbuild 20111127. At your service.
- ru.zip build 2011-11-27 16:57 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111251919-alt1
- repocop cronbuild 20111125. At your service.
- ru.zip build 2011-11-25 19:19 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111061046-alt1
- Rename package to moodle2.1-lang-ru
- ru.zip build 2011-11-06 10:46 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111061026-alt1
- repocop cronbuild 20111116. At your service.
- ru.zip build 2011-11-06 10:26 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021436-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021436-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111021436-alt1
- repocop cronbuild 20111105. At your service.
- ru.zip build 2011-11-02 14:36 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201902-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201902-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201902-alt1
- ru.zip build 2011-10-20 19:02 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110050641-alt1
- ru.zip build 2011-10-05 06:41 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109272015-alt1
- ru.zip build 2011-09-27 20:15 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109270433-alt1
- ru.zip build 2011-09-27 04:33 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231446-alt1
- ru.zip build 2011-09-23 14:46 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221040-alt1
- ru.zip build 2011-09-22 10:40 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- ru.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109190938-alt1
- ru.zip build 2011-09-19 09:38 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109190636-alt1
- ru.zip build 2011-09-19 06:36 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109160755-alt1
- ru.zip build 2011-09-16 07:55 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141836-alt1
- ru.zip build 2011-09-14 18:36 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131719-alt1
- ru.zip build 2011-09-13 17:19 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109110824-alt1
- ru.zip build 2011-09-11 08:24 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109071935-alt1
- ru.zip build 2011-09-07 19:35 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241750-alt1
- ru.zip build 2011-08-24 17:50 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191453-alt1
- ru.zip build 2011-08-19 14:53 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-ru
- ru.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt1
- ru_utf8.zip build 2010-06-17

* Tue Nov 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt2.cvs20100617
- inheritance fixed

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100617
- new version

* Tue Oct 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt2.cvs20091014
- rebuild with new Moodle

* Mon Oct 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20091014
- new build from cvs

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20090720
- new build from cvs

* Sat Apr 18 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.4-alt1.cvs20090416
- new build from cvs

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081106
- new build from cvs

* Mon Oct 13 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080926
- new build from cvs

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080802
- add build requires on rpm-build-webserver-common
- new build from cvs

* Thu Jun 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt2.cvs20080526
- change path moodle location

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080526
- new build for ALT Linux

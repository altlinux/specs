Group: System/Libraries
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global         githash     1ca80982c5a32c82bfc5e98e1fe9d8751ab44946
%global         shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global         gitdate     Wed, 17 Feb 2021 00:09:15 +0900
%global         gitdate_num 20210217

%global         githash_tools     0fe2106fbc052445c611e6c5b2a79899d740edcb

%undefine        _changelog_trimtime

Summary:	Dictionaries for SKK (Simple Kana-Kanji conversion program)
Name:		skkdic
Version:	%{gitdate_num}
Release:	alt1_3.git1ca80982c5
# See Source2
License:	GPLv2+ and CC-BY-SA and Unicode and Public Domain and MIT

Source0:	https://github.com/skk-dev/dict/archive/%{githash}/%{name}-%{gitdate_num}.git%{githash}.tar.gz
Source1:	https://raw.githubusercontent.com/skk-dev/skktools/%{githash_tools}/unannotation.awk
Source2:	license-investigation.txt
Source200:	README-skkdic.rh.ja

URL:		https://skk-dev.github.io/dict/
BuildArch:	noarch
Source44: import.info


%description
This package includes the SKK dictionaries, including the large dictionary
SKK-JISYO.L and pubdic+ dictionary.

%prep
%setup -q -c -T -a 0
ln -sf dict-%{githash} src
mkdir tools

cp -p %SOURCE200 .
cp -p %SOURCE1 tools

pushd src
cp -a zipcode/README.md zipcode/README-zipcode.md
popd

%build
pushd src

for dic in \
	SKK-JISYO.L.unannotated \
	SKK-JISYO.wrong
do
	rm -f $dic
	make $dic
done

popd

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/skk

pushd src
for f in SKK-JISYO* zipcode/SKK-JISYO*
do
	install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/skk
done
gzip -9 ChangeLog

popd

%files
%doc	src/ChangeLog.gz
%doc	README-skkdic.rh.ja
%doc	src/committers.md
%doc	src/edict_doc.html
%doc	src/zipcode/README-zipcode.md

%{_datadir}/skk/

%changelog
* Wed Feb 09 2022 Igor Vlasenko <viy@altlinux.org> 20210217-alt1_3.git1ca80982c5
- update to new release by fcimport

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 20181016-alt1_2.T1609
- update to new release by fcimport

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 20170102-alt1_3.T1100
- NMU (for oddity@): new version by fcimport

* Tue Sep 09 2014 Ilya Mashkin <oddity@altlinux.ru> 20131114-alt1.T1121
- build for Sisyphus

* Thu Nov 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 20131114-7.T1121
- Update to the latest data

* Fri Jan  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 20130104-4.T1435
- Update to the latest data

* Sun Oct 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 20111016-1.T0540
- Update for F16

* Wed Mar 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 20110309-1.T1520
- Update dictionaries

* Tue Sep 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 20090929-1.T0800
- Update for F12Beta

* Wed Aug  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 20090805-1.T0306
- Update for F12Alpha
- A bit clean up for spec file

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20080904-1
- fix license tag
- update source files

* Tue Sep 23 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20050614-2
- mass rebuilding

* Tue Jun 14 2005 Jens Petersen <petersen@redhat.com> - 20050614-1
- initial import to Fedora Extras
- update to latest dictionaries

* Wed Sep 22 2004 Jens Petersen <petersen@redhat.com> - 20040922-1
- update to latest dictionaries
- update url
- gzip ChangeLog since it is growing fast

* Thu Apr 15 2004 Jens Petersen <petersen@redhat.com> - 20040415-1
- update to latest
- update README-skkdic.rh.ja and convert it to utf-8

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 11 2003 Jens Petersen <petersen@redhat.com> - 20030211-1
- update dictionaries
- move rh readme file into cvs
- don't build unannotated dictionaries

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 20020724-2
- rebuild

* Wed Jul 24 2002 Jens Petersen <petersen@redhat.com> 20020724-1
- update dictionaries

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Jens Petersen <petersen@redhat.com> 20020220-2
- rebuild in new environment

* Tue Feb 20 2002 Jens Petersen <petersen@redhat.com> 20020220-1
- update to latest dictionaries
- put source in one bzip2ed tar file
- tidy spec file
- make unannotated
- include SKK-JISYO.pubdic+

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jun 23 2001 SATO Satoru <ssato@redhat.com>
- update and add more dictionaries: (jinmei,) law, okinawa, geo
- add README files

* Mon Jan 22 2001 SATO Satoru <ssato@redhat.com>
- update dictionaris
- add cdb-dictionaries
- clean up SPEC

* Mon Dec 28 2000 SATO Satoru <ssato@redhat.com>
- add many extra dictionaries
- clean up SPEC

* Tue Sep  5 2000 SATO Satoru <ssato@redhat.com>
- Initial release

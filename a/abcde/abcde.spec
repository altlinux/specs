Group: Sound
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/SHA.pm) perl(WebService/MusicBrainz/Artist.pm) perl(WebService/MusicBrainz/Release.pm) perl(WebService/MusicBrainz/Response/Track.pm) perl(WebService/MusicBrainz/Response/TrackList.pm) perl(encoding.pm)
# END SourceDeps(oneline)
Name:           abcde
Version:        2.5.4
Release:        alt1_5
Summary:        A Better CD Encoder

# Public domain after 2010-01-01, see comments in abcde and cddb-tool
License:        Public Domain
URL:            http://code.google.com/p/abcde/
Source0:        http://abcde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         %{name}-2.4.0-config.patch
# http://code.google.com/p/abcde/source/detail?r=379
# http://code.google.com/p/abcde/issues/detail?id=99
Patch1:         %{name}-2.5.4-eyed3_07-991163.patch
# http://code.google.com/p/abcde/issues/detail?id=107
Patch2:         %{name}-2.5.4-eyed3-empty-year.patch

BuildArch:      noarch
Requires:       cd-discid
Requires:       cdparanoia
Requires:       flac
Requires:       icedax
Requires:       vorbis-tools
Requires:       wget
Requires:       which
Conflicts:      python-module-eyeD3 < 0.7.0
Source44: import.info
AutoReq: yes,noshell

%description
abcde is a front end command line utility (actually, a shell script)
that grabs audio tracks off a CD, encodes them to various formats, and
tags them, all in one go.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
mv examples/cue2discid .


%build


%install
make install DESTDIR=$RPM_BUILD_ROOT
install -pm 755 cue2discid $RPM_BUILD_ROOT%{_bindir}
rm $RPM_BUILD_ROOT%{_bindir}/abcde-musicbrainz-tool # optional, some deps N/A


%files
%doc COPYING FAQ KNOWN.BUGS README TODO USEPIPES changelog examples/
%doc abcde-musicbrainz-tool
%config(noreplace) %{_sysconfdir}/abcde.conf
%{_bindir}/abcde
%{_bindir}/cddb-tool
%{_bindir}/cue2discid
%{_mandir}/man1/abcde.1*
%{_mandir}/man1/cddb-tool.1*


%changelog
* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_5
- update to new release by fcimport

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_4
- converted for ALT Linux by srpmconvert tools

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_2
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_1
- update to new release by fcimport

* Thu May 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_1
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_4
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.2-alt1_3.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_3
- initial release by fcimport


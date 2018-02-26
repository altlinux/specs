Group: Sound
Name:           abcde
Version:        2.5.2
Release:        alt1_1
Summary:        A Better CD Encoder

# Public domain after 2010-01-01, see comments in abcde and cddb-tool
License:        Public Domain
URL:            http://code.google.com/p/abcde/
Source0:        http://abcde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         %{name}-2.4.0-config.patch

BuildArch:      noarch
Requires:       cd-discid
Requires:       cdparanoia
Requires:       flac
Requires:       icedax
Requires:       vorbis-tools
Requires:       wget
Requires:       which
Source44: import.info
AutoReq: yes,noshell

%description
abcde is a front end command line utility (actually, a shell script)
that grabs audio tracks off a CD, encodes them to various formats, and
tags them, all in one go.


%prep
%setup -q
%patch0 -p1
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


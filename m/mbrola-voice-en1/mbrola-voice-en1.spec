%define voice en1
Summary: %{voice} - A British English male voice for the MBROLA synthesizer
Name: mbrola-voice-%{voice}
Version: 980910
Release: alt3
License: no-charge distributable for non-commercial, non-military use
Group: Sound
URL: http://tcts.fpms.ac.be/synthesis/mbrola.html
Source0: %{voice}-%{version}.zip
Packager: Igor Vlasenko <viy@altlinux.org>
BuildArch: noarch
AutoReqProv: none
Provides: mbrola-voice

# Automatically added by buildreq on Thu Oct 26 2006 (-bi)
BuildRequires: unzip

%description
%{voice} - A British English diphone male voice for the MBROLA synthesizer.

It  provides a British English male voice (known as "Roger's
voice")  to  be used with the MBROLA program.  It  has  been
built  from  the original Roger diphones made  available  by
CSTR, University of Edinburgh, as part of their generic text-
to-speech system FESTIVAL.

%prep
%setup -q -n %{voice}

%build

%install

VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices/english/%{voice}_mbrola/%{voice}

install -d $VOICE_DIR/
install -m 644 %{voice} $VOICE_DIR/

install -d $RPM_BUILD_ROOT%{_datadir}/mbrola
ln -s %{_datadir}/festival/voices/english/%{voice}_mbrola/%{voice} $RPM_BUILD_ROOT%{_datadir}/mbrola/%{voice}

%files
%doc TEST %{voice}.txt
%doc %{voice}mrpa
%dir %{_datadir}/festival/voices/english/%{voice}_mbrola/%{voice}
%{_datadir}/festival/voices/english/%{voice}_mbrola/%{voice}/%{voice}
%{_datadir}/mbrola/%{voice}

%changelog
* Fri Sep 05 2008 Igor Vlasenko <viy@altlinux.ru> 980910-alt3
- added Provides: mbrola-voice

* Thu Oct 26 2006 Igor Vlasenko <viy@altlinux.ru> 980910-alt2
 - fixed voice locations for festival support

* Tue Oct 24 2006 Igor Vlasenko <viy@altlinux.ru> 980910-alt1
 - first build for Sisyphus


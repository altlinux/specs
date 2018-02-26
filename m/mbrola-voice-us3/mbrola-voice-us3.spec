%define voice us3
Summary: %{voice} - An American English male voice for the MBROLA synthesizer
Name: mbrola-voice-%{voice}
Version: 990208
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
%{voice} - An American English diphone male voice for the MBROLA synthesizer.

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
%doc TEST %{voice}.txt license.txt
%dir %{_datadir}/festival/voices/english/%{voice}_mbrola/%{voice}
%{_datadir}/festival/voices/english/%{voice}_mbrola/%{voice}/%{voice}
%{_datadir}/mbrola/%{voice}

%changelog
* Fri Sep 05 2008 Igor Vlasenko <viy@altlinux.ru> 990208-alt3
- added Provides: mbrola-voice

* Thu Oct 26 2006 Igor Vlasenko <viy@altlinux.ru> 990208-alt2
 - fixed voice locations for festival support

* Tue Oct 24 2006 Igor Vlasenko <viy@altlinux.ru> 990208-alt1
 - first build for Sisyphus


# BEGIN SourceDeps(oneline):
BuildRequires: texinfo
# END SourceDeps(oneline)
Name:          festival-freebsoft-utils
Version:       0.10
Release:       alt3_10
Summary:       A collection of utilities that enhance Festival with some useful features

Group:         Sound
BuildArch:     noarch
License:       GPLv2+
URL:           http://www.freebsoft.org/festival-freebsoft-utils
Source0:       http://devel.freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

BuildRequires: festival

Requires: festival
Requires: libsox-fmt-alsa libsox-fmt-ao libsox-fmt-caf libsox-fmt-fap libsox-fmt-flac libsox-fmt-mat4 libsox-fmt-mat5 libsox-fmt-opus libsox-fmt-oss libsox-fmt-paf libsox-fmt-pulseaudio libsox-fmt-pvf libsox-fmt-sd2 libsox-fmt-sndfile libsox-fmt-vorbis libsox-fmt-w64 libsox-fmt-wavpack libsox-fmt-xi libsox3 sox-base
Source44: import.info

%description
A collection of utilities that enhance Festival with some useful features. They 
provide all that is needed for interaction with Speech Dispatcher.

Key festival-freebsoft-utils features are:
- Generalized concept of input events. festival-freebsoft-utils allows not only 
  plain text synthesis, but also combining it with sounds. Additionally, 
  mechanism of logical events mapped to other events is provided. 
- Substitution of events for given words. 
- High-level voice selection mechanism and setting of basic prosodic parameters. 
- Spelling mode. 
- Capital letter signalization. 
- Punctuation modes, for explicit reading or not reading punctuation characters. 
- Incremental synthesis of texts and events. 
- Speech Dispatcher support. 
- Rudimentary SSML support. 
- Enhance the Festival extension language with functions commonly used in Lisp.
- Support for wrapping already defined Festival functions by your own code.
- Everything is written in the extension language, no patching of the Festival 
  C++ sources is needed.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/festival/
cp -p *.scm %{buildroot}/%{_datadir}/festival/

%files
%doc COPYING NEWS README
%{_datadir}/festival/*.scm

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_6
- update to new release by fcimport

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_3
- update to new release by fcimport

* Sun May 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_2
- fixed festival_lib path

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- initial release by fcimport


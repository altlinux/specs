Name:          festival-freebsoft-utils
Version:       0.10
Release:       alt3_3
Summary:       A collection of utilities that enhance Festival with some useful features

Group:         Sound
BuildArch:     noarch
License:       GPLv2+
URL:           http://www.freebsoft.org/festival-freebsoft-utils
Source0:       http://www.freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

BuildRequires: festival

Requires: festival
Requires: sox
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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_3
- update to new release by fcimport

* Sun May 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_2
- fixed festival_lib path

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- initial release by fcimport


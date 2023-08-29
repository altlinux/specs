Group: Communications
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           aldo
Version:        0.7.7
Release:        alt1_12
Summary:        A morse tutor

License:        GPL-2.0-or-later AND GPL-3.0
URL:            http://aldo.nongnu.org/

Source0:        http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libao-devel
Source44: import.info

%description
Aldo is a morse code learning tool released under GPL, which provides
four type of training methods:

   1. Classic exercise : Identify random characters played in morse code.
   2. Koch method : Two morse characters will be played at full speed
      (20wpm) until you'll be able to identify at least 90 percent of
      them. After that, one more character will be added, and so on.
   3. Read from file : Identify the morse code generated from a file.
   4. Callsign exercise : Identify random callsigns played in morse code.


%prep
%setup -q



%build
%configure
%make_build


%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog README THANKS
%doc --no-dereference COPYING
%{_bindir}/*
%{_mandir}/man?/*


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.7.7-alt1_12
- update to new release by fcimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.7-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_5
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_4
- initial release by fcimport


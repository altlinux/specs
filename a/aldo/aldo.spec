# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           aldo
Version:        0.7.6
Release:        alt1_6
Summary:        A morse tutor

Group:          Communications
License:        GPLv2+
URL:            http://aldo.nongnu.org/
Source0:        http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2

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
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog COPYING README THANKS
%{_bindir}/*
%{_mandir}/man?/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_5
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_4
- initial release by fcimport


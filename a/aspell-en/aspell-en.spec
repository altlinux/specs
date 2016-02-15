%define lang en
%define langrelease 0
%define aspellversion 6
Summary: English dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 2015.04.24
Release: alt1_2
License: MIT and BSD
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60
Obsoletes: aspell-en-gb <= 0.33.7.1
Obsoletes: aspell-en-ca <= 0.33.7.1

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: English, Canadian
English, British English

%prep
%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2015.04.24-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 2015.04.24-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_4
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 7.1-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_2
- update and rebuild with proper aspell datadir

* Fri Feb 02 2007 Igor Vlasenko <viy@altlinux.ru> 0.60-alt3
- new version 6.0

* Tue Jun 29 2004 Vital Khilko <vk@altlinux.ru> 0.60-alt2
- rebuilded dictionaries 

* Tue May 18 2004 Vital Khilko <vk@altlinux.ru> 0.60-alt1
- new version

* Fri Apr 23 2004 Vital Khilko <vk@altlinux.ru> 0.50-alt4
- fixed #3957

* Mon Oct 20 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt3
- fix depedencies

* Fri Sep 19 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt2
- Fixed obsoletes

* Tue Sep 16 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt1
- New official package from aspell.net

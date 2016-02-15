%define lang nl
%define langrelease 2
Summary: Dutch dictionaries for Aspell
Name: aspell-%{lang}
# Have to bump this to make it newer than the old, bad version.
#Epoch: 51
Version: 0.50
Release: alt1_7
License: GPLv2+
Group: Text tools
URL: http://aspell.net/
Source0: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil} 
Source44: import.info

%description
Provides the word list/dictionaries for the following: Dutch

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}

%build
./configure prefix=/usr
make

%install
make install DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir}

%files
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_2
- update to new release by fcimport

* Sun Jul 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_1
- new release

* Sun Feb 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt2_10
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt2_9
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt1_9
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


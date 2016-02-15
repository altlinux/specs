Serial: 1
%define lang fo
%define langrelease 1
%define aspellversion 5
Summary: Faeroese dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 51
Version: 0.2.16
Release: alt2_19
License: GPLv2
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Faeroese

%prep
%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
make install  DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_18
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_13
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_12
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt2_11
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.2.16-alt1_11
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


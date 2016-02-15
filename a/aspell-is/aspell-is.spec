%define lang is
%define langrelease 0
%define aspellrelease 0.60
Summary: Icelandic dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 0.51.1
Release: alt2_16
License: GPLv2+
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= %{aspellrelease}
Requires: aspell >= %{aspellrelease}

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Icelandic

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
iconv -f windows-1252 -t utf8 Copyright >Copyright.aux
mv Copyright.aux Copyright

%build
./configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/%{_libdir}/aspell/*slenska.alias $RPM_BUILD_ROOT/%{_libdir}/aspell/íslenska.alias

%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_15
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_10
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_9
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_8
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt1_8
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


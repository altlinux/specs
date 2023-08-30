Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lang nl
%define langrelease 2
Summary: Dutch dictionaries for Aspell
Name: aspell-%{lang}
# Have to bump this to make it newer than the old, bad version.
#Epoch: 51
Version: 0.50
Release: alt1_23
License: GPL-2.0-or-later
URL: http://aspell.net/
Source0: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2

# IMPORTANT
# This package has been deprecated since Fedora 39
# The reason behind this is that upstream has been inactive for more than 4 years
# and there are other variants like hunspell or enchant which has active upstream
# FESCo approval is located here: https://pagure.io/fesco/issue/3009
# Change proposal is located here: https://fedoraproject.org/wiki/Changes/AspellDeprecation
Provides:  deprecated()

Buildrequires: aspell libaspell
Requires: aspell libaspell

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
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.50-alt1_23
- update to new release by fcimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_12
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_11
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_8
- update to new release by fcimport

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


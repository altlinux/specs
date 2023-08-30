Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define aspellversion 6
%define lang sk
%define langrelease 1
%define aspellname aspell%{aspellversion}-%{lang}

Name:           aspell-%{lang}
Version:        2.4.7
Release:        alt1_2
Summary:        Slovak dictionaries for Aspell

License:        GPLv2 or LGPLv2 or MPLv1.1
URL:            http://sk-spell.sk.cx/aspell-sk
Source0:        http://www.sk-spell.sk.cx/files/%{aspellname}-%{version}-%{langrelease}.tar.bz2

# IMPORTANT
# This package has been deprecated since Fedora 39
# The reason behind this is that upstream has been inactive for more than 4 years
# and there are other variants like hunspell or enchant which has active upstream
# FESCo approval is located here: https://pagure.io/fesco/issue/3009
# Change proposal is located here: https://fedoraproject.org/wiki/Changes/AspellDeprecation
Provides:  deprecated()

BuildRequires:  aspell libaspell
Requires:       aspell libaspell

%define debug_package %{nil}                                                    
Source44: import.info

%description
Provides the word list/dictionaries for the following: Slovak


%prep
%setup -q -n %{aspellname}-%{version}-%{langrelease}


%build
sh configure
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT



%files
%doc doc/* Copyright README
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 2.4.7-alt1_2
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_6
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1_4
- update and rebuild with proper aspell datadir

* Tue Jul 29 2008 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_4
- build for Sisyphus


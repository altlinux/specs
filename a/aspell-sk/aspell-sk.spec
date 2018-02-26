# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
%define aspellversion 6
%define lang sk
%define langrelease 2
%define aspellname aspell%{aspellversion}-%{lang}

Name:           aspell-%{lang}
Version:        2.01
Release:        alt2_5
Summary:        Slovak dictionaries for Aspell

Group:          Text tools
License:        GPLv2 or LGPLv2 or MPLv1.1
URL:            http://sk-spell.sk.cx/aspell-sk
Source0:        http://www.sk-spell.sk.cx/files/%{aspellname}-%{version}-%{langrelease}.tar.bz2

BuildRequires:  aspell >= 0.60
Requires:       aspell >= 0.60

%define debug_package %{nil}                                                    
Source44: import.info

%description
Provides the word list/dictionaries for the following: Slovak


%prep
%setup -q -n %{aspellname}-%{version}-%{langrelease}


%build
sh configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc doc/* Copyright README
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1_4
- update and rebuild with proper aspell datadir

* Tue Jul 29 2008 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_4
- build for Sisyphus


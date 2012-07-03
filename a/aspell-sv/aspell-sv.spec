# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
%define lang sv
%define langrelease 0
Summary: Swedish dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 0.51
Release: alt2_7
# file sv_phonet.dat is under GPLv2+ the other parts of this package are under LGPLv2+
License: LGPLv2+ and GPLv2+ 
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Swedish

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}

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
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.51-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.51-alt2_6
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1_6
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


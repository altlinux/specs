# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
%define lang pt_BR
%define langrelease 0
Summary: Brazilian Portuguese dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 20090702
Release: alt2_2
License: LGPLv2+
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60
Obsoletes: aspell-pt <= 50:0.50
Provides: aspell-pt = %{version}

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Brazilian Portuguese

%prep
%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 20090702-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20090702-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20090702-alt1_1
- update and rebuild with proper aspell datadir


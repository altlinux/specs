# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
%define lang sr
%define langrelease 0
Summary: Serbian dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 0.02
Release: alt2_8
License: LGPLv2
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}.tar.bz2
Patch0: aspell6-sr-0.02-time.patch
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Serbian

%prep
%setup -q -n aspell6-%{lang}-%{version}
%patch0 -p1 -b .time

%build
./configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_8
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
%define lang nb
%define langrelease 0
Summary: Norwegian dictionaries for Aspell
Name: aspell-no
#Epoch: 50
Version: 0.50.1
Release: alt3_17
License: GPLv2
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Patch: aspell-nb-0.50.1-0.utf-filename.patch
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Norwegian

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
%patch -p1 -b .utf-filename
cp bokmal.alias bokmål.alias

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
* Sun Feb 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_17
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_16
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt2_16
- update and rebuild with proper aspell datadir

* Wed Apr 30 2008 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt2
- fixed rebuild

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


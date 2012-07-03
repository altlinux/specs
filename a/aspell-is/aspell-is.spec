%define lang is
%define langrelease 0
%define aspellrelease 0.60
Summary: Icelandic dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 0.51.1
Release: alt2_9
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
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_9
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt2_8
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt1_8
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.51.1-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


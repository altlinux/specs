# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
Summary: Dutch dictionaries for Aspell
Name: aspell-nl
# Have to bump this to make it newer than the old, bad version.
#Epoch: 51
Version: 0.1e
Release: alt2_10
License: GPLv2+
Group: Text tools
URL: http://packages.debian.org/unstable/text/%{name}
Source0: http://ftp.debian.org/debian/pool/main/d/dutch/dutch_%{version}.orig.tar.gz
Patch0: dutch-debian.patch
Patch2: dutch-0.1e-nl.patch
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil} 
Source44: import.info

%description
Provides the word list/dictionaries for the following: Dutch

%prep
%setup -q -n dutch-%{version}
%patch0 -p1
%patch2 -p1 -b .nl
cp ./aspell/dutch.dat ./aspell/nl_affix.dat

%build
./configure prefix=/usr 
make

%install
make install DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir}
rm $RPM_BUILD_ROOT/usr/share/ispell/dutch.aff
rm $RPM_BUILD_ROOT/usr/dict/dutch
rm $RPM_BUILD_ROOT/usr/info/*
cp $RPM_BUILD_ROOT%{_libdir}/aspell/nl.dat $RPM_BUILD_ROOT%{_libdir}/aspell/nl_affix.dat

mkdir -p %buildroot%{_datadir}/aspell/
mv %buildroot%{_libdir}/aspell/*.dat %buildroot%{_datadir}/aspell/

%files
%doc COPYING README ChangeLog
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Sun Feb 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt2_10
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt2_9
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt1_9
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.1e-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import


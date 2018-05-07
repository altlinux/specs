Group: Emulators
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/col /usr/bin/groff /usr/bin/valgrind bzlib-devel gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           advancecomp
Version:        2.1
Release:        alt1_4
Summary:        Recompression utilities for .PNG, .MNG and .ZIP files
License:        GPLv3
URL:            http://www.advancemame.it/
Source0:        https://github.com/amadvance/advancecomp/releases/download/v%{version}/advancecomp-%{version}.tar.gz
BuildRequires:  tofrodos
BuildRequires:  zlib-devel
Source44: import.info

%description
AdvanceCOMP is a set of recompression utilities for .PNG, .MNG and .ZIP files.
The main features are :
* Recompress ZIP, PNG and MNG files using the Deflate 7-Zip implementation.
* Recompress MNG files using Delta and Move optimization.

This package contains:
* advzip - Recompression and test utility for zip files
* advpng - Recompression utility for png files
* advmng - Recompression utility for mng files
* advdef - Recompression utility for deflate streams in .png, .mng and .gz 
files

%prep
%setup -q

%build
%configure
%make_build

%install
make install DESTDIR=%{buildroot}

%files
%doc --no-dereference COPYING
%doc AUTHORS HISTORY README
%doc doc/adv*.txt
%doc doc/authors.txt
%doc doc/history.txt
%doc doc/readme.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_4
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_1
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_1
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_18
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_17
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_16
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_14
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_13
- initial release by fcimport


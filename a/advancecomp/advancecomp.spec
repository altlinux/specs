# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/col /usr/bin/groff /usr/bin/gzip bzlib-devel gcc-c++
# END SourceDeps(oneline)
Summary: Recompression utilities for .PNG, .MNG and .ZIP files
Name: advancecomp
Version: 1.15
Release: alt2_16
License: GPLv2+
Group: Emulators
URL: http://advancemame.sourceforge.net/
Source: http://downloads.sf.net/advancemame/advancecomp-%{version}.tar.gz
BuildRequires: zlib-devel
Source44: import.info

%description
AdvanceCOMP is a set of recompression utilities for .PNG, .MNG and .ZIP files.
The main features are :
* Recompress ZIP, PNG and MNG files using the Deflate 7-Zip implementation.
* Recompress MNG files using Delta and Move optimization.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS COPYING HISTORY README
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_16
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_14
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_13
- initial release by fcimport


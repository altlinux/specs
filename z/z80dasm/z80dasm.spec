# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		z80dasm
Version:	1.1.3
Release:	alt1_6
Summary:	Z80 Disassembler
Group:		Development/Other
License:	GPLv2+
URL:		http://www.tablix.org/~avian/blog/articles/%{name}/
Source0:	http://www.tablix.org/~avian/%{name}/%{name}-%{version}.tar.gz

# Target addresses are 16 bits, but relative address computations were not
# being masked to 16 bits, causing bad results on all systems and buffer
# overruns in sprintf on 64-bit systems.  Reported to upstream via email
# on 27-Feb-2012.
Patch0:		z80dasm-1.1.3-16-bit-addr.patch

BuildRequires:	z80asm
Source44: import.info

%description
z80dasm is a disassembler for the Zilog Z80 microprocessor and
compatibles. It can be used to reverse engineer programs and operating
systems for 1980's microcomputers using this processor architecture
(for example ZX81, Spectrum, Galaksija and many others).  Generated
assembly code can be assembled back with a number of Z80
assemblers. Compatibility with z80asm was thoroughly tested.

%prep
%setup -q
%patch -P 0 -p1 -b .16-bit-addr
%configure

%build
%make_build CFLAGS="%{optflags}"

%check
make test

%install
make install DESTDIR="%{buildroot}"

%files
%doc COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_6
- update to new version by fcimport

* Fri Mar 20 2015 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt2
- build for Sisyphus

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_6
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_5
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_3
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_2
- update to new release by fcimport

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_1
- converted for Sisyphus


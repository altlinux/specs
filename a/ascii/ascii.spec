Name:           ascii
Version:        3.8
Release:        alt2_3
URL:            http://www.catb.org/~esr/ascii/
Source0:        http://www.catb.org/~esr/ascii/ascii-3.8.tar.gz
Patch1:         ascii-3.8-makefile.patch

License:        GPLv2
Group:          Text tools
Summary:        Interactive ascii name and synonym chart
Source44: import.info

%description
The ascii utility provides easy conversion between various byte representations
and the American Standard Code for Information Interchange (ASCII) character
table.  It knows about a wide variety of hex, binary, octal, Teletype mnemonic,
ISO/ECMA code point, slang names, XML entity names, and other representations.
Given any one on the command line, it will try to display all others.  Called
with no arguments it displays a handy small ASCII chart.

%prep
%setup -q
%patch1 -p1

%build
make %{?_smp_mflags} ascii ascii.1 CFLAGS="${RPM_OPT_FLAGS}"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp ascii $RPM_BUILD_ROOT%{_bindir}
cp ascii.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii
%doc README COPYING

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.8-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_2
- initial release by fcimport


Group: Development/Tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           atasm
Version:        1.08
Release:        alt1_6
Summary:        6502 cross-assembler

License:        GPLv2+
URL:            http://atari.miribilist.com/atasm/
# fedora-getsvn atasm https://svn.code.sf.net/p/atasm/code/trunk 100
# svn rev 100 == version 1.08
Source0:        atasm-svn100.tar.bz2

BuildRequires:  gcc
BuildRequires:  zlib-devel
Source44: import.info


%description
ATasm is a 6502 command-line cross-assembler that is compatible with the
original Mac/65 macroassembler released by OSS software.  Code
development can now be performed using "modern" editors and compiles
with lightning speed.


%prep
%setup -q -n %{name}


%build
pushd src
%make_build CFLAGS="$RPM_OPT_FLAGS -DZLIB_CAPABLE -DUNIX"
sed -e 's|%%DOCDIR%%|%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}|g' %{name}.1.in > %{name}.1
popd


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

pushd src
install -p -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
popd


%check
pushd tests
make test
popd


%files
%doc LICENSE VERSION.TXT atasm.blurb atasm.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_6
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_10
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_8
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_7
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt1_2
- initial release by fcimport


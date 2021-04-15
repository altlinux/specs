Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           atasm
Version:        1.09
%global verstr  %(echo %{version} | sed -e 's/\\.//')
Release:        alt1_1
Summary:        6502 cross-assembler

License:        GPLv2+
URL:            https://atari.miribilist.com/atasm/
Source0:        https://atari.miribilist.com/atasm/%{name}%{verstr}.zip

BuildRequires:  gcc
BuildRequires:  zlib-devel
Source44: import.info


%description
ATasm is a 6502 command-line cross-assembler that is compatible with the
original Mac/65 macro-assembler released by OSS software.  Code
development can now be performed using "modern" editors and compiles
with lightning speed.


%prep
%setup -q -n %{name}%{verstr}


%build
pushd src
%make_build CFLAGS="%{optflags} -DZLIB_CAPABLE -DUNIX" L="%{build_ldflags} -lz"
sed -e 's|\%\%DOCDIR\%\%|%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}|g' %{name}.1.in > %{name}.1
popd


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

pushd src
install -p -m 755 %{name} %{buildroot}%{_bindir}
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1
popd


%check
pushd tests
make test
popd


%files
%doc --no-dereference LICENSE
%doc VERSION.TXT README.md docs/atasm.blurb docs/atasm.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 1.09-alt1_1
- update to new release by fcimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 1.08-alt1_8
- update to new release by fcimport

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


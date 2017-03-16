# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        AES-based encryption tool for tar/cpio and loop-aes images
Name:           aespipe
Version:        2.4d
Release:        alt1_4
License:        GPLv2+
Group:          System/Base
URL:            http://loop-aes.sourceforge.net/
Source:         http://loop-aes.sourceforge.net/aespipe/aespipe-v%{version}.tar.bz2
BuildRequires:  gnupg
Requires:       gnupg

%description
aespipe is an encryption tool that reads from standard input and
writes to standard output. It uses the AES (Rijndael) cipher.

It can be used as an encryption filter, to create and restore
encrypted tar/cpio backup archives and to read/write and convert
loop-AES compatible encrypted images.

aespipe can be used for non-destructive in-place encryption of
existing disk partitions for use with the loop-AES encrypted loop-back
kernel module.

%prep
%setup -q -n %{name}-v%{version}

%build
# Package calls CC to link
%configure LDFLAGS="${CFLAGS}"

%global make_target %{nil}
%ifarch x86_64
%global make_target amd64
%endif
%ifarch %{ix86}
%global make_target x86
%endif
%make_build %{make_target}

%check
make tests

%install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples
cp -p ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}
install -Dp -m0644 bz2aespipe %{buildroot}%{_defaultdocdir}/%{name}/examples
install -Dp -m0644 aespipe.1 %{buildroot}%{_mandir}/man1/aespipe.1
install -Dp -m0755 aespipe %{buildroot}%{_bindir}/aespipe


%files
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_mandir}/man1/*
%{_bindir}/aespipe

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.4d-alt1_4
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4d-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4d-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_2
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_1
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt1_0
- initial release by fcimport


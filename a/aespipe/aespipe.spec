# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/md5sum
# END SourceDeps(oneline)
Summary:        AES-based encryption tool for tar/cpio and loop-aes images
Name:           aespipe
Version:        2.4c
Release:        alt2_1
License:        GPLv2+
Group:          File tools
URL:            http://loop-aes.sourceforge.net/
Source:         http://loop-aes.sourceforge.net/aespipe/aespipe-v%{version}.tar.bz2
BuildRequires:  gpg
Requires:       gpg
Source44: import.info

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
%configure

%global make_target %{nil}
%ifarch x86_64
%global make_target amd64
%endif
%ifarch %{ix86}
%global make_target x86
%endif
%{__make} %{?_smp_mflags} %{make_target}

%check
%{__make} tests

%install
%{__mkdir} -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}/examples
%{__cp} -p ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}-%{version}
%{__install} -Dp -m0644 bz2aespipe %{buildroot}%{_defaultdocdir}/%{name}-%{version}/examples
%{__install} -Dp -m0644 aespipe.1 %{buildroot}%{_mandir}/man1/aespipe.1
%{__install} -Dp -m0755 aespipe %{buildroot}%{_bindir}/aespipe

%files
%dir %{_defaultdocdir}/%{name}-%{version}
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/man1/*
%{_bindir}/aespipe

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt2_1
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.4c-alt1_0
- initial release by fcimport


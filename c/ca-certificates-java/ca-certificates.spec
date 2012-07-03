Name: ca-certificates-java
Version: 0.01
Release: alt1

Summary: Common CA Certificates in java caserts format
License: MPL/GPL/LGPL
Group: System/Base
BuildArch: noarch

Source0: cacerts

%description
This package contains a bundle of X.509 certificates of public Certificate
Authorities (CA) chosen by the Mozilla Foundation for use with the Internet PKI
in java caserts format.

%prep
cp %{S:0} .

%build

%install
install -pDm644 cacerts %buildroot%{_sysconfdir}/pki/java/cacerts

%files
%{_sysconfdir}/pki/java

%changelog
* Thu Sep 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- temporary hack til the bug 25027 will be fixed

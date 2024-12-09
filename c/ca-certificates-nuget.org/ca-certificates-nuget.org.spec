%define pkidir %_datadir/pki/ca-trust-source/anchors

Name: ca-certificates-nuget.org
Version: 0.2
Release: alt1

Summary: DigiCert CA Root for nuget.org

License: Distributable
Group: Other
URL: https://www.digicert.com/kb/digicert-root-certificates.htm#roots

BuildArch: noarch

Source: %name-%version.tar

Requires: ca-trust

%description
This package contains DigiCert CA Root used at nuget.org.

%prep
%setup

%install
mkdir -p %buildroot%pkidir/
cat 348115.pem 4478377662.pem DigiCertTrustedRootG4.crt.pem >%buildroot%pkidir/%name.pem

%files
%pkidir/%name.pem

%changelog
* Mon Dec 09 2024 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add DigiCertTrustedRootG4 (ALT bug 49566)

* Fri Mar 01 2024 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus

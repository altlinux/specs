%define pkidir %_datadir/pki/ca-trust-source/anchors

Name: ca-certificates-nuget.org
Version: 0.1
Release: alt1

Summary: DigiCert CA Root for nuget.org
License: Distributable
Group: Other

BuildArch: noarch

Source: %name-%version.tar

Requires: ca-trust

%description
This package contains DigiCert CA Root used at nuget.org.

%prep
%setup

%install
mkdir -p %buildroot%pkidir/
cat 348115.pem 4478377662.pem >%buildroot%pkidir/%name.pem

%files
%pkidir/%name.pem

%changelog
* Fri Mar 01 2024 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus

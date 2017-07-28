Name: ca-gost-certificates
Version: 2017.07.28
Release: alt1

Summary: GOST CA Certificates

License: Public Domain
Group: System/Base
Url: https://e-trust.gosuslugi.ru

BuildArch: noarch

# TODOSource-url: https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion
Source: %name-%version.tar

BuildRequires: wget xsltproc

%description
This package contains a bundle of X.509 certificates of russian government public
Certificate Authorities (CA).

%prep
%setup

%build
./convert.sh

%install
mkdir -p %buildroot%_datadir/%name/
#cp -a guc/* %buildroot%_datadir/%name/
cp -a auc/* %buildroot%_datadir/%name/

%files
%_datadir/%name/

%changelog
* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.07.28-alt1
- initial build for ALT Sisyphus

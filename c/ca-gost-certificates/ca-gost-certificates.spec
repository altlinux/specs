Name: ca-gost-certificates
Version: 2017.07.28
Release: alt3

Summary: GOST CA Certificates

License: Public Domain
Group: System/Base
Url: https://e-trust.gosuslugi.ru

BuildArch: noarch

# TODOSource-url: https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion
Source: %name-%version.tar

BuildRequires: openssl

%description
This package contains a bundle of X.509 certificates of russian government public
Certificate Authorities (CA).

%prep
%setup

%build
# TODO: need update bundle /usr/share/ca-certificates/ca-bundle.crt
#./verify.sh || true
./convert.sh

%install
mkdir -p %buildroot%_datadir/%name/
install -m644 ca-gost-bundle.crt %buildroot%_datadir/%name/
cp -a guc-pem/ %buildroot%_datadir/%name/
#cp -a auc/ %buildroot%_datadir/%name/
#cp crl.list crl.url.failed.list %buildroot%_datadir/%name/

%files
%doc README.md
%_datadir/%name/

%changelog
* Sun Sep 24 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.07.28-alt3
- initial build for ALT Sisyphus

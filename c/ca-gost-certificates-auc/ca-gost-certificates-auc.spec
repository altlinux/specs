# update procedure:
# $ download.sh
# $ download_crl.sh
Name: ca-gost-certificates-auc
Version: 2017.10.22
Release: alt1

Summary: GOST CA intermediate certificates

License: Public Domain
Group: System/Base
Url: https://e-trust.gosuslugi.ru

BuildArch: noarch

# TODOSource-url: https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion
Source: %name-%version.tar

BuildRequires: xsltproc openssl

# See https://bugzilla.altlinux.org/show_bug.cgi?id=33703
BuildRequires: libxmlsec1 libxmlsec1-openssl-devel ca-gost-certificates

Requires: ca-gost-certificates

AutoReq: no

%description
This package contains a bundle of intermediate X.509 certificates of russian government public
Certificate Authorities (CA).

%package crl
Summary: GOST CA CRL intermediate certificates
Group: System/Base
Requires: %name = %version-%release
BuildArch: noarch

%description crl
This package contains a bundle of CRL intermediate X.509 certificates of russian government public
Certificate Authorities (CA).

%prep
%setup

%build
# TODO: need update bundle /usr/share/ca-certificates/ca-bundle.crt
# check sign on downloaded TSL xml
./verify.sh || true
./convert.sh

%install
mkdir -p %buildroot%_datadir/%name/
install -m644 ca-gost-intermediate-bundle.crt %buildroot%_datadir/%name/
cp -a crl/ %buildroot%_datadir/%name/
cp -a crl-pem/ %buildroot%_datadir/%name/
cp -a auc/ %buildroot%_datadir/%name/
cp -a auc-pem/ %buildroot%_datadir/%name/
cp crl.list crl.url.failed.list %buildroot%_datadir/%name/

%files
%doc README.md
%_datadir/%name/ca-gost-intermediate-bundle.crt
%_datadir/%name/auc/
%_datadir/%name/auc-pem/

%files crl
%_datadir/%name/crl.*
%_datadir/%name/crl/
%_datadir/%name/crl-pem/

%changelog
* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.10.22-alt1
- update 22.10.2017

* Sun Sep 24 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.09.24-alt1
- initial build for ALT Sisyphus

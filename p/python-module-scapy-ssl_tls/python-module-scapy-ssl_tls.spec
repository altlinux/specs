%define module_name scapy_ssl_tls

Name: python-module-scapy-ssl_tls
Version: 1.2.3.1
Release: alt1

Summary: SSL/TLS layers for scapy the interactive packet manipulation tool

Group: Development/Python
License: GPL3
Url: https://github.com/tintinweb/scapy-ssl_tls

# Source-url: https://github.com/tintinweb/scapy-ssl_tls/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-distribute

%description
SSL/TLS and DTLS layers and TLS utiltiy functions for Scapy.

An offensive stack for SSLv2, SSLv3 (TLS), TLS, DTLS penetration
testing providing easy access to packet crafting, automatic dissection,
encryption, decryption, session tracking, automated handshakes,
TLSSocket abstraction, cryptography containers, predefined hooks,
SSL sniffing including minimalistic PCAP stream decryption (RSA_WITH_*),
fuzzing and security scanning
(Renegotiation, Heartbleed, Poodle, Logjam/Freak, various Buffer overflows, ...).

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%module_name/
%python_sitelibdir/%module_name-*egg-info

%changelog
* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.3.1-alt1
- new version 1.2.3.1 (with rpmrb script)

* Tue Mar 01 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Sisyphus


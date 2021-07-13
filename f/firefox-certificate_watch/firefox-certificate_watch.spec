# SPEC file for the Certificate Watch Firefox extension

%define rname	certificate_watch
%define cid	\{ab8c066f-9e3e-4aa3-997e-dca3520fecd0\}

Name:		%firefox_name-%rname
Version:	1.12.0
Release:	alt1

Summary:	Certificate Watch Firefox extension
Summary(ru_RU.UTF-8):	расширение Certificate Watch для Firefox

License:	%asl 2.0
Group:		Networking/WWW
URL:		https://github.com/PilzAdam/CertificateWatch
#URL:		https://addons.mozilla.org/firefox/addon/certwatch/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Certificate Watch Firefox extension watches over the TLS certificates
that websites present to you and warns when the certificate for
a domain changes.

If a new domain is encountered, its certificate is added to the local
storage of this add-on. Future connections to that domain will check
that the certificate is still the same as in the local storage.

%description -l ru_RU.UTF-8
Расширение Certificate Watch для Firefox отслеживает использование
сертификатов TSL веб-сайтами и предупреждает в случае изменения
сертификата домена.

При первом посещении сайта его сертификат добавляется в локальное
хранилище данного расширения. При последующих соединениях с известным
сайтом проверяется, не изменился ли его сертификат по сравнению
с локальной копией.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.12.0-alt1
- Initial build for ALT Linux Sisyphus

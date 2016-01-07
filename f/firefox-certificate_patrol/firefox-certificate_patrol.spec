# SPEC file for Gmail Manager extension

%define rname	certificate_patrol
%define version 2.0.14.1
%define release alt1
%define cid 	CertPatrol@PSYC.EU
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Certificate Patrol extension for Firefox
Summary(ru_RU.UTF-8):	расширение Certificate Patrol для Firefox

License:	%mpl 1.1
Group:		Networking/WWW
# URL:		http://patrol.psyced.org/
URL:		https://addons.mozilla.org/ru/firefox/addon/certificate-patrol/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
Web browser trusts a lot of certification authorities and chained
sub-authorities, and it does so blindly.

The root CAs can delegate permission to issue certificates to an
unlimited amount of subordinate CAs (SCA) just by signing their
certificate, and everyone can even buy such a CA from GeoTrust or
elsewhere.

It is unclear how many intermediate certification authorities
really exist, and yet each of them has "god-like power" to
impersonate any https web site using a Man in the Middle (MITM)
attack scenario.

Certificate Patrol add-on reveals when certificates are updated,
so you can ensure it was a legitimate change.

%description -l ru_RU.UTF-8
Веб-браузер доверяет большому числу различных центров сертификации
и принимает подписанные ими сертификаты сайтов молча.

Центры сертификации (CA) могут делегировать полномочия по выпуску
сертификатов неограниченному числу подчинённых центров сертификации
(SubCA), просто подписывая их сертификаты, и кто угодно может купить
такой SubCA, например от GeoTrust или других центров сертификации.

Сколько сейчас существует таких промежуточных центров сертификации -
Неизвестно, но с помощью каждого из них можно осуществить атаку
"человек посередине" (Man in the Middle, MITM) - выпустив для
произвольного сайта сертификат, который будет молча принят браузером.

Расширение Certificate Patrol отслеживает изменения сертификатов
посещавшихся ранее сайтов, и позволяет быть уверенным в
добропорядочности таких изменений.

%prep
%setup -c

%install
mkdir -p --  %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.14.1-alt1
- Signed version to work with Firefox >= 43.x

* Wed Oct 30 2013 Andrey Cherepanov <cas@altlinux.org> 2.0.14-alt2.1
- Update maxVersion for Firefox/Thunderbird 24.x and Seamonkey 2.22.x

* Sun May 26 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.14-alt2
- Fix extention CID

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.14-alt1
- Initial build for ALTLinux Sisyphus

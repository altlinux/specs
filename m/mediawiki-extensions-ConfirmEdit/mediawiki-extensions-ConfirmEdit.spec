%define oname ConfirmEdit
%define major 1.16
%define dversion MW%major
#define dversion trunk
%define revision r62678

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1.1

BuildArch: noarch

Group: Networking/WWW
Summary: The ConfirmEdit extension enables a simple text Captcha

Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-%dversion-%revision.tar.gz
Source: %oname-%version.tar

%description
The ConfirmEdit extension enables a simple text Captcha that will probably
not allow most bots to edit your site. It was designed largely by Brion
Vibber. The FancyCaptcha and reCAPTCHA addons create more complex
image captchas.  Captchas are a way of combating automated edits,
helping to ensure that wiki edits are being made by real humans rather
than bots. This can be particularly useful for reducing the problem of
wiki spam, but captchas reduce accessibility and cause inconvenience to
human users.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.16.r62678-alt1.1
- Rebuild with Python-2.7

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62678-alt1
- initial build for ALT Linux Sisyphus

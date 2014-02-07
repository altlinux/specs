%define oname Validator

Name: mediawiki-extensions-%oname
Version: 1.0
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Validator provides an easy way for other extensions to validate parameters of parser functions and tag extensions, set default values and generate error messages.
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.22

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-Validator/legacy.tar.gz/master
Source: %oname-%version.tar

%description
Validator is an extension that makes parameter validation functionality
available to other extensions. This enables other extensions to validate
parameters, set them to their defaults, and generate error messages,
while only defining the parameters and their criteria. The goal of
this extension is to facilitate the handling of parameters in other
extension, and generalize the error output. By itself, it does not add
any functionality to the user end.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus

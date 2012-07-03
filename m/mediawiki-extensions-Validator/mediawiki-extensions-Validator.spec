%define oname Validator

Name: mediawiki-extensions-%oname
Version: 0.2
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Validator provides an easy way for other extensions to validate parameters of parser functions and tag extensions, set default values and generate error messages.
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.15.1-alt4

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://code.bn2vs.com/viewtopic.php?mode=attach&id=251
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
* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus

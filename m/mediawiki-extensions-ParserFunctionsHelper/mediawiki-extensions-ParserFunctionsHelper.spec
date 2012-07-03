%define oname ParserFunctionsHelper
%define major 1.0.0
%define revision r1223

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

Summary: Provides services to parser function extensions which require inserting content after the parsing phase

License: No license specified
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.15.1-alt4

Requires: mediawiki-extensions-StubManager

# http://mediawiki.googlecode.com/svn/trunk/extensions/SecureHTML/
Source0: %oname-%version.tar

%description
Provides services to parser function extensions which require
inserting content after the parsing phase.
This extension is meant to serve other extensions
i.e. it does not provide end-user functionality by itself.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 45 %oname

%files -f %oname.files

%changelog
* Wed May 26 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.0.r1223-alt1
- initial build for ALT Linux Sisyphus

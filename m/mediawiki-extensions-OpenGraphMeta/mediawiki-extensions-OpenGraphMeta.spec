%define oname OpenGraphMeta

Name: mediawiki-extensions-%oname
Version: 0.2012
Release: alt1

Summary: OpenGraphMeta provides OpenGraph protocol metadata for articles on the wiki for 3rd parties like Facebook to extract

License: GPLv2+
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.15.1-alt4

# https://gerrit.wikimedia.org/r/p/mediawiki/extensions/OpenGraphMeta.git
Source: %name-%version.tar

%description
OpenGraphMeta provides OpenGraph protocol metadata for articles on the wiki
for 3rd parties like Facebook to extract. The primary use for this extension
is for any wiki that provides its users a button to "Like" pages on the wiki,
especially if the wiki uses a custom default skin.

%prep
%setup

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sat Feb 02 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2012-alt1
- initial build for ALT Linux Sisyphus

%define oname SecureHTML
%define major 2.3.0
%define revision r1223

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

Summary: This MediaWiki extension provides a secure way to include raw HTML code on a page

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
This extension allows editors to add HTML section(s) or pages on a wiki page.
This extension can only be used on protected pages,
but allows an editor to add a protected template on an unprotected, editable page.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Wed May 26 2010 Vitaly Lipatov <lav@altlinux.ru> 2.3.0.r1223-alt1
- initial build for ALT Linux Sisyphus


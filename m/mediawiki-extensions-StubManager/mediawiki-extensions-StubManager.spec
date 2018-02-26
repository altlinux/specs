%define oname StubManager

Name: mediawiki-extensions-%oname
Version: 1.3.2
Release: alt1

Summary: This extension lowers loading times which speeds up MediaWiki sites

License:  No license specified
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.15.1-alt4

# http://mediawiki.googlecode.com/svn/tags/StubManager/
#Source: http://mediawiki.googlecode.com/svn/tags/StubManager/%oname-%version.tar
Source: %oname-%version.tar

%description
This extension lowers loading times which speeds up MediaWiki sites. This
is done by addressing 'rare events' handling through class object
'stubs'. For infrequent events (of course this is relative!), use this
extension to create a 'stub object' for the required hooks.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 40 %oname

%files -f %oname.files

%changelog
* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- initial build for ALT Linux Sisyphus


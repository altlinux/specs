%define oname NewUserNotif
%define major 1.16
%define revision r60802

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

Summary: This MediaWiki extension sends email notification when user accounts are created

License:  No license specified
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.16

Requires: mediawiki-extensions-StubManager

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-MW%major-%revision.tar.gz
Source: %oname-%version.tar

%description
The New User Email Notification extension sends a customisable email to
specified recipients when a new user account is created. The extension
can send to multiple users, and additional email addresses, and is useful
for keeping track of account creation on a small wiki.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Wed Sep 28 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r60802-alt1
- initial build for ALT Linux Sisyphus


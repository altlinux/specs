%define oname UserMerge

Name: mediawiki-extensions-%oname
Version: 1.8.1
Release: alt1
Serial: 1

BuildArch: noarch

Group: Networking/WWW
Summary: User Merge and Delete extension allows to merge one Wiki user's account with another one

Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.22

# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-UserMerge/legacy.tar.gz/REL1_22
Source: %oname-%version.tar

%description
User Merge and Delete extension allows Wiki users with the 'usermerge'
permission (Bureaucrat by default) to merge one Wiki user's account
with another Wiki user's account - deleting following merge is also
supported. You may not delete a user without merging first - omitting
the "New User" field will auto-populate the New User as "Anonymous",
user_id 0 and ask you to confirm merge to Anonymous.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.0-alt1
- update to 1.7.0 against MW 1.20

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66255-alt1
- initial build for ALT Linux Sisyphus

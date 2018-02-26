%define oname UserMerge
%define major 1.16
%define dversion MW%major
#define dversion trunk
%define revision r66255

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: User Merge and Delete extension allows to merge one Wiki user's account with another one

Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-%dversion-%revision.tar.gz
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
* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66255-alt1
- initial build for ALT Linux Sisyphus

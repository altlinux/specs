%define oname UserMerge
%define mwversion 1.46
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.10.2
Release: alt1
Serial: 1

Summary: User Merge and Delete extension allows to merge one Wiki user's account with another one

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

Requires: mediawiki >= %mwversion

# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-%oname/tar.gz/refs/heads/%MWREL
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
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.2-alt1
- new version 1.10.2 (REL1_46, extension.json format, MediaWiki 1.46)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)
- require mediawiki >= 1.46 (as in extension.json)
- remove development files (tests, node and composer files) from package

* Sun Mar 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.1-alt2
- cleanup spec
- build with real last sources

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.0-alt1
- update to 1.7.0 against MW 1.20

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66255-alt1
- initial build for ALT Linux Sisyphus
